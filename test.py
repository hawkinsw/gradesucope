from shutil import ExecError
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
from gradescope_utils.autograder_utils.decorators import weight

from gradesucope.gradesucope import ExecutableGoldenTestCase, GoldenTestCase, InteractiveExecutableGoldenTestCase, MandatoryPostProcessor


def reformatting_post_processor(next):
    def generated_post_processor(data):
        if 'output' in data['tests'][0]:
            print(data['tests'][0]['output'])
        next(data)
    return generated_post_processor


class simple_golden_test_case(GoldenTestCase):
    def generate_golden(self):
        return "one, two, three"

    def generate_actual(self):
        return "One, tWo, threE"

    @weight(10)
    def test_me(self):
        """test_me: simple_golden_test_case."""
        self.student_view()


def perform_simple_golden_test():
    suite = unittest.TestSuite()
    suite.addTest(simple_golden_test_case("test_me"))
    output = JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_failing_executable_golden_test_case(ExecutableGoldenTestCase):
    dir = "test/"
    golden_file = "test.golden"
    fail_exe = "fail_test"

    def generate_actual(self):
        return self.execute([], simple_failing_executable_golden_test_case.fail_exe, path=simple_failing_executable_golden_test_case.dir)

    def generate_golden(self):
        return self.read_golden(simple_failing_executable_golden_test_case.golden_file, path=simple_failing_executable_golden_test_case.dir)

    @weight(10)
    def test_me(self):
        """test_me: simple_failing_executable_golden_test_case."""
        self.student_view()


def perform_failing_executable_golden_test():
    suite = unittest.TestSuite()
    suite.addTest(simple_failing_executable_golden_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_passing_executable_golden_test_case(ExecutableGoldenTestCase):
    dir = "test/"
    golden_file = "test.golden"
    success_exe = "success_test"

    def generate_actual(self):
        return self.execute([], simple_passing_executable_golden_test_case.success_exe, path=simple_passing_executable_golden_test_case.dir)

    def generate_golden(self):
        return self.read_golden(simple_passing_executable_golden_test_case.golden_file, path=simple_passing_executable_golden_test_case.dir)

    @weight(10)
    def test_me(self):
        """test_me: simple_passing_executable_golden_test_case."""
        self.student_view()


def perform_passing_executable_golden_test():
    suite = unittest.TestSuite()
    suite.addTest(simple_passing_executable_golden_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)

class simple_failing_interactive_executable_golden_test_case(InteractiveExecutableGoldenTestCase):
    dir = "test/"
    golden_file = "echo.golden"
    success_exe = "echo_test"

    def generate_actual(self):
        return self.execute([], simple_failing_interactive_executable_golden_test_case.success_exe, ("2", "input2"), path=simple_failing_interactive_executable_golden_test_case.dir)

    def generate_golden(self):
        return self.read_golden(simple_failing_interactive_executable_golden_test_case.golden_file, path=simple_failing_interactive_executable_golden_test_case.dir)

    @weight(10)
    def test_me(self):
        """test_me: simple_failing_interactive_executable_golden_test_case."""
        self.student_view()


def perform_simple_failing_interactive_executable_golden_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_failing_interactive_executable_golden_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)



class simple_passing_interactive_executable_golden_test_case(InteractiveExecutableGoldenTestCase):
    dir = "test/"
    golden_file = "echo.golden"
    success_exe = "echo_test"

    def generate_actual(self):
        return self.execute([], simple_passing_interactive_executable_golden_test_case.success_exe, ("1", "input2"), path=simple_passing_interactive_executable_golden_test_case.dir)

    def generate_golden(self):
        return self.read_golden(simple_passing_interactive_executable_golden_test_case.golden_file, path=simple_passing_interactive_executable_golden_test_case.dir)

    @weight(10)
    def test_me(self):
        """test_me: simple_passing_interactive_executable_golden_test_case."""
        self.student_view()


def perform_simple_passing_interactive_executable_golden_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_passing_interactive_executable_golden_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)

if __name__ == '__main__':
    perform_simple_golden_test()
    perform_failing_executable_golden_test()
    perform_passing_executable_golden_test()
    perform_simple_passing_interactive_executable_golden_test_case()
    perform_simple_failing_interactive_executable_golden_test_case()
