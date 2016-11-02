import unittest
import logging

def warn_if_not_implemented(func):
    def wrapper(*args, **kwargs):
        try:
            func(*args, **kwargs)
        except Exception as e:
            if e.args[0] == 'Not implemented':
                logging.warning('%s is not implemented' % func.__name__[len('test_'):])
                return
            raise

    return wrapper


class TestTasks(unittest.TestCase):

    @warn_if_not_implemented
    def test_xor(self):
        from xor import xor
        self.assertEqual(xor(False, False), True)
        self.assertEqual(xor(False, True), False)
        self.assertEqual(xor(True, False), False)
        self.assertEqual(xor(True, True), True)

    @warn_if_not_implemented
    def test_compare(self):
        from compare import compare
        self.assertEqual(compare(2, 1), 'a is greater then b')
        self.assertEqual(compare(1, 2), 'a is less than b')
        self.assertEqual(compare(1, 1), 'a is equal to b')


if __name__ == '__main__':
    unittest.main()
