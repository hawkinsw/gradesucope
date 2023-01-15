from shutil import ExecError
import unittest
from gradescope_utils.autograder_utils.json_test_runner import JSONTestRunner
from gradescope_utils.autograder_utils.decorators import weight

from gradesucope.gradesucope import InteractiveExecutableOutputMatchTestCase, ExecutableGoldenTestCase, GoldenTestCase, InteractiveExecutableGoldenTestCase, MandatoryPostProcessor, FileContentsMatchTestCase, StringContentsMatchTestCase


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
    suite.addTest(
        simple_failing_interactive_executable_golden_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_failing_extra_character_interactive_executable_golden_test_case(InteractiveExecutableGoldenTestCase):
    dir = "test/"
    golden_file = "echo.golden"
    success_exe = "echo_extra_character_test"

    def generate_actual(self):
        return self.execute([], simple_failing_extra_character_interactive_executable_golden_test_case.success_exe, ("2", "input2"), path=simple_failing_interactive_executable_golden_test_case.dir)

    def generate_golden(self):
        return self.read_golden(simple_failing_extra_character_interactive_executable_golden_test_case.golden_file, path=simple_failing_extra_character_interactive_executable_golden_test_case.dir)

    @weight(10)
    def test_me(self):
        """test_me: simple_failing_interactive_executable_golden_test_case."""
        self.student_view()


def perform_simple_failing_extra_character_interactive_executable_golden_test_case():
    suite = unittest.TestSuite()
    suite.addTest(
        simple_failing_extra_character_interactive_executable_golden_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_failing_missing_newline_interactive_executable_golden_test_case(InteractiveExecutableGoldenTestCase):
    dir = "test/"
    golden_file = "echo.golden"
    success_exe = "echo_missing_newline_test"

    def generate_actual(self):
        return self.execute([], simple_failing_missing_newline_interactive_executable_golden_test_case.success_exe, ("2", "input2"), path=simple_failing_interactive_executable_golden_test_case.dir)

    def generate_golden(self):
        return self.read_golden(simple_failing_missing_newline_interactive_executable_golden_test_case.golden_file, path=simple_failing_missing_newline_interactive_executable_golden_test_case.dir)

    @weight(10)
    def test_me(self):
        """test_me: simple_failing_interactive_executable_golden_test_case."""
        self.student_view()


def perform_simple_failing_missing_newline_interactive_executable_golden_test_case():
    suite = unittest.TestSuite()
    suite.addTest(
        simple_failing_missing_newline_interactive_executable_golden_test_case("test_me"))
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
    suite.addTest(
        simple_passing_interactive_executable_golden_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_file_contents_match_test_case(FileContentsMatchTestCase):
    dir = "test/"
    match_file = "match_test.txt"

    @weight(10)
    def test_me(self):
        """test_me: simple_file_contents_match_test_case."""
        result = self.count_file_matches(self.match_file, "here: ", self.dir)
        self.assertTrue(result == 2,
                        msg="" + str(result) + " matches found but expected 2.")


def perform_simple_file_contents_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_file_contents_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_file_contents_no_match_test_case(FileContentsMatchTestCase):
    dir = "test/"
    match_file = "match_test.txt"

    @weight(10)
    def test_me(self):
        """test_me: simple_file_contents_no_match_test_case."""
        result = self.count_file_matches(self.match_file, "there: ", self.dir)
        self.assertTrue(result == 0,
                        msg="" + str(result) + " matches found but expected 0.")


def perform_simple_file_contents_no_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_file_contents_no_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_file_contents_one_match_test_case(FileContentsMatchTestCase):
    dir = "test/"
    match_file = "match_test.txt"

    @weight(10)
    def test_me(self):
        """test_me: simple_file_contents_one_match_test_case."""
        result = self.count_file_matches(self.match_file, "one ", self.dir)
        self.assertTrue(result == 1,
                        msg="" + str(result) + " matches found but expected 1.")


def perform_simple_file_contents_one_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_file_contents_one_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_file_contents_end_match_test_case(FileContentsMatchTestCase):
    dir = "test/"
    match_file = "match_test.txt"

    @weight(10)
    def test_me(self):
        """test_me: simple_file_contents_match_test_case."""
        result = self.count_file_matches(
            self.match_file, "another\.", self.dir)
        self.assertTrue(result == 1,
                        msg="" + str(result) + " matches found but expected 1.")


def perform_simple_file_contents_end_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_file_contents_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_file_contents_bad_re_match_test_case(FileContentsMatchTestCase):
    dir = "test/"
    match_file = "match_test.txt"

    @weight(10)
    def test_me(self):
        """test_me: simple_file_contents_bad_re_match_test_case."""
        result = self.count_file_matches(
            self.match_file, "(another\.", self.dir)
        self.assertTrue(result == -1,
                        msg="" + str(result) + " matches found but expected -1.")


def perform_simple_file_contents_bad_re_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_file_contents_bad_re_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_file_contents_missing_file_test_case(FileContentsMatchTestCase):
    dir = "test/"
    match_file = "missing.txt"

    @weight(10)
    def test_me(self):
        """test_me: simple_file_contents_missing_file_test_case."""
        result = self.count_file_matches(
            self.match_file, "empty on purpose", self.dir)
        self.assertTrue(result == -1,
                        msg="" + str(result) + " matches found but expected -1.")


def perform_simple_file_contents_missing_file_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_file_contents_missing_file_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_string_contents_end_match_test_case(StringContentsMatchTestCase):
    match_contents = "this is the\nend of\nthe road."

    @weight(10)
    def test_me(self):
        """test_me: simple_string_contents_end_match_test_case."""
        result = self.count_matches(self.match_contents, "road\.$")
        self.assertTrue(result == 1,
                        msg="" + str(result) + " matches found but expected 1.")


def perform_simple_string_contents_end_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_string_contents_end_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_string_contents_start_match_test_case(StringContentsMatchTestCase):
    match_contents = "this is the\nend of\nthe road."

    @weight(10)
    def test_me(self):
        """test_me: simple_string_contents_start_match_test_case."""
        result = self.count_matches(self.match_contents, "^this")
        self.assertTrue(result == 1,
                        msg="" + str(result) + " matches found but expected 1.")


def perform_simple_string_contents_start_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_string_contents_start_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_string_contents_eol_match_test_case(StringContentsMatchTestCase):
    match_contents = """this is the
    end of
    the road."""

    @weight(10)
    def test_me(self):
        """test_me: simple_string_contents_eol_match_test_case."""
        result = self.count_matches(self.match_contents, "of\n")
        self.assertTrue(result == 1,
                        msg="" + str(result) + " matches found but expected 1.")


def perform_simple_string_contents_eol_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_string_contents_eol_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class simple_string_contents_no_match_test_case(StringContentsMatchTestCase):
    match_contents = "this is the\nend of\nthe road."

    @weight(10)
    def test_me(self):
        """test_me: simple_string_contents_no_match_test_case."""
        result = self.count_matches(self.match_contents, "extra")
        self.assertTrue(result == 0,
                        msg="" + str(result) + " matches found but expected 0.")


def perform_simple_string_contents_no_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(simple_string_contents_no_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


class interactive_executable_output_match_test_case(InteractiveExecutableOutputMatchTestCase):
    dir = "test/"
    executable_name = "multiline_output"

    @weight(10)
    def test_me(self):
        """test_me: interactive_executable_output_match_test_case."""
        matches = self.count_output_matches([], interactive_executable_output_match_test_case.executable_name, (
        ), "^This: $", interactive_executable_output_match_test_case.dir)
        self.assertTrue(matches == 1,
                        msg="" + str(matches) + " matches found but expected 1.")

        matches = self.count_output_matches([], interactive_executable_output_match_test_case.executable_name, (
        ), "^Is: Not$", interactive_executable_output_match_test_case.dir)
        self.assertTrue(matches == 1,
                        msg="" + str(matches) + " matches found but expected 1.")

        matches = self.count_output_matches([], interactive_executable_output_match_test_case.executable_name, (
        ), "^Is:$", interactive_executable_output_match_test_case.dir)
        self.assertTrue(matches == 0,
                        msg="" + str(matches) + " matches found but expected 1.")


def perform_interactive_executable_output_match_test_case():
    suite = unittest.TestSuite()
    suite.addTest(interactive_executable_output_match_test_case("test_me"))
    JSONTestRunner(verbosity=1, post_processor=reformatting_post_processor(
        MandatoryPostProcessor)).run(suite)


if __name__ == '__main__':
    perform_simple_golden_test()
    perform_failing_executable_golden_test()
    perform_passing_executable_golden_test()
    perform_simple_passing_interactive_executable_golden_test_case()
    perform_simple_failing_interactive_executable_golden_test_case()
    perform_simple_failing_extra_character_interactive_executable_golden_test_case()
    perform_simple_failing_missing_newline_interactive_executable_golden_test_case()
    perform_simple_file_contents_match_test_case()
    perform_simple_file_contents_no_match_test_case()
    perform_simple_file_contents_one_match_test_case()
    perform_simple_file_contents_end_match_test_case()
    perform_simple_file_contents_bad_re_match_test_case()
    perform_simple_file_contents_missing_file_test_case()
    perform_simple_string_contents_end_match_test_case()
    perform_simple_string_contents_start_match_test_case()
    perform_simple_string_contents_no_match_test_case()
    perform_simple_string_contents_eol_match_test_case()
    perform_interactive_executable_output_match_test_case()
