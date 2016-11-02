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
    def test_number_to_text(self):
        from number_to_text import number_to_text
        self.assertEqual(number_to_text(0), 'zero')
        self.assertEqual(number_to_text(1), 'one')
        self.assertEqual(number_to_text(2), 'two')
        self.assertEqual(number_to_text(3), 'three')
        self.assertEqual(number_to_text(4), 'four')
        self.assertEqual(number_to_text(5), 'five')
        self.assertEqual(number_to_text(6), 'six')
        self.assertEqual(number_to_text(7), 'seven')
        self.assertEqual(number_to_text(8), 'eight')
        self.assertEqual(number_to_text(9), 'nine')

    @warn_if_not_implemented
    def test_product_sign(self):
        from product_sign import product_sign
        self.assertEqual(product_sign(1, 1), '+')
        self.assertEqual(product_sign(1, -1), '-')
        self.assertEqual(product_sign(-1, -1), '+')


if __name__ == '__main__':
    unittest.main()
