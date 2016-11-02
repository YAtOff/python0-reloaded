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
    def test_max3(self):
        from max3 import max3
        self.assertEqual(max3(1, 2, 3), 3)

    @warn_if_not_implemented
    def test_min2(self):
        from min2 import min2
        self.assertEqual(min2(1, 2), 1)

    @warn_if_not_implemented
    def test_min3(self):
        from min3 import min3
        self.assertEqual(min3(1, 2, 3), 1)

    @warn_if_not_implemented
    def test_even(self):
        from even import is_even
        self.assertEqual(is_even(1), False)
        self.assertEqual(is_even(2), True)

    @warn_if_not_implemented
    def test_odd(self):
        from odd import is_odd
        self.assertEqual(is_odd(1), True)
        self.assertEqual(is_odd(2), False)

    @warn_if_not_implemented
    def test_abs(self):
        from abs import abs
        self.assertEqual(abs(1), 1)
        self.assertEqual(abs(-1), 1)


if __name__ == '__main__':
    unittest.main()
