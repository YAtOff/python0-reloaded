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
        self.assertEqual(xor(False, False), False)
        self.assertEqual(xor(False, True), True)
        self.assertEqual(xor(True, False), True)
        self.assertEqual(xor(True, True), False)

if __name__ == '__main__':
    unittest.main()
