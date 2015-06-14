__author__ = 'Eidan Wasser'
"""Running tests"""

from unittest import result
import time, sys, datetime
from unittest.signals import registerResult
from TestCaseInfo import get_info
__unittest = True

class Result(result.TestResult):
    """A test result class that can print formatted text results to a stream.

    Used by TextTestRunner.
    """
    separator1 = '=' * 70
    separator2 = '-' * 70
    tab = " " * 10
    failedList = []

    def __init__(self, stream, descriptions, verbosity, runName):
        super(Result, self).__init__(stream, descriptions, verbosity)
        self.stream = stream
        self.descriptions = descriptions
        self.runName = runName

    def getDescription(self, test):
        doc_first_line = test.shortDescription()
        if self.descriptions and doc_first_line:
            return '\n'.join((str(test), doc_first_line))
        else:
            return get_info(str(test))

    def startTest(self, test):
        super(Result, self).startTest(test)
        pass

    def startTestRun(self):
        branch = "Placeholder"
        d = datetime.datetime.now()
        self.stream.write("Test Run: " + self.runName + self.tab + "Start time: " + d.strftime("%d/%m/%y %H:%M:%S"))
        self.stream.writeln("Branch: " + branch)
        self.stream.writeln()

    def stopTestRun(self):
        super(Result, self).stopTestRun()
        self.stream.writeln("Failed Test Cases:")
        for i in self.failedList:
            self.stream.writeln(i)

    def addSuccess(self, test):
        pass
        """
        super(Result, self).addSuccess(test)
        write = str(self.testsRun) + ". "
        write = write + self.getDescription(test) + "..."
        write = write + "OK"
        self.failedList.append(write)
        """

    def addError(self, test, err):
        super(Result, self).addError(test, err)
        write = str(self.testsRun) + ". "
        write = write + self.getDescription(test) + "..."
        write = write + "ERROR"
        self.failedList.append(write)

    def addFailure(self, test, err):
        super(Result, self).addFailure(test, err)
        write = str(self.testsRun) + ". "
        write = write + self.getDescription(test) + "..."
        write = write + "FAIL"
        self.failedList.append(write)
    """
    def addSkip(self, test, reason):
        super(Result, self).addSkip(test, reason)
        self.getTestName(test)
        self.stream.writeln("skipped {0!r}".format(reason))

    def addExpectedFailure(self, test, err):
        super(Result, self).addExpectedFailure(test, err)
        self.getTestName(test)
        self.stream.writeln("expected failure")

    def addUnexpectedSuccess(self, test):
        super(Result, self).addUnexpectedSuccess(test)
        self.getTestName(test)
        self.stream.writeln("unexpected success")
    """

    def printErrors(self):
        self.stream.writeln()
        self.printErrorList('ERROR', self.errors)
        self.printErrorList('FAIL', self.failures)

    def printErrorList(self, flavour, errors):
        for test, err in errors:
            self.stream.writeln(self.separator1)
            self.stream.writeln("%s: %s - %s" % (flavour,self.getDescription(test), str(test)))
            self.stream.writeln(self.separator2)
            self.stream.writeln("%s" % err)


class Runner(object):
    """A test runner class that displays results in textual form.

    It prints out the names of tests as they are run, errors as they
    occur, and a summary of the results at the end of the test run.
    """
    resultclass = Result

    def __init__(self, stream=sys.stderr, descriptions=True, verbosity=1,
                 failfast=False, buffer=False, resultclass=None, runName=None):
        self.stream = _WritelnDecorator(stream)
        self.descriptions = descriptions
        self.verbosity = verbosity
        self.failfast = failfast
        self.buffer = buffer
        self.runName = runName
        if resultclass is not None:
            self.resultclass = resultclass

    def _makeResult(self):
        return self.resultclass(self.stream, self.descriptions, self.verbosity, self.runName)

    def run(self, test):
        "Run the given test case or test suite."
        result = self._makeResult()
        registerResult(result)
        result.failfast = self.failfast
        result.buffer = self.buffer
        startTime = time.time()
        
        startTestRun = getattr(result, 'startTestRun', None)
        if startTestRun is not None:
            startTestRun()
        
        try:
            test(result)
        finally:
            stopTestRun = getattr(result, 'stopTestRun', None)

            stopTime = time.time()
            timeTaken = stopTime - startTime

            if hasattr(result, 'separator2'):
                self.stream.writeln(result.separator2)

            run = result.testsRun
            self.stream.writeln("Ran %d test%s in %.3fs" %
                        (run, run != 1 and "s" or "", timeTaken))
            self.stream.writeln()

            expectedFails = unexpectedSuccesses = skipped = 0
            try:
                results = map(len, (result.expectedFailures,
                                    result.unexpectedSuccesses,
                                    result.skipped))
            except AttributeError:
                pass
            else:
                expectedFails, unexpectedSuccesses, skipped = results

            infos = []
            if not result.wasSuccessful():
                self.stream.write("FAILED")
                failed, errored = map(len, (result.failures, result.errors))
                if failed:
                    infos.append("failures=%d" % failed)
                if errored:
                    infos.append("errors=%d" % errored)
            else:
                self.stream.write("OK")
            if skipped:
                infos.append("skipped=%d" % skipped)
            if expectedFails:
                infos.append("expected failures=%d" % expectedFails)
            if unexpectedSuccesses:
                infos.append("unexpected successes=%d" % unexpectedSuccesses)
            if infos:
                self.stream.writeln(" (%s)" % (", ".join(infos),))
            else:
                self.stream.write("\n")

            self.stream.writeln(Result.separator2)
            stopTestRun()

        result.printErrors()

        return result

class _WritelnDecorator(object):
    """Used to decorate file-like objects with a handy 'writeln' method"""
    def __init__(self,stream):
        self.stream = stream

    def __getattr__(self, attr):
        if attr in ('stream', '__getstate__'):
            raise AttributeError(attr)
        return getattr(self.stream,attr)

    def writeln(self, arg=None):
        if arg:
            self.write(arg)
        self.write('\n') # text-mode streams translate to \r\n if needed