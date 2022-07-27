# Python Online Marathon
# sprint 01
# built-in types
############################################################################################# theory

x = 'foo'
y = x
print(x)
# foo
y += 'bar'
print(x)
# foo
x = 'iryna'
y = x
print(x)
# iryna
y += 'dmytro'
print(x)
# iryna
x = [1, 2, 3]
y = x
print(x)
# [1, 2, 3]
y += [3, 2, 1]
print(x)
# [1, 2, 3, 3, 2, 1]
iryna = 1109
print(id(iryna))
# 1920979970992
iryna += 2810
print(id(iryna))
# 1920979974352
print(iryna)
# 3919
us = [1109, 2810]
love = [1109]
print(id(love))
# 1920981716288
love.append(2810)
print(id(love))
# 1920981716288
print(love)
# [1109, 2810]
name = 'Iryna'
age = 19
salary = 1000
# print('%s is %d years old. Her salary is %d $'(name, age, salary))
# Traceback (most recent call last):
#   File "<pyshell#29>", line 1, in <module>
    # print('%s is %d years old. Her salary is %d $'(name, age, salary))
# TypeError: 'str' object is not callable
mystr = 'I love Kryvyi Rih'
print('str = ', mystr)
# str =  I love Kryvyi Rih
print('first character = ', mystr[0])
# first character =  I
print('last character = ', mystr[-1])
# last character =  h
print('characters 2nd to 5th = ', mystr[2:5])
# characters 2nd to 5th =  lov
print('characters 2, 3, 4 = ', mystr[2:5])
# characters 2, 3, 4 =  lov
print('characters 6th and 2nd last = ', mystr[6:-2])
# characters 6th and 2nd last =   Kryvyi R
print('characters 6...-3 = ', mystr[6:-2])
# characters 6...-3 =   Kryvyi R
"pRoGrAmIZ".lower()
# 'programiz'
'pRoGrAmIz'.upper()
# 'PROGRAMIZ'
'This will split all words into a list'.split()
# ['This', 'will', 'split', 'all', 'words', 'into', 'a', 'list']
''.join(['This', 'will', 'join', 'all', 'words', 'into', 'a', 'string'])
# 'Thiswilljoinallwordsintoastring'
a = 5
dir(a)
# ['__abs__', '__add__', '__and__', '__bool__', '__ceil__', '__class__', '__delattr__', '__dir__', '__divmod__', '__doc__', '__eq__', '__float__', '__floor__', '__floordiv__', '__format__', '__ge__', '__getattribute__', '__getnewargs__', '__gt__', '__hash__', '__index__', '__init__', '__init_subclass__', '__int__', '__invert__', '__le__', '__lshift__', '__lt__', '__mod__', '__mul__', '__ne__', '__neg__', '__new__', '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__', '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__round__', '__rpow__', '__rrshift__', '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__', '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__', '__xor__', 'as_integer_ratio', 'bit_count', 'bit_length', 'conjugate', 'denominator', 'from_bytes', 'imag', 'numerator', 'real', 'to_bytes']
'Happy Birthday'.find('ay')
# 12
'I love Dmytro'.find('Dm')
# 7
'We are a couple'.replace('couple', 'family')
# 'We are a family'
girl = 'Iryna'
boy = girl
print(boy)
# Iryna
print(id(girl))
# 1920981612400
print(id(boy))
# 1920981612400
boy += 'Dmytro'
print(boy)
# IrynaDmytro
girl = 'Iryna'
boy = girl
boy += 'Dmytro'
print(boy)
# IrynaDmytro
x = 'foo'
y = x
y += 'bar'
print(y)
# foobar
girl = 'Iryna'
boy = girl
print(girl)
# Iryna
boy += 'Dmytro'
print(girl)
# Iryna
print(id(girl))
# 1920981612400
print(id(boy))
# 1920953582128
us = [31102020, 21022021, 17052021]
love = us
print(us)
# [31102020, 21022021, 17052021]
love += [12072021 31102021]
# SyntaxError: invalid syntax. Perhaps you forgot a comma?
love += [12072021, 31102021]
print(us)
# [31102020, 21022021, 17052021, 12072021, 31102021]
print(id(us))
# 1920981652928
print(id(love))
# 1920981652928
print(id(us[0]))
# 1920979971024
print(id(us[-1]))
# 1920979973584
print(id(love[-1]))
# 1920979973584
a = 'a'
ord(a)
# 97
a = 'b'
ord(a)
# 98
b = 'a'
ord(b)
# 97
b = 'b'
ord(b)
# 98
a = 5
b = 5.0
c = 3
d = 3.0
print(a+b, a-b, sep=\n)
# SyntaxError: unexpected character after line continuation character
print(a+b, a-b, sep='\n')
# 10.0
# 0.0
a = 5
b = 5.0
c = 3
d = 3.
d = 3.0
print(a+c, a+b, a-c, b-c, a*c, a*b, a/c, b/c, a//c, b//c, a%c, b%c, a**c, b**c, sep='\n')
# 8
# 10.0
# 2
# 2.0
# 15
# 25.0
# 1.6666666666666667
# 1.6666666666666667
# 1
# 1.0
# 2
# 2.0
# 125
# 125.0
star = 4
star +=2
print(star+=2)
# SyntaxError: invalid syntax
print(star += 2)
# SyntaxError: invalid syntax
print(star)
# 6
star = 4
star += 2
print(star)
# 6
star -= 2
print(star)
# 4
star *= 2
print(star)
# 8
star /= 2
print(star)
# 4.0
star //= 1.5
print(star)
# 2.0
4.0/2
# 2.0
4.0/1.5
# 2.6666666666666665
star **= 3
print(star)
# 8.0
star %= 3
print(star)
# 2.0

############################################################################################# practise

eval('print(3+5)')
# 8
eval('print(str(3+5))')
# 8
eval('print(float(3+5))')
# 8.0
eval('print(str(3) + str(5))')
# 35
