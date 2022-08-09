# Python Online Marathon
# sprint 06
# practical tasks

########################################## 1 ##########################################
# Create function find(file, key)
# This function parses json-file and returns all unique values of the key.

# 1.json:
# [{"name": "user_1”, "password": "pass_1”},
# {"name": "user_2”, "password": ["pass_1", "qwerty“]} ]
# find("1.json", "password") returns ["pass_1", "qwerty"]

# 2.json:
# [{"name": "user_1”, "credentials": {"username": "user_user”, "password": "1234qweQWE"}}, {"name": "user_2”, "password": ["pass_1 ", "qwerty "]}]
# find("2.json", "password") returns ["1234qweQWE", "pass_1", "qwerty"]

# 3.json:
# {"name": "user_1","credentials": {"username": "user_user","password": "1234qweQWE"}}
# find("3.json", "password") returns ["1234qweQWE"]


########################################## 2 ##########################################
# Implement function parse_user(output_file, *input_files) for creating file that will contain only unique records (unique by key "name") by merging information from all input_files argument (if we find user with already existing name from previous file we should ignore it). Use pretty printing for writing users to json-file.


# If the function cannot find input files we need to log information with error level  

# root - ERROR - File <file name> doesn't exist

# For example:
# user1.json : 
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# ]

# user2.json : 
# [{"name": "Bob1", "rate": 25, “languages": ["French"]},
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]

# If we execute parse_user(user3.json, user1.json, user2.json)
# then file user3.json should contain information:
# [{"name": "Bob1", "rate": 1, “languages": ["English"]},
# {"name": "Bob2", "rate":0.78, "languages": ["English", "French"]}
# {"name": "Bob3", "rate": 78, "languages": ["Germany"]}
# ]
import json
# type your code here
def find(file,key):
    output=[]
    def parse_json(json_obj):
        for k, v in json_obj.items():
            if k == key:
                output.append(v)
    with open(file) as file:
        json.load(file,object_hook=parse_json)
    l=[]
    for i in output:
        if type(i)==list:
            l+=[*i]
            output.remove(i)
    return list(set(output+l))

print(find('C:\\Python Online Marathon\\sprint 06\\Test data-20220731\\array_pass.json','password'))
########################################## 3 ##########################################
# In user.json file we have information about users in format [{“id”: 1, “name”: “userName”, “department_id”: 1}, ...], 

# in file department.json are information about departments in format: [{“id”: 1, “name”: “departmentName”}, ...]. 

# Function user_with_department(csv_file, user_json, department_json) should read from json files information and create csv file in format:

# header line - user, department

# next lines :  <userName>, <departmentName>

# If file department.json doesn't contain department with department_id from user.json we generate DepartmentName exception.

# Create appropriate json-schemas for user and department.

# If schema for user or department doesn't satisfy formats described above we should generate InvalidInstanceError exception  

# To validate instances create function validate_json(data, schema)


########################################## 4 ##########################################
# Class Student has attributes full_name:str, avg_rank: float, courses: list
# Class Group has attributes title: str, students: list.

# Make both classes JSON serializable. 

# Json-files represent information about student (students). 

# Create methods:  

# Student.from_json(json_file) that return Student instance from attributes from json-file;

# Group.serialize_to_json(list_of_groups, filename)

# Group.create_group_from_file(students_file)

# Parse given files, create instances of Student class and create instances of Group class (title for group is name of json-file without extension).


########################################## 5 ##########################################
# Create context manager class SerializeManager with attributes filename and type for serializing python object to different formats.
# This class should contain method serialize for serialize object to filename according to  type. 
# For defining format create enum FileType with values JSON, BYTE.
# Create function serialize(object, filename, filetype).
# This function use SerializeManager and should serialize object to filename according to type.
# For example:
# if user_dict = { 'name': 'Roman', 'id': 8}
# then
# serialize(user_dict, "2", FileType.BYTE) -> creates file with name "2" and this file will contain user_dict as byte array
# serialize("String", "string.json", FileType.JSON) -> creates file with name "string.json" and text "String"
