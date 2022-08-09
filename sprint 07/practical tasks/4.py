# Python Online Marathon
# sprint 07
# practical tasks

########################################## 4 ##########################################
################################ PASSED ################################
class Washing:
    def wash(self):
        print("Washing...")
 
class Rinsing:
    def rinse(self):
        print("Rinsing...")
 
class Spinning:
    def spin(self):
        print("Spinning...")
 
class WashingMachine:
    def __init__(self):
        self.washing = Washing()
        self.rinsing = Rinsing()
        self.spinning = Spinning()
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()
        
    def startWashing(self):
        self.washing.wash()
        self.rinsing.rinse()
        self.spinning.spin()

######################### tests #########################
# washingMachine = WashingMachine()

# washingMachine.startWashing()
