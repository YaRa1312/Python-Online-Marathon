# Python Online Marathon
# sprint 04
# practical tasks

########################################## 1 ##########################################
################################ PASSED ################################
class Employee:
    @classmethod
    def from_string(cls, param):
        firstname = param.split("-")[0]
        lastname = param.split("-")[1]
        salary = param.split("-")[2]
        return Employee(firstname, lastname, int(salary))
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary

########################################## 2 ##########################################
################################ PASSED ################################
class Pizza:
    total_orders = 1
    def __init__(self, ingredients: list):
        self.order_number = Pizza.total_orders
        Pizza.total_orders += 1
        self.ingredients = ingredients
    @classmethod
    def hawaiian(cls):
        ingredients = ['ham', 'pineapple']
        return Pizza(ingredients)
    @classmethod
    def meat_festival(cls):
        ingredients = ['beef', 'meatball', 'bacon']
        return Pizza(ingredients)
    @classmethod
    def garden_feast(cls):
        ingredients = ['spinach', 'olives', 'mushroom']
        return Pizza(ingredients)

########################################## 3 ##########################################
################################ PASSED ################################
class Employee:
    def __init__(self, full_name, **kwargs):
        self.full_name = full_name
        self.name = full_name.split(" ")[0]
        self.lastname = full_name.split(" ")[1]
        self.__dict__.update(kwargs)

########################################## 4 ##########################################

########################################## 5 ##########################################
