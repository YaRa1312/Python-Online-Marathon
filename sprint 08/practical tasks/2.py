# Python Online Marathon
# sprint 08
# practical tasks

########################################## 2 ##########################################
################################ PASSED ################################
import unittest


def divide(num1, num2):
    return float(num1/num2)


class GoodInstanceInteger:

    random_integer_num = 5


class GoodInstanceFloat:

    random_float_num = 5.0


class DivideTest(unittest.TestCase):
    
    def test_type_integer(self):
        checked_object = GoodInstanceInteger()
        msg = "given object is not instance of class GoodInstanceInteger"
        self.assertIsInstance(checked_object, GoodInstanceInteger, msg)
        
    def test_type_float(self):
        checked_object = GoodInstanceFloat()
        msg = "given object is not instance of class GoodInstanceFloat"
        self.assertIsInstance(checked_object, GoodInstanceFloat, msg)
    
    def test_exception_zero_division(self):
        for positive_num in range(1, (10**5)):
            self.assertRaises(Exception, divide, positive_num, 0)
        for negative_num in range(-(10**5), -1):
            self.assertRaises(Exception, divide, negative_num, 0)

    def test_sth(self):
        self.assertAlmostEqual(divide(1, 6), 0.16666666666666666, 17)

######################### tests #########################

# count_tests >= 3

# failures

# errors

# skipped

# expectedFailures

# expectRaisesError
