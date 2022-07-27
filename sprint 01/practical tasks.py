# Python Online Marathon
# sprint 01
# practical tasks

########################################## 1 ##########################################
################################ PASSED ################################
def kthTerm(n, k):
    '''
    doc task 1
    '''
    degree = 0
    result = 0
    list_for = []
    while True:
        if len(list_for) >= k:
            break
        temp_list = []
        result = n ** degree
        temp_list.append(result)
        if len(list_for) > 0:
            for elem in list_for:
                result = n ** degree + elem
                temp_list.append(result)
            else:
                degree += 1
                list_for = list_for + temp_list
        else:
            degree += 1
            list_for = list_for + temp_list

    answer = list_for[k - 1]
    return answer
    
########################################## 2 ##########################################
################################ PASSED ################################
def filterBible(scripture, book, chapter):
    '''
    doc task 2
    'bb' (book) has to be 01<=bb<=66
    'ccc' (chapter) has to be 001<=ccc
    'vvv' (verse) has to be 001<=vvv
    '''
    result = []
    for i in scripture:
        if book == i[:2] and chapter == i[2:5]:
            result.append(i)
    return result
    
########################################## 3 ##########################################
################################ PASSED ################################
def isPalindrome(str):
    '''
    doc task 3
    '''
    freq_char_dict = {}
    for char in str:
        freq_char_dict[char] = freq_char_dict.get(char, 0) + 1
    odd_count = 0
    for i in freq_char_dict.values():
        if i % 2 == 1:
            odd_count = odd_count + 1
        if odd_count > 1:
            return False
    return True

########################################## 4 ##########################################
################################ PASSED ################################
def findPermutation(n, p, q):
    '''
    doc task 4
    '''
    r = []
    for i in range(n):
        r.insert(i, p.index(q[i])+1)
    return r

########################################## 5 ##########################################
################################ PASSED ################################
def toPostFixExpression(e):
    '''
    doc task 5
    '''
    result = []
    operator = []
    priority = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    ''.join(e)
    for char in e:
        if char == '(':
            operator.append(char)
        elif char == ')':
            while operator[-1] != '(':
                el = operator.pop()
                result.append(el)
            operator.pop()
        elif char == '^' or char == '*' or char == '/' or char == '+' or char == '-':
            if len(operator) > 0:
                while priority[operator[-1]] >= priority[char]:
                    el = operator.pop()
                    result.append(el)
                    if len(operator) == 0:
                        break
            operator.append(char)
        else:
            result.append(char)
    while len(operator) != 0:
        el = operator.pop()
        result.append(el)
    return result
    
########################################## 6 ##########################################
################################ PASSED ################################
def order(a):
    '''
    doc task 6
    '''
    ascending = 'ascending'
    descending = 'descending'
    not_sorted = 'not sorted'
    if sorted(a) == a:
        return ascending
    elif sorted(a, reverse=True) == a:
        return descending
    else:
        return not_sorted

########################################## 7 ##########################################
################################ PASSED ################################
def Cipher_Zeroes(N):
    '''
    doc task 7
    '''
    visible_zeroes = 0
    for i in N:
        if i == '0' or i == '6' or i == '9':
            visible_zeroes += 1
        elif i == '8':
            visible_zeroes += 2
    if visible_zeroes % 2 == 1:
        visible_zeroes += 1
    elif visible_zeroes % 2 == 0 and visible_zeroes > 0:
        visible_zeroes -= 1
    result = bin(visible_zeroes)[2:]
    return result

########################################## 8 ##########################################
################################ PASSED ################################
def studying_hours(a):
    '''
    doc task 8
    '''
    days = 1
    list_of_counts = []
    for index in range(len(a)):
        if a[index:index + 1] <= a[index + 1:index + 2]:
            days += 1

        else:
            list_of_counts.append(days)
            days = 1

    return max(list_of_counts)
