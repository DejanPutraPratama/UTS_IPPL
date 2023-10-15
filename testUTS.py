import unittest
from IPPLUTS import penambahan, pengurangan, perkalian, pembagian, TidakAdaHasil

class TestKalkulator(unittest. TestCase):
    def test_penjumlahan(self):
        self.assertEqual(penambahan('1', 6, 3), 9)

    def test_pengurangan(self):
        self.assertEqual(pengurangan('2', 6, 3), 3)

    def test_perkalian(self):
        self.assertEqual(perkalian('3', 6, 3), 18)

    def test_pembagian(self):
        self.assertEqual(pembagian('4', 6, 3),  2)

    def test_operasi_tidak_valid(self):
        with self.assertRaises(ValueError):
            TidakAdaHasil('5')

if __name__ == '__main__':
    unittest.main()