# Python Online Marathon
# sprint 05
# practical tasks

########################################## 1 ##########################################
################################ PASSED ################################
def check_odd_even(number):
    try:
        if number % 2 == 0:
            return("Entered number is even")
        elif number % 2 == 1:
            return("Entered number is odd")
    except TypeError:
        return("You entered not a number.")

########################################## 2 ##########################################
################################ PASSED ################################
def divide(numerator, denominator):
    try:
        result = numerator/denominator
        return(f"Result is {result}")
    except ZeroDivisionError:
        return(f"Oops, {numerator}/0, division by zero is error!!!")
    except TypeError:
        return("Value Error! You did not enter a number!")

########################################## 3 ##########################################
################################ PASSED ################################
class ToSmallNumberGroupError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)

def check_number_group(number):
    try:
        if number > 10:
            return(f"Number of your group {number} is valid")
        elif number < 10:
            raise ToSmallNumberGroupError("Number of your group can't be less than 10")
    except ToSmallNumberGroupError as e:
        msg = "We obtain error:" + e.data
        return msg
    except TypeError:
        try:
            res = int(number)
            if res > 10:
                return(f"Number of your group {res} is valid")
        except ValueError:
            return("You entered incorrect data. Please try again.")

########################################## 4 ##########################################
################################ PASSED ################################
def day_of_week(day):
    try:
        if day == 1:
            return("Monday")
        elif day == 2:
            return("Tuesday")
        elif day == 3:
            return("Wednesday")
        elif day == 4:
            return("Thursday")
        elif day == 5:
            return("Friday")
        elif day == 6:
            return("Saturday")
        elif day == 7:
            return("Sunday")
        elif day < 1 or day > 7:
            return("There is no such day of the week! Please try again.")
    except TypeError:
        try:
            res = int(day)
            if res == 1:
                return("Monday")
            elif res == 2:
                return("Tuesday")
            elif res == 3:
                return("Wednesday")
            elif res == 4:
                return("Thursday")
            elif res == 5:
                return("Friday")
            elif res == 6:
                return("Saturday")
            elif res == 7:
                return("Sunday")
            elif res < 1 or res > 7:
                return("There is no such day of the week! Please try again.")
        except ValueError:
            return("You did not enter a number! Please try again.")

########################################## 5 ##########################################
################################ PASSED ################################
import cmath
def solve_quadric_equation(a, b, c):
    try:
        discriminant = (b**2)-(4*a*c)
        x1 = (-b-cmath.sqrt(discriminant))/(2*a)
        x2 = (-b+cmath.sqrt(discriminant))/(2*a)
        return(f"The solution are x1={x1} and x2={x2}")
    except ZeroDivisionError:
        return("Zero Division Error")
    except TypeError:
        return("Could not convert string to float")

########################################## 6 ##########################################
################################ PASSED ################################
import re
def valid_email(email):
    try:
        pattern_for_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        if re.fullmatch(pattern_for_email, email):
            return ("Email is valid")
        else:
            return ("Email is not valid")
    except TypeError:
        return ("Email is not valid")

########################################## 7 ##########################################
################################ PASSED ################################
class MyError(Exception):
    def __init__(self, data):
        self.data = data
    def __str__(self):
        return repr(self.data)
    
def check_positive(number):
    try:
        if number > 0:
            res_number = float(number)
            return(f"You input positive number: {res_number}")
        elif number < 0:
            res_number = float(number)
            raise MyError(f"You input negative number: {res_number}. Try again.")
    except MyError:
        return(f"You input negative number: {res_number}. Try again.")
    except TypeError:
        try:
            num = int(number)
            if num > 0:
                res_num = float(num)
                return(f"You input positive number: {res_num}")
            elif num < 0:
                res_num = float(num)
                raise MyError(f"You input negative number: {res_num}. Try again.")
        except MyError:
            return(f"You input negative number: {res_num}. Try again.")
        except ValueError:
            return(f"Error type: ValueError!")
            