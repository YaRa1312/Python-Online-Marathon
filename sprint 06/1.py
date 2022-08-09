import json
def find(file, key):
	m_list =[]
	with open(file) as file:
	    file = json.load(file)
    value = set(list(it_gen(file, key)))
	    for val in value:
            m_list.append(val)
	return m_list
	
def it_gen(file,key):
	if isinstance(file,dict):
		for k,v in file.items():
			if k == key:
				if type(v) == list:
					for i in v:
						yield "".join(i)
				else:
					yield v
			else:
				yield from it_gen(v, key)
	elif isinstance(file, list):
		for item in file:
			yield from it_gen(item, key)
print(find("C:\\Python Online Marathon\\sprint 06\\Test data-20220731\\without_pass.json", 'password'))