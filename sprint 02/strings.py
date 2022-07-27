# Python Online Marathon
# sprint 02
# strings
############################################################################################# theory

mystr = 'I love Ukraine!'
mystr.capitalize()
# 'I love ukraine!'
mystr.casefold()
# 'i love ukraine!'
mystr.center(18)
# ' I love Ukraine!  '
mystr.center(35, '!')
# '!!!!!!!!!!I love Ukraine!!!!!!!!!!!'
mystr.count('3')
# 0
mystr.count('I')
# 1
mystr.count('I', 2)
# 0
mystr.count('I', 0, 7)
# 1
mystr.encode()
# b'I love Ukraine!'
mystr.encode(encoding='utf-8', errors='strict')
# b'I love Ukraine!'
mystr.encode(encoding='utf-8')
# b'I love Ukraine!'
mystr.endswith('e')
# False
mystr.endswith('!')
# True
mystr.endswith('e!', 0, 14)
# False
mystr.endswith('e!', 13, 14)
# False
mystr.endswith('!', 14)
# True
mystr.expandtabs(tabsize=8)
# 'I love Ukraine!'
mystr
# 'I love Ukraine!'
mystr.expandtabs()
# 'I love Ukraine!'
mystr.expandtabs(tabsize=15)
# 'I love Ukraine!'
mystr.find('kra')
# 8
mystr.find('kra', 0, 12)
# 8
mystr.find('kra', 9)
# -1
mystr.find('r', 13)
# -1
mystr.find('ov', 13)
# -1
mystr.find('ov', 0, 4)
# -1
mystr.find('ov', 0, 5)
# 3
ticket = 'The ticket costs {cost: .2f} hryvnias'
ticket.format(cost=850)
# 'The ticket costs  850.00 hryvnias'
travel1 = 'I visited {city}, and it was in {year}'.format(city='Paris', year=2023)
travel1
# 'I visited Paris, and it was in 2023'
travel2 = 'I visited {0}, and it was in {1}'.format('London', 2024)
travel2
# 'I visited London, and it was in 2024'
travel3 = 'I visited {}, and it was in {}'.format('New York', 2025)
travel3
# 'I visited New York, and it was in 2025'
halychyna = {'x': 'Zolochiv', 'y': 2021}
'I was in {x} in {y}'.format_map(halychyna)
# 'I was in Zolochiv in 2021'
friends = {'name': ['Maryna', 'Lilia', 'Veronika'], 'profession': ['an artist', 'an interpreter', 'a writer']}
'{name[0]} is my sister and she is {profession[0]}. My friend {name[1]} from Zolochiv works as {profession[1]}. But my other friend {name[2]} is happy to be {profession[2]}!'.format_map(friends)
# 'Maryna is my sister and she is an artist. My friend Lilia from Zolochiv works as an interpreter. But my other friend Veronika is happy to be a writer!'
mystr[10:-1]
# 'aine'
