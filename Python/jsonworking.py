data = [{'username':"a","id":1, "age":10},
	{'username':"b","id":2, "age":10},
	{'username':"c","id":3, "age":10}
]
print(data)
print("-----------------------------------------------")
new_list = []
for dict_data in data:
	new_dict = [(k,v) for k, v in dict_data.items() if k != "age"]
	new_list.append(dict(new_dict))
print(new_list)

new_dict = [(dict_data.keys(), dict_data.values()) for dict_data.items() in data if dict_data.keys() != "age" else None]
print(new_dict)