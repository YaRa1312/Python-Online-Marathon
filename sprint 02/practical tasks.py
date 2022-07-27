# Python Online Marathon
# sprint 02
# practical tasks

########################################## 1 ##########################################
################################ PASSED ################################
def double_string(data):
    '''
    doc task 1
    '''
    counter = 0
    for i in data:
        if any(i+el in data for el in data):
            counter+=1
    return counter

########################################## 2 ##########################################
################################ PASSED ################################
def morse_number(x):
    '''
    doc task 2
    '''
    res = []
    for char in x:
        if char == '0':
            res.append('-----')
        elif char == '1':
            res.append('.----')
        elif char == '2':
            res.append('..---')
        elif char == '3':
            res.append('...--')
        elif char == '4':
            res.append('....-')
        elif char == '5':
            res.append('.....')
        elif char == '6':
            res.append('-....')
        elif char == '7':
            res.append('--...')
        elif char == '8':
            res.append('---..')
        elif char == '9':
            res.append('----.')
    res_string = ' '.join(res)
    return res_string

########################################## 3 ##########################################
################################ PASSED ################################
import math
def figure_perimetr(situation):
    '''
    doc 3
    '''
    lb_x = int(situation[3:4])
    lb_y = int(situation[5:6])
    
    rb_x = int(situation[9:10])
    rb_y = int(situation[11:12])
    
    lt_x = int(situation[15:16])
    lt_y = int(situation[17:18])
    
    rt_x = int(situation[21:22])
    rt_y = int(situation[23:24])
    
    distance_lb_rb = math.sqrt((rb_x-lb_x)**2 + (rb_y-lb_y)**2)
    distance_rb_rt = math.sqrt((rt_x-rb_x)**2 + (rt_y-rb_y)**2)
    distance_rt_lt = math.sqrt((lt_x-rt_x)**2 + (lt_y-rt_y)**2)
    distance_lt_lb = math.sqrt((lb_x-lt_x)**2 + (lb_y-lt_y)**2)
    
    perimetr = distance_lb_rb + distance_rb_rt + distance_rt_lt + distance_lt_lb
    
    return perimetr

########################################## 4 ##########################################
################################ PASSED ################################
import re
def pretty_message(data):
    'doc task 4'
    result = re.sub(r'([a-z]+?)\1+', r'\1', data)
    return result

########################################## 5 ##########################################
################################ PASSED ################################
import re
def max_population(data):
    '''
    doc task 5
    '''
    res = []
    for i in data:
        res.append(re.split(',', i))
    res.pop(0)
    
    population = []
    for i in res:
        population.append(int(i[2]))
    max_population_int = max(population)
    
    my_result = []
    my_result.append(max_population_int)
    max_population_str = str(max_population_int)
    for i in res:
        if max_population_str in i:
            my_result.insert(0, i[1])
    
    result = tuple(my_result)
    
    return result
