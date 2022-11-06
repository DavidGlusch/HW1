import unittest
from Task_1 import ContextManager


class TestContexManager(unittest.TestCase):
    test_instance_a_plus = ContextManager('test_new_file.txt', 'a+')
    test_instance_w_plus = ContextManager('test_new_file.txt', 'w+')

    def test_read_file(self):
        with self.test_instance_a_plus as f:
            f.read()

    def test_write_file(self):
        with self.test_instance_w_plus as f:
            f.write('asd')
            f.write('dsa')
            f.seek(0)
            test = f.read()
            self.assertEqual(test, 'asddsa')
