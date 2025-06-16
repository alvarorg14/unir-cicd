import unittest
from unittest.mock import patch
import pytest
import math


from app.calc import Calculator, InvalidPermissions


def mocked_validation(*args, **kwargs):
    return True

def mocked_validation_fail(*args, **kwargs):
    return False


@pytest.mark.unit
class TestCalculate(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    # ADD
    def test_add_method_returns_correct_result(self):
        self.assertEqual(4, self.calc.add(2, 2))
        self.assertEqual(0, self.calc.add(2, -2))
        self.assertEqual(-4, self.calc.add(-2, -2))
        self.assertEqual(2, self.calc.add(1, 0))

    def test_add_method_fails_with_invalid_parameters(self):
        self.assertRaises(TypeError, self.calc.add, "2", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "2")
        self.assertRaises(TypeError, self.calc.add, "a", 2)
        self.assertRaises(TypeError, self.calc.add, 2, "a")
        self.assertRaises(TypeError, self.calc.add, None, 2)
        self.assertRaises(TypeError, self.calc.add, 2, None)
        self.assertRaises(TypeError, self.calc.add, object(), 2)
        self.assertRaises(TypeError, self.calc.add, 2, object())

    # SUBSTRACT
    def test_substract_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.substract(2, 2))
        self.assertEqual(4, self.calc.substract(2, -2))
        self.assertEqual(0, self.calc.substract(-2, -2))

    def test_substract_method_fails_with_invalid_parameters(self):
        self.assertRaises(TypeError, self.calc.substract, "2", 2)
        self.assertRaises(TypeError, self.calc.substract, 2, "2")
        self.assertRaises(TypeError, self.calc.substract, "2", "2")
        self.assertRaises(TypeError, self.calc.substract, None, 2)
        self.assertRaises(TypeError, self.calc.substract, 2, None)
        self.assertRaises(TypeError, self.calc.substract, object(), 2)
        self.assertRaises(TypeError, self.calc.substract, 2, object())

    # MULTIPLY
    @patch('app.util.validate_permissions', side_effect=mocked_validation)
    def test_multiply_method_returns_correct_result(self, _):
        self.assertEqual(4, self.calc.multiply(2, 2))
        self.assertEqual(0, self.calc.multiply(1, 0))
        self.assertEqual(0, self.calc.multiply(-1, 0))
        self.assertEqual(-2, self.calc.multiply(-1, 2))
        self.assertEqual(4, self.calc.multiply(-2, -2))

    @patch('app.util.validate_permissions', side_effect=mocked_validation_fail)
    def test_multiply_method_fails_with_invalid_permissions(self, _):
        self.assertRaises(InvalidPermissions, self.calc.multiply, 2, 2)

    def test_multiply_method_fails_with_invalid_parameters(self):
        with patch('app.util.validate_permissions', return_value=True):
            self.assertRaises(TypeError, self.calc.multiply, "2", 2)
            self.assertRaises(TypeError, self.calc.multiply, 2, "2")
            self.assertRaises(TypeError, self.calc.multiply, "a", 2)
            self.assertRaises(TypeError, self.calc.multiply, 2, "a")
            self.assertRaises(TypeError, self.calc.multiply, None, 2)
            self.assertRaises(TypeError, self.calc.multiply, 2, None)
            self.assertRaises(TypeError, self.calc.multiply, object(), 2)
            self.assertRaises(TypeError, self.calc.multiply, 2, object())

    # DIVIDE
    def test_divide_method_returns_correct_result(self):
        self.assertEqual(1, self.calc.divide(2, 2))
        self.assertEqual(1.5, self.calc.divide(3, 2))
        self.assertEqual(0, self.calc.divide(0, 2))
        self.assertEqual(1, self.calc.divide(-2, -2))
    
    def test_divide_method_fails_with_division_by_zero(self):
        self.assertRaises(TypeError, self.calc.divide, 2, 0)
        self.assertRaises(TypeError, self.calc.divide, 2, -0)
        self.assertRaises(TypeError, self.calc.divide, 0, 0)

    def test_divide_method_fails_with_invalid_parameters(self):
        self.assertRaises(TypeError, self.calc.divide, "2", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "2")
        self.assertRaises(TypeError, self.calc.divide, "a", 2)
        self.assertRaises(TypeError, self.calc.divide, 2, "a")
        self.assertRaises(TypeError, self.calc.divide, None, 2)
        self.assertRaises(TypeError, self.calc.divide, 2, None)
        self.assertRaises(TypeError, self.calc.divide, object(), 2)
        self.assertRaises(TypeError, self.calc.divide, 2, object())

    # POWER
    def test_power_method_returns_correct_result(self):
        self.assertEqual(8, self.calc.power(2, 3))
        self.assertEqual(1, self.calc.power(5, 0))
        self.assertEqual(0.25, self.calc.power(2, -2))
        self.assertEqual(0.25, self.calc.power(-2, -2))

    def test_power_method_fails_with_invalid_parameters(self):
        self.assertRaises(TypeError, self.calc.power, "2", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "2")
        self.assertRaises(TypeError, self.calc.power, "a", 2)
        self.assertRaises(TypeError, self.calc.power, 2, "a")
        self.assertRaises(TypeError, self.calc.power, None, 2)
        self.assertRaises(TypeError, self.calc.power, 2, None)
        self.assertRaises(TypeError, self.calc.power, object(), 2)
        self.assertRaises(TypeError, self.calc.power, 2, object())

    # SQRT
    def test_sqrt_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.sqrt(0))
        self.assertEqual(3, self.calc.sqrt(9))
        self.assertAlmostEqual(math.sqrt(2), self.calc.sqrt(2), places=6)

    def test_sqrt_method_fails_with_negative_number(self):
        self.assertRaises(TypeError, self.calc.sqrt, -4)

    def test_sqrt_method_fails_with_invalid_parameters(self):
        self.assertRaises(TypeError, self.calc.sqrt, "2")
        self.assertRaises(TypeError, self.calc.sqrt, "a")
        self.assertRaises(TypeError, self.calc.sqrt, None)
        self.assertRaises(TypeError, self.calc.sqrt, object())

    # LOG10
    def test_log10_method_returns_correct_result(self):
        self.assertEqual(0, self.calc.log10(1))
        self.assertEqual(2, self.calc.log10(100))
        self.assertAlmostEqual(math.log10(2), self.calc.log10(2), places=6)

    def test_log10_method_fails_with_non_positive_number(self):
        self.assertRaises(TypeError, self.calc.log10, 0)
        self.assertRaises(TypeError, self.calc.log10, -10)

    def test_log10_method_fails_with_invalid_parameters(self):
        self.assertRaises(TypeError, self.calc.log10, "2")
        self.assertRaises(TypeError, self.calc.log10, "a")
        self.assertRaises(TypeError, self.calc.log10, None)
        self.assertRaises(TypeError, self.calc.log10, object())


if __name__ == "__main__":  # pragma: no cover
    unittest.main()
