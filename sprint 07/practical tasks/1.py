# Python Online Marathon
# sprint 07
# practical tasks

########################################## 1 ##########################################
################################ PASSED ################################
from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def cook(self):
        pass
    
class FettuccineAlfredo(Product):
    name = "Fettuccine Alfredo"
    def cook(self):
        result = (f"Italian main course prepared: {self.name}")
        print(result)

class Tiramisu(Product):
    name = "Tiramisu"
    def cook(self):
        result = (f"Italian dessert prepared: {self.name}")
        print(result)
        
class DuckALOrange(Product):
    name = "Duck À L'Orange"
    def cook(self):
        result = (f"French main course prepared: {self.name}")
        print(result)

class CremeBrulee(Product):
    name = "Crème brûlée"
    def cook(self):
        result = (f"French dessert prepared: {self.name}")
        print(result)

class Factory(ABC):
    @abstractmethod
    def get_dish(self):
        pass

class ItalianDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return(FettuccineAlfredo())
        elif type_of_meal == "dessert":
            return(Tiramisu())

class FrenchDishesFactory(Factory):
    def get_dish(self, type_of_meal):
        if type_of_meal == "main":
            return(DuckALOrange())
        elif type_of_meal == "dessert":
            return(CremeBrulee())

class FactoryProducer:
    def get_factory(self, type_of_factory):
        if type_of_factory == "italian":
            return(ItalianDishesFactory())
        elif type_of_factory == "french":
            return(FrenchDishesFactory())

######################### tests #########################

# fp = FactoryProducer()
# fac = fp.get_factory("italian")
# main_dish = fac.get_dish("main")
# main_dish.cook()

# dessert = fac.get_dish("dessert")
# dessert.cook()

# fac1 = fp.get_factory("french")
# main_dish = fac1.get_dish("main")
# main_dish.cook()

# dessert = fac1.get_dish("dessert")
# dessert.cook()
