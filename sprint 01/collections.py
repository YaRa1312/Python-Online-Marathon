# Python Online Marathon
# sprint 01
# collections
############################################################################################# theory

############################################## LIST ##############################################
love = ['Iryna', 1109, 'Dmytro', 2810]
love.append(31.10)
# love
['Iryna', 1109, 'Dmytro', 2810, 31.1]
love.clear()
love
# []
love.append('Iryna')
love.append(1109)
love.append('Dmytro')
love.append(2810)
love.append(31.10)
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1]
love.copy()
# ['Iryna', 1109, 'Dmytro', 2810, 31.1]
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1]
love.count('Iryna')
# 1
love.extend('teddybear')
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 't', 'e', 'd', 'd', 'y', 'b', 'e', 'a', 'r']
love.append('teddybear')
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 't', 'e', 'd', 'd', 'y', 'b', 'e', 'a', 'r', 'teddybear']
love.index('teddybear')
# 14
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 't', 'e', 'd', 'd', 'y', 'b', 'e', 'a', 'r', 'teddybear']
love.insert(5, 1705)
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 1705, 't', 'e', 'd', 'd', 'y', 'b', 'e', 'a', 'r', 'teddybear']
love.insert(-10, 13.07)
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 1705, 13.07, 't', 'e', 'd', 'd', 'y', 'b', 'e', 'a', 'r', 'teddybear']
love.pop(-2)
# 'r'
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 1705, 13.07, 't', 'e', 'd', 'd', 'y', 'b', 'e', 'a', 'teddybear']
love.pop(-4)
# 'b'
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 1705, 13.07, 't', 'e', 'd', 'd', 'y', 'e', 'a', 'teddybear']
love.remove('t')
love.remove('y')
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 1705, 13.07, 'e', 'd', 'd', 'e', 'a', 'teddybear']
love.count('d')
# 2
love.extend('kitten')
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 1705, 13.07, 'e', 'd', 'd', 'e', 'a', 'teddybear', 'k', 'i', 't', 't', 'e', 'n']
love.reverse()
love
# ['n', 'e', 't', 't', 'i', 'k', 'teddybear', 'a', 'e', 'd', 'd', 'e', 13.07, 1705, 31.1, 2810, 'Dmytro', 1109, 'Iryna']
love.reverse()
love
# ['Iryna', 1109, 'Dmytro', 2810, 31.1, 1705, 13.07, 'e', 'd', 'd', 'e', 'a', 'teddybear', 'k', 'i', 't', 't', 'e', 'n']
num = [1, 2, 3, 4]
num
# [1, 2, 3, 4]
num.append([5, 6])
num
# [1, 2, 3, 4, [5, 6]]
num.extend([7, 8])
num
# [1, 2, 3, 4, [5, 6], 7, 8]
num.append(9)
num
# [1, 2, 3, 4, [5, 6], 7, 8, 9]
all(love)
# True
any(num)
# True
empty = []
any(empty)
# False
all(empty)
# True
enumerate(love)
# <enumerate object at 0x00000217342C3DC0>
enumerate(num)
# <enumerate object at 0x00000217342C1080>
enumerate(empty)
# <enumerate object at 0x00000217324E0D80>
len(love)
# 19
len(num)
# 8
len(empty)
# 0
poland = {203: "arriving", 2407: "departure"}
list(poland)
# [203, 2407]
poland
# {203: 'arriving', 2407: 'departure'}
pol = {'arriving': 203, 'departure': 2407}
pol
# {'arriving': 203, 'departure': 2407}
list(pol)
# ['arriving', 'departure']
max(list(poland))
# 2407
min(list(poland))
# 203
sorted(poland)
# [203, 2407]
u = [12, 3333, 213, 5.677, 44, 78.3424]
sorted(u)
# [5.677, 12, 44, 78.3424, 213, 3333]
sum(u)
# 3686.0194
x = ['apple', 'banana', 'cherry']
y = enumerate(x)
print(list(y))
[(0, 'apple'), (1, 'banana'), (2, 'cherry')]
pow2 = [2 ** x for x in range(10)]

pow2
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
pow2 = []
for x in range(10):
    pow2.append(x)

    
pow2
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
pow2 = []
for x in range(10):
    pow2.append(2 ** x)

    
pow2
# [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
[x+y for x in ['Python', 'C'] for y in ['Language', 'Programming']]
# ['PythonLanguage', 'PythonProgramming', 'CLanguage', 'CProgramming']
[x + y for x in ['Python ', 'C '] for y in ['Language ', 'Programming ']]
# ['Python Language ', 'Python Programming ', 'C Language ', 'C Programming ']
for fruit in ['apple', 'banana', 'cherry']:
    print("I like ", fruit)

    
# I like  apple
# I like  banana
# I like  cherry
fruit = ['apple', 'banana', 'cherry']
i = 0
for i in range(len(fruit)):
    print("I like fruit", fruit[i])

    
# I like fruit apple
# I like fruit banana
# I like fruit cherry
# t = (1, 3, 2)

############################################## TUPLE ##############################################
t = (1, 3, 2)
t[1]
# 3
(a, b, c) = t
a
# 1
b
# 3
(a, b, c)
# (1, 3, 2)
a, b = b, a
a, b
# (3, 1)
t
# (1, 3, 2)
a
# 3
b
# 1
c
# 2
r = list(t)
r
# [1, 3, 2]
tuple(r)
# (1, 3, 2)
r
# [1, 3, 2]
t.count(1)
# 1
t.count(2)
# 1
t.count(3)
# 1
t.index(1)
# 0
t.index(2)
# 2
t.index(3)
# 1
t
# (1, 3, 2)

############################################## SET ##############################################
myset = {5, 43, 887, 4.7, 3.6785, 33}
myset.add(6)
myset
# {33, 3.6785, 4.7, 5, 6, 887, 43}
myset
# {33, 3.6785, 4.7, 5, 6, 887, 43}
myset.add(4.7)
myset
# {33, 3.6785, 4.7, 5, 6, 887, 43}
set1 = {1, 2, 3, 11, 22, 33}
set2 = {0, 9, 8, 99, 88}
set1.difference()
# {1, 2, 3, 33, 22, 11}
set2.difference()
# {0, 99, 8, 9, 88}
set1.difference(set2)
# {1, 2, 3, 33, 11, 22}
set2.difference(set1)
# {0, 99, 8, 9, 88}
set1.difference_update(set2)
set1
# {1, 2, 3, 33, 22, 11}
set2
# {0, 99, 8, 9, 88}
print(set1.difference_update(set2))
# None
print(set2.difference_update(set1))
# None
set1.discard(1)
set1
# {2, 3, 33, 22, 11}
set1.add(1)
set1
# {1, 2, 3, 33, 22, 11}
set1.discard(111)
set1
# {1, 2, 3, 33, 22, 11}
set1.discard(99)
set1
# {1, 2, 3, 33, 22, 11}
set1.add(1)
set1
# {1, 2, 3, 33, 22, 11}
set1.add(1)
set1
# {1, 2, 3, 33, 22, 11}
set1.intersection()
# {1, 2, 3, 33, 22, 11}
set1.intersection(set2)
set1
# {1, 2, 3, 33, 22, 11}
set2
# {0, 99, 8, 9, 88}
set2.intersection(set1)
set2
# {0, 99, 8, 9, 88}
set1
# {1, 2, 3, 33, 22, 11}
set1.difference([1, 66])
# {2, 3, 33, 22, 11}
set1
# {1, 2, 3, 33, 22, 11}
set1.difference([1, 2, 3])
# {33, 22, 11}
set1.difference([1, 66, 2, 55])
# {3, 33, 22, 11}
set1.difference_update([1, 2, 3])
set1
# {33, 22, 11}
set1
# {33, 22, 11}
set1.add(1)
set1.add(2)
set1.add(3)
set1
# {2, 1, 33, 3, 22, 11}
set2
# {0, 99, 8, 9, 88}
set2.add(1)
set2.add(2)
set2.add(3)
set1.intersection(set2)
# {1, 2, 3}
set2.intersection(set1)
# {1, 2, 3}
set1.intersection_update(set2)
set1
# {1, 2, 3}
set2
# {0, 1, 2, 99, 3, 8, 9, 88}
set1.add(11)
set1.add(22)
set1.add(33)
set1
# {1, 2, 3, 33, 11, 22}
set2
# {0, 1, 2, 99, 3, 8, 9, 88}
set2.intersection_update(set1)
set2
# {1, 2, 3}
set1
# {1, 2, 3, 33, 11, 22}
set2.add(8)
set2.add(9)
set2.add(88)
set2.add(99)
set2
# {1, 2, 3, 99, 8, 9, 88}
set2.add(0)
set2
# {0, 1, 2, 3, 99, 8, 9, 88}
set1
# {1, 2, 3, 33, 11, 22}
set1.isdisjoint(set2)
# False
set2.isdisjoint(set1)
# False
set1.issubset(set2)
# False
set2.issubset(set1)
# False
set1.issuperset(set2)
# False
set2.issuperset(set1)
# False
set01 = {55, 44, 54, 45}
set02 = {3}
set1.isdisjoint(set2)
# False
set01.isdisjoint(set02)
# True
sset = {6, 7, 3, 2}
ssett = {3, 2}
ssett.issubset(sset)
# True
sset.issuperset(ssett)
# True
set1.pop()
# 1
set1
# {2, 3, 33, 11, 22}
set1.add(1)
set1
# {1, 2, 3, 33, 11, 22}
set01
# {44, 45, 54, 55}
set01.pop()
# 44
set01.pop()
# 45
set01.add(44)
set01.add(45)
set01
# {44, 45, 54, 55}
set02
# {3}
sset
# {2, 3, 6, 7}
sset.remove(2)
sset
# {3, 6, 7}
sset.add(2)
sset
# {2, 3, 6, 7}
ssett
# {2, 3}
set1
# {1, 2, 3, 33, 11, 22}
set2
# {0, 1, 2, 3, 99, 8, 9, 88}
set01
# {44, 45, 54, 55}
set02
# {3}
set02.add(7)
set02.add(77)
set01
# {44, 45, 54, 55}
set02
# {3, 77, 7}
set01.symmetric_difference(set02)
# {3, 7, 44, 45, 77, 54, 55}
set01
# {44, 45, 54, 55}
set02.symmetric_difference(set01)
# {3, 7, 44, 45, 77, 54, 55}
set02
# {3, 77, 7}
set01.symmetric_difference_update(set02)
set01
# {3, 7, 44, 45, 77, 54, 55}
set02
# {3, 77, 7}
set01.remove(3)
set01.remove(7)
set01.remove(77)
set01
# {44, 45, 54, 55}
set02
# {3, 77, 7}
set02.symmetric_difference_update(set01)
set02
# {3, 7, 44, 45, 77, 54, 55}
set01
# {44, 45, 54, 55}
set02.remove(44)
set02.remove(45)
set02.remove(54)
set02.remove(55)
set02
# {3, 7, 77}
set01
# {44, 45, 54, 55}
set01.union(set02)
# {3, 7, 77, 54, 55, 44, 45}
set01
# {44, 45, 54, 55}
set02
# {3, 7, 77}
id(set01.union(set02))
# 2298682547264
id(set01)
# 2298682544576
id(set02)
# 2298682544352
set02.union(set01)
# {3, 45, 55, 54, 7, 44, 77}
set01.update(set02)
set01
# {3, 7, 44, 45, 77, 54, 55}
set02
# {3, 7, 77}
set01.remove(3)
set01.remove(7)
set01.remove(77)
set01
# {44, 45, 54, 55}
set02
# {3, 7, 77}
set02.update(set01)
set02
# {3, 7, 44, 77, 45, 55, 54}
set01
# {44, 45, 54, 55}
set02.remove(44)
set02.remove(45)
set02.remove(54)
set02.remove(55)
set02
# {3, 7, 77}
set01
# {44, 45, 54, 55}

############################################## DICT ##############################################
h = {'key1': 12, 'python': 'word'}
h['key1']
# 12
h['hello'] = 'world'
h
# {'key1': 12, 'python': 'word', 'hello': 'world'}
h['hello'] = 'sweetie'
h
# {'key1': 12, 'python': 'word', 'hello': 'sweetie'}
del(h['hello'])
h
# {'key1': 12, 'python': 'word'}
h.fromkeys('key1')
# {'k': None, 'e': None, 'y': None, '1': None}
h
# {'key1': 12, 'python': 'word'}
h.fromkeys('python')
# {'p': None, 'y': None, 't': None, 'h': None, 'o': None, 'n': None}
h
# {'key1': 12, 'python': 'word'}
h.fromkeys([1, 2, 3, 4])
# {1: None, 2: None, 3: None, 4: None}
h.fromkeys('bear')
# {'b': None, 'e': None, 'a': None, 'r': None}
seq = ('name', 'age', 'sex')
h = h.fromkeys(seq)
print('New dict: %s'% str(h))
# New dict: {'name': None, 'age': None, 'sex': None}
h = h.fromkeys(seq, 10)
print('New dict: %s'% str(h))
# New dict: {'name': 10, 'age': 10, 'sex': 10}
h
# {'name': 10, 'age': 10, 'sex': 10}
h.get('age')
# 10
h.popitem()
# ('sex', 10)
h
# {'name': 10, 'age': 10}
h.popitem()
# ('age', 10)
h
# {'name': 10}
h.popitem()
# ('name', 10)
h
# {}
other = [('me', 'you'), ('first date', 3110), ('first night', 17.05)]
h.update([other])
h
# {}
other = {'me': 'ýou'}
h.update({'me': 'you'})
h
# {'m': 'e', 'me': 'you'}
h.pop('m')
# 'e'
h
# {'me': 'you'}
h.update({"first date": 3110})
h
# {'me': 'you', 'first date': 3110}
h.update({"first night": 17.05})
h
# {'me': 'you', 'first date': 3110, 'first night': 17.05}
h.keys()
# dict_keys(['me', 'first date', 'first night'])
h.values()
# dict_values(['you', 3110, 17.05])
h.setdefault('me')
# 'you'
h
# {'me': 'you', 'first date': 3110, 'first night': 17.05}
h.setdefault('first vacation')
h
# {'me': 'you', 'first date': 3110, 'first night': 17.05, 'first vacation': None}
all(h)
# True
h
# {'me': 'you', 'first date': 3110, 'first night': 17.05, 'first vacation': None}
any(h)
# True
len(h)
# 4
me = {'name': 'Iryna', 'age': 19}
you = {'name': 'Dmytro', 'age': 27}
sorted(me)
# ['age', 'name']
sorted(you)
# ['age', 'name']
me
# {'name': 'Iryna', 'age': 19}
you
# {'name': 'Dmytro', 'age': 27}
squares = {x: x*x for x in range(6)}
squares
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
squares = {}
for i in range(6):
    squares[i] = i*i

    
squares
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
odd_squares = {x: x*x for x in range(11) if x%2 == 1}
odd_squares
# {1: 1, 3: 9, 5: 25, 7: 49, 9: 81}
d = {'name': 'Iryna', 'surname': "Pleshyvtseva", 'age': 19, 'course': 'Python Online Marathon 2022'}
for key in d:
    print('student {} = {}'.format(key, d[key]))

    
# student name = Iryna
# student surname = Pleshyvtseva
# student age = 19
# student course = Python Online Marathon 2022
for key, val in d.items():
    print('{} = {} .'.format(key, val, sep='\n+'))

    
# name = Iryna .
# surname = Pleshyvtseva .
# age = 19 .
# course = Python Online Marathon 2022 .
for key in d.keys():
    print('student {} = {}'.format(key, d[key]))

    
# student name = Iryna
# student surname = Pleshyvtseva
# student age = 19
# student course = Python Online Marathon 2022
for val in d.values():
    print('student {} = {}'.format('?', val))

    
# student ? = Iryna
# student ? = Pleshyvtseva
# student ? = 19
# student ? = Python Online Marathon 2022

############################################################################################# practise

############################################## LIST ##############################################
newList = [1, 2, 3]
newList1 = newList.copy()
print(id(newList), id(newList1), sep='\n')
# 1302901605440
# 1302865173312
print(id(newList[0]), id(newList1[0]), sep='\n')
# 1302864527600
# 1302864527600
print(id(newList[1]), id(newList1[1]), sep='\n')
# 1302864527632
# 1302864527632
print(id(newList[2]), id(newList1[2]), sep='\n')
# 1302864527664
# 1302864527664

############################################## DICT ##############################################
ageList = [{'age': 132}, {'age': 13}, {'age': 1}, {'age': 46}]
ageList.sort(key=lambda e: e['age'])
print(ageList)
# [{'age': 1}, {'age': 13}, {'age': 46}, {'age': 132}]
ageList = [{'age': 132}, {'age': 13}, {'age': 1}, {'age': 46}]
ageList.sort(key=lambda e: e['age'], reverse=True)
print(ageList)
# [{'age': 132}, {'age': 46}, {'age': 13}, {'age': 1}]
d1 = {'name': 'Iryna', 'age': 19}
d2 = dict.fromkeys(d1, 'undefined')
print(d2)
# {'name': 'undefined', 'age': 'undefined'}
