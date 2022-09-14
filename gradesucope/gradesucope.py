from sys import stdin
import difflib
import subprocess32 as subprocess
import os
import unittest
import re


class HappyDiffer(difflib.Differ):
    def _qformat(self, aline, bline, atags, btags):
        if hasattr(difflib, "_keep_original_ws"):
            atags = difflib._keep_original_ws(aline, atags).rstrip()
            btags = difflib._keep_original_ws(bline, btags).rstrip()
            pass

        yield "Yours: " + aline
        if atags:
            yield f"       {atags}\n"

        yield "Mine:  " + bline
        if btags:
            yield f"       {btags}\n"

    def _dump(self, tag, x, lo, hi):
        if tag == '+':
            tag = "Mine: "
        elif tag == '-':
            tag = "Yours:  "
        elif tag == ' ':
            tag = "Ours: "
        for i in range(lo, hi):
            if x[i] == '\n':
                yield '%s %s' % (tag, "(newline)")
                continue
            yield '%s %s' % (tag, x[i])


def MandatoryPostProcessor(result):
    # In the case where the student has a mandatory
    # test that is failing, no matter how else they
    # scored, we reset their scores to 0.
    for t in result["tests"]:
        if "tags" in t and\
           "mandatory" in t["tags"] and\
           t["score"] == 0.0:
            result["score"] = 0.0


class UCTestCase(unittest.TestCase):
    def generate_string_comparison_function(self):
        def string_compare(left, right, msg=None):
            if left != right:
                raise self.failureException(
                    f"{msg}\n\n{str.strip(left)} != {str.strip(right)}")
        return string_compare

    def __init__(self, *args, **kwargs):
        super(UCTestCase, self).__init__(*args, **kwargs)
        # By default, suppress any default output from the assertXXX functions
        # about why the assertion failed and *only* print the text given
        # by the named parameter `msg`.
        self.longMessage = False
        self.addTypeEqualityFunc(
            str, UCTestCase.generate_string_comparison_function(self))


class FileExistsTestCase(UCTestCase):
    # Helper methods
    def file_exists(self, filename, path="/autograder/source/"):
        """Check if file exists"""
        self.assertTrue(os.path.isfile(path + filename),
                        msg="No " + filename + " file found in submission. "
                        "If submitting via GitHub make sure the file is "
                        "in '/labX' where 'X' is the lab number.")


class StringContentsMatchTestCase(UCTestCase):
    def count_matches(self, contents, match):
        """ Count how many time match matches contents"""

        try:
            regexp = re.compile(match, re.MULTILINE)
        except re.error as _:
            return -1
        return len(regexp.findall(contents))

class FileContentsMatchTestCase(StringContentsMatchTestCase):
    def count_file_matches(self, filename, match, path="/autograder/source/"):
        """ Count how many time match matches the text in filename """
        file_contents = ""
        try:
            with open(path + "/" + filename, "r") as file:
                file_contents = file.read()
        except IOError as ioe:
            return -1
        return self.count_matches(file_contents, match)


class GoldenTestCase(UCTestCase):
    # Helper methods
    def read_golden(self, filename, path="/autograder/source/"):
        golden_contents = ""
        with open(path + filename, 'r') as fh:
            golden_contents = "".join(fh.readlines())
        return golden_contents

    def match_golden(self, actual, golden):
        self.assertEqual(actual, golden,
                         msg="Be sure to check the example output in the "
                         "lab write up!")

    def diff_golden(self, actual, golden):
        self.assertTrue(
            actual != golden, msg="Internal autograder error: diff_golden called when output was correct.")
        print("Below is an explanation of how your program's output differs from the\nexpected output.")
        print((":" * 80))
        print("\n".join(HappyDiffer().compare(
            [ x + "\n" for x in actual.split("\n")],
            [ x + "\n" for x in golden.split("\n")])))

    # Test Cases
    def student_view(self):
        actual = self.generate_actual()
        golden = self.generate_golden()
        if actual != golden:
            self.diff_golden(actual, golden)
        self.match_golden(actual, golden)

    def generate_actual(self):
        raise NotImplementedError()

    def generate_golden(self):
        raise NotImplementedError()


class ExecutableTestCase(UCTestCase):
    def execute(self, parameters, exe, path="/autograder/source/build/"):
        args = [path + exe]
        args.extend(parameters)
        exe = subprocess.Popen(args,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,)
        output = exe.stdout.read().decode()
        exe.terminate()
        return output

class ExecutableGoldenTestCase(ExecutableTestCase, GoldenTestCase):
    pass

class InteractiveExecutableTestCase(UCTestCase):
    def execute(self, parameters, exe, inputs, path="/autograder/source/build/"):
        args = [path + exe]
        args.extend(parameters)
        exe = subprocess.Popen(args,
                               stdin=subprocess.PIPE,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE,
                               universal_newlines=True,)
        lined_inputs = [ x + "\n" for x in inputs]
        exe.stdin.write("".join(lined_inputs))
        exe.stdin.flush()
        output = exe.stdout.read()
        exe.terminate()
        return output

class InteractiveExecutableGoldenTestCase(InteractiveExecutableTestCase, GoldenTestCase):
    pass