# Example taken from: https://github.com/otrabalhador/python-testing-by-examples/blob/master/docs/en/mocking/examples/reading-writing-on-files.md
# Additional info: https://stackoverflow.com/questions/16134281/python-mocking-a-function-from-an-imported-module
# https://docs.python.org/3/library/unittest.mock.html#where-to-patch

import unittest
from unittest.mock import patch, mock_open

# import file_reader
from file_reader import count_lines


class TestReadFiles(unittest.TestCase):
    def test_count_lines(self):
        file_content_mock = """Hello World!!
Hello World is in a file.
A mocked file.
He is not real.
But he think he is.
He doesn't know he is mocked"""
        fake_file_path = 'file/path/mock'

        # Note that we are patching the open inside file_reader
        # with patch('file_reader.open',
        with patch('file_reader.open',
                   new=mock_open(read_data=file_content_mock)) as _file:
            # actual = file_reader.count_lines(fake_file_path)
            actual = count_lines(fake_file_path)
            _file.assert_called_once_with(fake_file_path, 'r')

        expected = len(file_content_mock.split('\n'))
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()
