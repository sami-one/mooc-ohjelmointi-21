import unittest
from unittest.mock import patch

from tmc import points, reflect
from tmc.utils import load, load_module, reload_module, get_stdout, check_source

@points('1.pelin_palautus')
class VarastosaldoTest(unittest.TestCase):
    def test_1_pygame(self):
        pass

if __name__ == '__main__':
    unittest.main()
