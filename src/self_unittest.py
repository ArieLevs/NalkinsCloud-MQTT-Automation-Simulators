import unittest
from src.functions import *

valid_topic = 'some/valid/topic'
invalid_topic = 'invalid/topic'
empty_topic = ''


class PyBumpTest(unittest.TestCase):

    def setUp(self):
        pass

    def test_is_valid_topic(self):
        self.assertTrue(is_valid_topic(valid_topic))
        self.assertFalse(is_valid_topic(invalid_topic))
        self.assertFalse(is_valid_topic(empty_topic))


if __name__ == '__main__':
    unittest.main()
