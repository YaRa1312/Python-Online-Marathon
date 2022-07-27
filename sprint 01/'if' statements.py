# Python Online Marathon
# sprint 01
# 'if' statements
############################################################################################# theory

weather = 'raining'
print('Open your umbrella' if weather == 'raining' else 'Wear your cap')
# Open your umbrella
answer_go_out = input('Do you like to go out? ')
# Do you like to go out? Yes
print('Super!' if answer_go_out == 'Yes' else 'What a pity!')
# Super!
match status:
    case 400:
        print("Bad request")
    case 401:
        print("Unauthorized")
    case 403:
        print("Forbidden")
    case 404:
        print("Not found")
    case _:
        print("Other error")

        
# Traceback (most recent call last):
#   File "<pyshell#19>", line 1, in <module>
    # match status:
# NameError: name 'status' is not defined
match values:
    case 'load', link:
        load(link)
    case 'save', link, filename:
        save(link, filename)
    case 'save', link, *filenames:
        for filename in filenames:
            save(link, filename)
    case _:
        default(values)

        
# Traceback (most recent call last):
#   File "<pyshell#113>", line 1, in <module>
#     match values:
# NameError: name 'values' is not defined
match status:
    case 400:
        print("Bad request")
    case 401 | 403 as error:
        print(f"{error} is an authentication error")
    case 404:
        print("Not found")
    case _:
        print("Other error")

        
# Traceback (most recent call last):
#   File "<pyshell#30>", line 1, in <module>
    # match status:
# NameError: name 'status' is not defined
match item:
    case['evening', action]:
        print(f"You almost finished the day! Now {action}")
    case[time, action]:
        print(f"Good {time}! It is time to {action}!")
    case _:
        print("The time is invalid")

        
# Traceback (most recent call last):
#   File "<pyshell#38>", line 1, in <module>
    # match item:
# NameError: name 'item' is not defined. Did you mean: 'iter'?
match item:
    case{"time": "evening", 'action': action}:
        print(f"You almost finished the day! Now {action}")
    case{"time": time, "action": action}:
        print(f"Good {time}! It is time to {action}!")
    case _:
        print("The time is invalid")

        
# Traceback (most recent call last):
#   File "<pyshell#48>", line 1, in <module>
    # match item:
# NameError: name 'item' is not defined. Did you mean: 'iter'?
class MyClass:
    __match_args__=('time', 'action')
    def __init__(self, time, action):
        self.time = time
        self.action = action
    match item:
        case MyClass(time='evening', action='relax'):
            print(f'You almost finished the day!')
        case MyClass(time, action):
            print(f'Good {time}! It is time to {action}!')
        case _:
            print('The time is invalid')

            
# Traceback (most recent call last):
#   File "<pyshell#77>", line 1, in <module>
    # class MyClass:
#   File "<pyshell#77>", line 6, in MyClass
    # match item:
# NameError: name 'item' is not defined. Did you mean: 'iter'?
match item:
    case['evening', action] if action not in ['work', 'study']:
        print(f'You almost finished the day! Now {action}!')
    case['evening', _]:
        print('Come on, you deserve some rest!')
    case[time, action]:
        print(f'Good {time}! It is time to {action}!')

        
# Traceback (most recent call last):
#   File "<pyshell#85>", line 1, in <module>
    # match item:
# NameError: name 'item' is not defined. Did you mean: 'iter'?
a = []
if not a:
    print("The list is empty")

    
# The list is empty
keyword = 'lambda'
if keyword in ['and', 'del', 'from', 'lambda']:
    print("{} is a keyword".format(keyword))

    
# lambda is a keyword
y = 5
x = y
id(x)
# 2298645447024
id(y)
# 2298645447024
x is y
# True
y is not x
# False

############################################################################################# practise

# and
True and True and 1 and 12334
# 12334
True and [] and 1 and 12334
# []
{} and [] and 1 and 12334
# {}

# or
[] or 0 or {}
# {}
[] or 0 or {1}
# {1}
[] or 0 or [1] or True
# [1]

# not
# boolean values only #
not '1'
# False
not {''}
# False
not []
# True

not False and 1 or 10
# 1
(not False and 1) or 10
# 1
not False and (1 or 10)
# 1

