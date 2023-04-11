import unittest
from decimal2binario import decimal2binario
from binario2decimal import binario2decimal


class TestNumeracion(unittest.TestCase):
#Tests de binario a decimal
    def test_binario2decimal_1(self):
        self.assertEqual(binario2decimal('01011100'), 92)
    def test_binario2decimal_2(self):
        self.assertEqual(binario2decimal('1100001'), 97)


#Tests de decimal a binario
    def test_decimal2binario_1(self):
        self.assertEqual(decimal2binario(97), '1100001')
    def test_decimal2binario_2(self):
        self.assertEqual(decimal2binario(92), '1011100')


if __name__ == '__main__':
    unittest.main()
