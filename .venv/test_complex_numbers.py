import unittest
import complex_numbers as cn
import math
class TestComplexNumbers(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(cn.suma((1, 2), (3, 4)), (4, 6))
        self.assertEqual(cn.suma((-1, -2), (1, 2)), (0, 0))

    def test_resta(self):
        self.assertEqual(cn.resta((5, 7), (3, 4)), (2, 3))
        self.assertEqual(cn.resta((1, 2), (1, 2)), (0, 0))

    def test_producto(self):
        self.assertEqual(cn.producto((1, 2), (3, 4)), (-5, 10))
        self.assertEqual(cn.producto((0, 1), (1, 0)), (0, 1))

    def test_division(self):
        self.assertEqual(cn.division((1, 2), (3, 4)), (0.44, 0.08))
        self.assertEqual(cn.division((1, 1), (1, -1)), (0.0, 1.0))

    def test_modulo(self):
        self.assertAlmostEqual(cn.modulo((3, 4)), 5)
        self.assertAlmostEqual(cn.modulo((1, 1)), math.sqrt(2))

    def test_conjugado(self):
        self.assertEqual(cn.conjugado((1, 2)), (1, -2))
        self.assertEqual(cn.conjugado((-1, -2)), (-1, 2))

    def test_cartesiano_a_polar(self):
        self.assertEqual(cn.cartesiano_a_polar((0, 1)), (1, math.pi / 2))
        self.assertEqual(cn.cartesiano_a_polar((1, 0)), (1, 0))

    def test_polar_a_cartesiano(self):
        self.assertAlmostEqual(cn.polar_a_cartesiano((1, math.pi / 2))[0], 0, places=10)
        self.assertAlmostEqual(cn.polar_a_cartesiano((1, math.pi / 2))[1], 1, places=10)
        self.assertAlmostEqual(cn.polar_a_cartesiano((1, 0))[0], 1, places=10)
        self.assertAlmostEqual(cn.polar_a_cartesiano((1, 0))[1], 0, places=10)

    def test_fase(self):
        self.assertEqual(cn.fase((0, 1)), math.pi / 2)
        self.assertEqual(cn.fase((1, 0)), 0)

if __name__ == '__main__':
    unittest.main()