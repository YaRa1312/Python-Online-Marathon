# Python Online Marathon
# sprint 08
# practical tasks

########################################## 2 ##########################################
################################ PASSED ################################
# Please, write the code with unit tests for the function "divide":
# minimum 3 tests
# must chek all flows
# all test must be pass
# no failures
# no skip

import unittest
from parameterized import parameterized


def divide(num1, num2):
    return float(num1/num2)


# class GoodInstanceInteger:
#     random_integer_num = 5

# class GoodInstanceFloat:
#     random_float_num = 5.0

class GoodInstances:
    pass

class DivideTest(unittest.TestCase):
    
    # @parameterized.expand([
    #     [5, GoodInstanceInteger, 'num is not integer'],
    #     [5.0, G]
    # ])
    # def test_parameterized(self, checked_object, class_name, message):
    #     pass
    # def test_parametrized(self):
    #     checked_object = GoodInstanceInteger()
    #     msg = "given object is not instance of class GoodInstance"
    #     self.assertIsInstance(checked_object, GoodInstanceInteger, msg)
    
    def test_exception_zero_division(self):
        for positive_num in range(1, (1000000**10.5)):
            self.assertRaises(Exception, divide, positive_num, 0)
        for negative_num in range(-(1000000**10.5), -1):
            self.assertRaises(Exception, divide, negative_num, 0)

######################### tests #########################

# count_tests >= 3

# failures

# errors

# skipped

# expectedFailures

# expectRaisesError
