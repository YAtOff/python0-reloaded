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
    def test_max2(self):
        from max2 import max2
        self.assertEqual(max2(1, 2), 2)

    @warn_if_not_implemented
    def test_ph_to_text(self):
        from ph import ph_to_text
        self.assertEqual(ph_to_text(2), 'strong acid')
        self.assertEqual(ph_to_text(5), 'weak acid')
        self.assertEqual(ph_to_text(7), 'neutral')
        self.assertEqual(ph_to_text(8), 'weak base')
        self.assertEqual(ph_to_text(10), 'strong base')


if __name__ == '__main__':
    unittest.main()
