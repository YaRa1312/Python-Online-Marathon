# Python Online Marathon
# sprint 08
# practical tasks

########################################## 1 ##########################################
################################ PASSED ################################
import unittest


class Product:

    def __init__(self, name, price, count):
        self.name = name
        self.price = price
        self.count = count
       

class Cart:

    def __init__(self, products):
        self.products = products

    def get_total_price(self):
        result = 0
        for i in self.products:
            if i.count > 20:
                result += (i.price - (i.price*0.5)) * i.count
            elif i.count >= 20:
                result += (i.price - (i.price*0.3)) * i.count
            elif i.count >= 10 and i.count < 20:
                result += (i.price - (i.price*0.2)) * i.count
            elif i.count >= 7 and i.count < 10:
                result += (i.price - (i.price*0.1)) * i.count
            elif i.count >= 5 and i.count < 7:
                result += (i.price - (i.price*0.05)) * i.count
            elif i.count < 5:
                result += i.price * i.count
        return result


test_data = (Product('p1',10,4),
Product('p2',100,5),
Product('p3',200,6),
Product('p4',300,7),
Product('p5',400,9),
Product('p6',500,10),
Product('p7',1000,20))


class CartTest(unittest.TestCase):

    def test_type_of_elem(self):
        for i in test_data:
            self.assertEqual(type(i.name), str)
            self.assertEqual(type(i.price), int)
            self.assertEqual(type(i.count), int)

######################### tests #########################

# print(count_tests > 0)

# print(failures)

# print(errors)

# print(assertEqual)

# products = (Product('p1',10,4),
# Product('p2',100,5),
# Product('p3',200,6),
# Product('p4',300,7),
# Product('p5',400,9),
# Product('p6',500,10),
# Product('p7',1000,20))
# cart = Cart(products)
# print(cart.get_total_price())
