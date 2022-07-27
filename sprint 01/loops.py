# Python Online Marathon
# sprint 01
# loops
############################################################################################# theory

start = 0
finish = 10
while start < finish:
    print(start)
    start += 1
else:
    print('The end')

    
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# The end
for j in [0, 1, 2, 3, 4]:
    print(j)
else:
    print(j, ' is the last one')

    
# 0
# 1
# 2
# 3
# 4
# 4  is the last one
[i for i in range(10)]
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[i for i in range(5, 10)]
# [5, 6, 7, 8, 9]
[i for i in range(0, 10, 2)]
# [0, 2, 4, 6, 8]
for val in "string":
    if val == 'i':
        break
    print(val)
    print("The end")

    
# s
# The end
# t
# The end
# r
# The end
for val in 'string':
    if val == 'i':
        break
    print(val)

    
# s
# t
# r
for val in 'string':
    if val == 'i':
        continue
    print(val)

    
# s
# t
# r
# n
# g
for val in "I love you!!!":
    if val == ' ':
        continue
    if val == '!':
        break
    print(val)

    
# I
# l
# o
# v
# e
# y
# o
# u
sequence = {'p', 'a', 's', 's'}
for val in sequence:
    pass

############################################################################################# practise

a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
    i **= i
    print(i)

    
# 1
# 1
# 2
# 4
# 3
# 27
# 4
# 256
# 5
# 3125
a = [[1, 2], 3, 4, 5]
for i in a:
    print(i)
    if isinstance(i, list):
        i.append(100)
    print(a)

    
# [1, 2]
# [[1, 2, 100], 3, 4, 5]
# 3
# [[1, 2, 100], 3, 4, 5]
# 4
# [[1, 2, 100], 3, 4, 5]
# 5
# [[1, 2, 100], 3, 4, 5]
a = [1, 2, 3, 4, 5]
for i in a:
    print(i)
    if i == 3:
        a.insert(5, 100)
    print(a)

    
# 1
# [1, 2, 3, 4, 5]
# 2
# [1, 2, 3, 4, 5]
# 3
# [1, 2, 3, 4, 5, 100]
# 4
# [1, 2, 3, 4, 5, 100]
# 5
# [1, 2, 3, 4, 5, 100]
# 100
# [1, 2, 3, 4, 5, 100]

# using BREAK (+else works or not)?
k = 0
while k != 10:
    k += 1
    print(k)
    if k == 5:
        break
else:
    print("else")

    
# 1
# 2
# 3
# 4
# 5
k = 10
for i in range(k):
    print(i)
    if i == 5:
        break
else:
    print('else')

    
# 0
# 1
# 2
# 3
# 4
# 5
for i in range(5):
    for j in range(i, i+5):
        print(f'{i}-{j}')
        if j % 2 != 1:
            break

        
# 0-0
# 1-1
# 1-2
# 2-2
# 3-3
# 3-4
# 4-4

# using CONTINUE

k = 5
while k != 0:
    k -= 1
    if k == 3:
        continue
    print(k)

    
# 4
# 2
# 1
# 0
k = 5
for i in range(k):
    if k == 3:
        continue
    print(k)

    
# 5
# 5
# 5
# 5
# 5
