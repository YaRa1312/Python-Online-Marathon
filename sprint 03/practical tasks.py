# Python Online Marathon
# sprint 03
# practical tasks

########################################## 1 ##########################################
################################ PASSED ################################
def outer(name):
    def inner():
        print(f'Hello, {name}!')
    return inner

########################################## 2 ##########################################
################################ PASSED ################################
def create(arg):
    return lambda x: x == arg

########################################## 3 ##########################################
################################ PASSED ###############################
import re
from collections import Counter
def create_account(user_name, password, secret_words):
    pattern = "^.*(?=.{6,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[!@#№$;%^:*_-]).*$"
    if not (re.fullmatch(pattern, password)):
        print('Raises ValueError')
    def check(password_, secret_words_):
        if password_ == password:
            if len(secret_words_) == len(secret_words):
                difference = list((Counter(secret_words)-Counter(secret_words_)).elements())
                if len(difference) == 1 or len(difference) == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False
    return check

tom = create_account("Tom", "Qwerty1_", ["1", "word"])  
check1 = tom("Qwerty1_",  ["1", "word"]) 
check2 = tom("Qwerty1_",  ["word"]) 
check3 = tom("Qwerty1_",  ["word", "2"]) 
check4 = tom("Qwerty1!",  ["word", "12"]) 

########################################## 4 ##########################################
############################### PASSED ###############################
def divisor(num):
    i = 1
    while i <= num:
        if not num % i:
            yield i
        i += 1
    while num and i:
        yield None

########################################## 5 ##########################################
############################### PASSED ###############################
def logger(func):
    f_name = func.__name__
    arg_names = func.__code__.co_varnames[:func.__code__.co_argcount]
    def wrapper(*args, **kwargs):
        result_piece = f'Executing of function {f_name} with arguments'
        args_ = ''
        kwargs_ = ''
        for arg in args:
            args_ = args_ + " " + str(arg) + ","
        for kwarg in kwargs:
            kwargs_ = kwargs_ + " " + str(kwargs[kwarg]) + ","
        func_action = func(*args, **kwargs)
        print((result_piece + args_ + kwargs_)[:-1] + "...")
        return func_action
    return wrapper

@logger
def sum(a,b):
    return a+b
    
@logger
def print_arg(arg):
    print(arg)

@logger
def concat(*args, **kwargs):
    result = ""
    for arg in args:
        result += str(arg)
    for kwarg in kwargs.values():
        result += str(kwarg)
    return result
    
########################################## 6 ##########################################
############################### PASSED ###############################
import random
def randomWord(word_list):
    if not word_list:
        yield None
    else:
        while True:
            word_list_copy = list(word_list)
            random.shuffle(word_list_copy)
            for el in word_list_copy:
                yield el
