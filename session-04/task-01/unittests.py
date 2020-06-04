import unittest
import sys
import io
import inspect

# See: https://stackoverflow.com/questions/1218933/can-i-redirect-the-stdout-in-python-into-some-sort-of-string-buffer
from contextlib import redirect_stdout

from unittest.mock import patch, mock_open

# Import the program under test.
from word_index import main as wi_main

# Import the monolithic main used as oracle
from monolithic_word_index import main as oracle_main

class TestWordIndex(unittest.TestCase):

    def test_program_with_few_lines(self):
        # Print name of this test
        print(self.__class__.__name__ + " - " +inspect.stack()[0][3])

        fake_file_path="/fake/file/path"

        lines= ["foo", "bar", ""] # the last empty line ensures that we have a final '\n'

        fake_file = io.StringIO('\n'.join(lines))

        # Create the expectation using the oracle_main
        with patch('monolithic_word_index.open', return_value=fake_file, create=True):
            expected_output = oracle_main(fake_file_path)

        # Create the actual output using the wi_main
        fake_file = io.StringIO('\n'.join(lines))
        with io.StringIO() as buf, redirect_stdout(buf):

            with patch('word_index.open', return_value=fake_file, create=True):
                wi_main(fake_file_path)

            output = buf.getvalue()

        # Assert that the two output matches
        self.assertEqual(output, expected_output, msg="Output does not match")

    def test_program_with_many_lines(self):
        # Print name of this test
        print(self.__class__.__name__ + " - " +inspect.stack()[0][3])

        fake_file_path="/fake/file/path"

        lines = []
        # This should appear on output
        for i in range(1, 100): # 99 occurrences - not filtered
            lines.append("foo")

        # This should not appear on output
        for i in range(1, 102): # 101 occurrences - filtered
            lines.append("bar")

        lines.append("")

        fake_file = io.StringIO('\n'.join(lines))

        # Create the expectation using the oracle_main
        with patch('monolithic_word_index.open', return_value=fake_file, create=True):
            expected_output = oracle_main(fake_file_path)

        # Create the actual output using the wi_main
        fake_file = io.StringIO('\n'.join(lines))
        with io.StringIO() as buf, redirect_stdout(buf):

            with patch('word_index.open', return_value=fake_file, create=True):
                wi_main(fake_file_path)

            output = buf.getvalue()

        # Assert that the two output matches
        self.assertEqual(output, expected_output, msg="Output does not match")

    def test_program_with_sample_file(self):
        # Print name of this test
        print(self.__class__.__name__ + " - " +inspect.stack()[0][3])

        real_file_path="../test-data/sample.txt"

        expected_output = oracle_main(real_file_path)

        with io.StringIO() as buf, redirect_stdout(buf):
            wi_main(real_file_path)
            output = buf.getvalue()

        # Assert that the two output matches
        self.assertEqual(output, expected_output, msg="Output does not match")

    def test_program_with_long_file(self):
        # Print name of this test
        print(self.__class__.__name__ + " - " +inspect.stack()[0][3])

        real_file_path="../test-data/long.txt"

        expected_output = oracle_main(real_file_path)

        with io.StringIO() as buf, redirect_stdout(buf):
            wi_main(real_file_path)
            output = buf.getvalue()

        # Assert that the two output matches
        self.assertEqual(output, expected_output, msg="Output does not match")

    def test_output_with_empty_file(self):
        print(self.__class__.__name__ + " - " +inspect.stack()[0][3])

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
        print(self.__class__.__name__ + " - " +inspect.stack()[0][3])

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
        print(self.__class__.__name__ + " - " +inspect.stack()[0][3])

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
#

if __name__ == '__main__':
    unittest.main()


