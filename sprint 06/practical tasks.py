# Python Online Marathon
# sprint 06
# practical tasks

########################################## 1 ##########################################
################################ PASSED ################################
import json

def find(file, key):
    result = []
    with open(file) as f:
        data = json.load(f)
        # for key in data:
        #     if isinstance(key, str):
        #         result.append(data[key])
        #     elif isinstance(key, list):
        #         for j in key:
        #             result.append(j)
        # return result
        
        for key in data:
            if key in data and isinstance(key, str):
                result.append(key)
                # return result
            elif isinstance(key, list):
                for j in key:
                    result.append(j)
                    # return result
            # else:
            #     return result
        return result
            
        # return result
        # try:
        #     for i in data:
        #         el = str(i)
        #         result.append(i[key])
        #         return result
        # except KeyError:
        #     return result

# def find(file, key):
#     good_columns = ['password']
#     data = []
#     with open(file, "r") as f:
#         objects = ijson.items(f, 'data.item')
#         for row in objects:
#             selected_row = []
#             for item in good_columns:
#                 selected_row.append(row)
        # columns = list(objects)

# def find(file, key):
#     with open(file) as f:
#         data = json.load(f)
#     values = list([i['password1'] for i in data])
#     print(json.dump(values))

# def find(file, key):
#     with open (file) as f:
#         content = json.load(f)
#     values = set()
#     for item in content:
#         values.add(item[key])
#     result = json.dump(list(values))
#     return result
# type your code here

########################################## 2 ##########################################

########################################## 3 ##########################################

########################################## 4 ##########################################

########################################## 5 ##########################################
