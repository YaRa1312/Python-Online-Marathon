# Python Online Marathon
# sprint 02
# regular expressions
############################################################################################# theory

import re
ukrstring = 'Glory to Ukraine!'
res = re.findall(r' ', ukrstring)
res
# [' ', ' ']
res.count(' ')
# 2
res.count('!')
# 0
x = 'Ukraine became independent in 1991. We had 3 revolutions and 1 war that begun in 2014.'
y = re.findall(r'[0-9]+', x)
y
# ['1991', '3', '1', '2014']
emails = 'superfrench041@gmail.com, lyaka119@ukr.net are my emails'
result = re.findall(r'(\S+@\S+[^,| ])', emails)
result
# ['superfrench041@gmail.com', 'lyaka119@ukr.net']
