import unittest
import sys
import io
import inspect

# See: https://stackoverflow.com/questions/1218933/can-i-redirect-the-stdout-in-python-into-some-sort-of-string-buffer
from contextlib import redirect_stdout

from unittest.mock import patch, mock_open

# Import the 'main function from word_index.py as wi_main
from word_index import main as wi_main


class TestPythonVersion(unittest.TestCase):

    def test_python_version(self):
        """ This is a simple example of a unittest that checks if you are running the right version of Python """
        self.assertEqual(sys.version_info.major, 3, msg="You are not running python 3")
        self.assertEqual(sys.version_info.minor, 7, msg="You are not running python 3.7")


class TestWordIndex(unittest.TestCase):
    # TODO One can implement the following: start+stop and invoke it every time, but it is better to use pytohn context managers for that (see https://book.pythontips.com/en/latest/context_managers.html)

    # def start_record_stdout(self):
    #     """ Create a StringIO object and redirect stdout to it """
    #     self.capturedOutput = io.StringIO()
    #     self.the_sys_out = sys.stdout
    #     sys.stdout = self.capturedOutput
    #
    # def stop_record_stdout(self):
    #     """ Reset the original stdout to avoid polluting the environment """
    #     sys.stdout = self.the_sys_out
    #     output = self.capturedOutput.getvalue()
    #     del self.capturedOutput
    #     return  output
    #
    # def a_test(self):
    #     self.start_record_stdout()
    #     wi_main('./sample.txt')
    #     output = self.stop_record_stdout()



    def test_output_with_an_existing_file(self):
        print(inspect.stack()[0][3]) # Print the name of THIS function

        # Execute main and be sure you capture the output
        with io.StringIO() as buf, redirect_stdout(buf):
            wi_main('./sample.txt')
            output = buf.getvalue()

        # Check the output is not None
        self.assertIsNotNone(output, msg="Output cannot be None")

        # Check the output is not empty
        self.assertNotEqual(output, '', msg="Output cannot be empty")

    def test_output_with_another_existing_file(self):
        print(inspect.stack()[0][3])

        # Execute main and be sure you capture the output
        with io.StringIO() as buf, redirect_stdout(buf):
            wi_main('./long.txt')
            output = buf.getvalue()

        # Check the output is not None
        self.assertIsNotNone(output, msg="Output cannot be None")

        # Check the output is not empty
        self.assertNotEqual(output, '', msg="Output cannot be empty")


class TestWordIndexUsingMocks(unittest.TestCase):
    # See: https://stackoverflow.com/questions/24201908/mock-for-line-in-openfile
    # NOTE: io.StringIO must be terminated explicitly with \n

    def test_output_with_a_mocked_file(self):
        print(inspect.stack()[0][3])

        fake_file_path="/fake/file/path"

        lines= ["foo", "bar", ""] # the last empty line ensures that we have a final '\n'

        fake_file = io.StringIO('\n'.join(lines))

        # Execute main and be sure you capture the output but use mocking to fake a file read by the program
        with io.StringIO() as buf, redirect_stdout(buf):

            with patch('word_index.open', return_value=fake_file, create=True):
                wi_main(fake_file_path)

            output = buf.getvalue()

        # Check the output is not None
        self.assertIsNotNone(output, msg="Output cannot be None")

        # Check the output is not empty
        self.assertNotEqual(output, '', msg="Output cannot be empty")

    def test_output_with_empty_file(self):
        print(inspect.stack()[0][3])

        fake_file_path="/fake/file/path"
        lines = [""]  # the last empty line ensures that we have a final '\n'
        fake_file = io.StringIO('\n'.join(lines))

        # Execute main and be sure you capture the output but use mocking to fake a file read by the program
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('word_index.open', return_value=fake_file, create=True):
                wi_main(fake_file_path)

            output = buf.getvalue()

        # Check the output is not None
        self.assertIsNotNone(output, msg="Output cannot be None")

        # Check the output is empty
        self.assertEqual(output, '', msg="Output is not empty")

    def test_only_invalid_chars_result_in_empty_output(self):
        print(inspect.stack()[0][3])

        fake_file_path="/fake/file/path"
        lines = ["%.,", ",,", "   ", " \" "]  # the last empty line ensures that we have a final '\n'
        fake_file = io.StringIO('\n'.join(lines))

        # Execute main and be sure you capture the output but use mocking to fake a file read by the program
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('word_index.open', return_value=fake_file, create=True):
                wi_main(fake_file_path)

            output = buf.getvalue()

        # Check the output is not None
        self.assertIsNotNone(output, msg="Output cannot be None")

        # Check the output is empty
        self.assertEqual(output, '', msg="Output is not empty")

    def test_invalid_chars_are_removed(self):
        print(inspect.stack()[0][3])

        fake_file_path="/fake/file/path"
        lines = ["%.,", ",,", "alpha", " \" "]  # the last empty line ensures that we have a final '\n'
        fake_file = io.StringIO('\n'.join(lines))

        # Execute main and be sure you capture the output but use mocking to fake a file read by the program
        with io.StringIO() as buf, redirect_stdout(buf):
            with patch('word_index.open', return_value=fake_file, create=True):
                wi_main(fake_file_path)

            output = buf.getvalue()

        output_lines = list(filter(None, output.split('\n'))) # Split over '\n' but remove empty strings
        expected_n_lines = 1
        expected_output_string = "alpha - 1\n"

        self.assertEqual(expected_n_lines, len(output_lines),
                         msg="Output has wrong number of lines")
        self.assertEqual(expected_output_string, output, msg="Wrong output")

        # Check the output is empty


if __name__ == '__main__':
    unittest.main()


