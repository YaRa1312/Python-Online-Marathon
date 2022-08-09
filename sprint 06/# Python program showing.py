# Python program showing
# file management using
# context manager

# class FileManager():
# 	def __init__(self, filename, mode):
# 		self.filename = filename
# 		self.mode = mode
# 		self.file = None
		
# 	def __enter__(self):
# 		self.file = open(self.filename, self.mode)
# 		return self.file
	
# 	def __exit__(self, exc_type, exc_value, exc_traceback):
# 		self.file.close()

# # loading a file
# with FileManager('C:\Python Online Marathon\sprint 06\1.json', 'r') as f:
# 	f.read()

# print(f.closed)

# import json

# def find(file, key):
#     with open (file) as f:
#         content = json.load(f)
#     values = set()
#     for item in content:
#         values.add(item[key])
#     result = json.dump(list(values))
#     return result
# # type your code here
# print(find(".\1.json", "password"))



# jsonFile = open('C:\\Python Online Marathon\\sprint 06\\1.json', 'r')
# data = json.load(jsonFile)

# size=len(data["password"])
# print (size)
# values = [];
# uniqueNames = [];
# for i in data["password"]:
#     if(i["password"] not in uniqueNames):
#          uniqueNames.append(i["password"]);
#          values.append(i)
# jsonFile.close()
# str_json = """
# [
#     {
#         "name": "user_1",
#         "password": "pass_1"
#     },
#     {
#         "name": "user_2",
#         "password": [
#             "pass_1",
#             "qwerty"
#         ]
#     }
# ]
# """

# data = json.loads(str_json)
# print(data['password'])

mydata = [
    {
        "name": "Bob1",
        "pass": "_00_"
    }, 
    {
        "name": "Bob2",
        "pass": ["_00_", "56"]
    }
]
for el in mydata:
    if 'pass' in el.keys():
        print(True)
    else:
        print(False)
# res = []
# for i in mydata:
#     for key, value in i.items():
#         if i['password'] in i:
#             res.append(i['password'])
#         else:
#             res
# print(res)
# for i in mydata:
#     for key, value in i.items():
#         if key == 'password':
#             print(i[key])

data = {
        "name": "user",
        "password": ["_00_"],
        "love": 123
}
# flag = False
# res = []
# for key, value in data.items():
#     if isinstance(data['password'], list):
#         for el in data["password"]:
#             res.append(el)
        # result = data['password']
# res.append(result)
# new_res = set(res)
# result = list(new_res)
# print(result)
# result = list(set(res)) # !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# print(result)