# Python Online Marathon
# sprint 07
# practical tasks

########################################## 2 ##########################################
################################ PASSED ################################
class Goods:
    def __init__(self, price, discount_strategy = None):
        self.price = price
        self.discount_strategy = discount_strategy
    def price_after_discount(self):
        if self.discount_strategy:
            discount = self.discount_strategy(self)
        else:
            discount = 0
        result = self.price - discount
        return result
    def __repr__(self):
        return(f"Price: {self.price}, price after discount: {self.price_after_discount()}")

def on_sale_discount(order):
    result = order.price / 2
    return result

def twenty_percent_discount(order):
    result = order.price * 0.20
    return result

######################### tests #########################

# print(Goods(20000))

# print(Goods(20000, discount_strategy = twenty_percent_discount))

# print(Goods(20000, discount_strategy = on_sale_discount))
