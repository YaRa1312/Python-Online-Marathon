# Python Online Marathon
# sprint 08
# practical tasks

########################################## 3 ##########################################
# Write the function quadratic_equation with arguments a, b ,c that solution to quadratic equation without a complex solution.

# Write unit tests for this function with QuadraticEquationTest class

# Minimum 3 tests: discriminant < 0, discriminant > 0, discriminant = 0

################################ PASSED ################################
import unittest
import math


def quadratic_equation(a, b, c):
    discriminant = (b**2)-(4*a*c)
    if discriminant < 0:
        return(None)
    x1 = (-b+math.sqrt(discriminant))/(2*a)
    x2 = (-b-math.sqrt(discriminant))/(2*a)
    if x1 == x2:
        return x1
    else:
        return(x1, x2)


test_data_with_positive_discriminant = [2, 1, -1]
test_data_with_negative_discriminant = [-2, 1, -1]


class QuadraticEquationTest(unittest.TestCase):
    
    def test_positive_discriminant(self):
        for el in test_data_with_positive_discriminant:
            discriminant = ((el[1]) ** 2) - (4 * el[0] * el[2])
        expected = discriminant > 0
        self.assertTrue(expected, msg="Discriminant is NOT greater than 0")

    def test_negative_discriminant(self):
        for el in test_data_with_negative_discriminant:
            discriminant = ((el[1]) ** 2) - (4 * el[0] * el[2])
        expected = discriminant < 0
        self.assertTrue(expected, msg="Discriminant is NOT less than 0")

    def test_zero_discriminant(self):
        self.assertRaises(Exception, quadratic_equation, 0, 0, 0)
        # pass

######################### tests #########################

# print(quadratic_equation(2, 1, -1))

# print(quadratic_equation(1, -4, 4))

# print(quadratic_equation(4, 1, 2))

# try:
#     quadratic_equation(0, 0, 0)
# except ValueError:
#     print('error')

# print(count_tests > 3)

# print(failures)

# print(errors)

# print(cheater)

# print(skipped)

# print(expectedFailures)
