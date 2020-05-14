import unittest
import tempfile
import io
import inspect
import os

# See: https://stackoverflow.com/questions/1218933/can-i-redirect-the-stdout-in-python-into-some-sort-of-string-buffer
from contextlib import redirect_stdout

from unittest.mock import patch, mock_open

# Import the program under test.
from word_index import main as wi_main
# Q: Exercise at home: Try to move the import INSIDE the test to see whether global variables
#       are automatically re-initialized.
# Q: Exercise at home: Implement a test case that runs the program under test using as subprocess
#       and check whether global variables are re-initialized



# Import the monolithic main used as oracle
from monolithic_word_index import main as oracle_main

# https://simpleit.rocks/python/test-files-creating-a-temporal-directory-in-python-unittests/

# This will not work because main expects a str, bytes or os.PathLike object, not _io.TextIOWrapper
# with tempfile.TemporaryFile('w') as tmp_file:
        #     print('created temporary file', tmp_file)
        #     # Fill the temp file
        #     tmp_file.writelines(["foo", "bar"])
class TestWordIndexUsingTempFiles(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.TemporaryDirectory()

    def tearDown(self):
        # Q: Will the directory be removed?
        print("Temp Dir Exists ? ", os.path.exists(self.test_dir.name))
        self.test_dir.cleanup()
        print("Temp Dir Exists ?", os.path.exists(self.test_dir.name))


    def test_program_with_few_lines(self):
        # Print name of this test
        print(inspect.stack()[0][3])

        temp_file = os.path.join(self.test_dir.name, "input.txt")

        expected_output = '\n'.join(["bar - 1", "foo - 1",""])

        with open(temp_file, 'w') as f:
            f.writelines('\n'.join(["foo", "bar"]))

        with io.StringIO() as buf, redirect_stdout(buf):
            # Invoke main passing the temp file
            wi_main(temp_file)
            output = buf.getvalue()

        # Make the assertions
        self.assertEqual(output, expected_output, msg="Output does not match")

if __name__ == '__main__':
    unittest.main()


