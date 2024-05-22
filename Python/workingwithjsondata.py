# from urllib.request import urlopen
# import json

# url = "https://github.com/awasekhirni/jsondata/blob/master/100books.json"

# response = urlopen(url)
# json_data = json.loads(response.read())

# print(json_data)


# x = '{"Name":"Ram","Age":25,"Address":"Lalitpur"}'
# y = json.loads(x)
# print(y)   # Display all the files in dictionary format
# print(y["Name"])    # Display name only
# print(y["Age"])    # Display Age only
# print(y["Address"])    # Display Address only

# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# y = json.dumps(x)    # .dumps() function convert dictionary into json format
# print(y)

# x = {1,2,3,4,5}
# y = json.dumps(x)  # Cannot convert due to different data type
# print(y)

# print(json.dumps(dict({"name":"John","age":29})))
# print(json.dumps(list([1,2,3,4,5])))
# print(json.dumps(tuple((6,7,8,9,0))))
# print(json.dumps("Hello"))
# print(json.dumps(32))
# print(json.dumps(34.5))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))


# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # print(json.dumps(x, indent=4, separators=(".","=")))    # indent and separators are the parameters. indent gives space between {} and separator act like "name" = "John".
# print(json.dumps(x, indent=3, sort_keys=True))   


# import json

# json_data ={
#   "firstName": "Jane",
#   "lastName": "Doe",
#   "hobbies": ["running", "sky diving", "singing"],
#   "age": 35,
#   "children": [
#     {
#       "firstName": "Alice",
#       "age": 6
#     },
#     {
#       "firstName": "Bob",
#       "age": 8
#     }
#   ]
# }

# with open("json_example_writing.json", 'w') as write_file:
#     json.dump(json_data, write_file)
#     json_string = json.dumps(json_data, indent=3)
#     print(json_string)

# with open("100books.json", "r") as read_file:
#     print(json.load(read_file))

# import json
# import requests 

# response = requests.get("https://raw.githubusercontent.com/awasekhirni/jsondata/master/100books.json")   # get the data of the link
# books = json.loads(response.text)    # deserialize the text data of response and also loads the json data of response
# country_list = []
# for i in books:
#     if i['country'] not in country_list:
#         country_list.append(i['country'])


# print(country_list)

# print(dict1)
# print(type(books))
# country_name = list(filter(lambda x: x,books))
# print(country_name)

# print(type(books))
# print(books[0])
# print(type(books[0]))
# with open("country_sort.json", "w") as write_file:
#     json.dump(books, write_file, indent=3)
#     # print(books)
#     json_data = json.dumps(books, indent=3)
    
#     print(json_data)
# with open ("Country_sort.json", "r") as read_file:
#     print(json.load(read_file))

# empty_list = {}
# for k,v in json_data:
#     # print(k.keys())
#     new_book = k['country']
#     # print(type(new_book))
#     empty_list.append(new_book)
#     # print(v)
#     print(empty_list)
# # print(empty_list)
# # print(new_book)
# country_list =[]

# for c in empty_list:
#     if c not in country_list:
#         country_list.append(c)
# print("----------------------------------------------------------------")
# # print(country_list)

# print(sorted(country_list))

# country_name = {}


# dict1 = {'a':'apple','b':'ball','c':'cat'}
# dict1['d']='doll'
# dict1['e']='elephant'
# print(dict1)

# dict2=dict1.pop('a')
# print(dict1)
# print(dict2)

# dict2 = dict1.popitem()
# print(dict1)
# print(dict2)


# import json
# import requests

# urls = requests.get('https://raw.githubusercontent.com/awasekhirni/jsondata/master/100books.json')
# datas = json.loads(urls.text)

# temp_list = []
# # for i in dict1:
# #     country_list.append(i['country'])
# country_list = []
# country_sorted_list = []

# temp_list = [i['country'] for i in datas]
# # print(sorted(temp_list))
# country_list = set(temp_list)
# print(country_list)

# print(sorted(temp_list))
# for i in temp_list:
#     if i not in country_list:
#         country_list.append(i)
# print(sorted(country_list))


# import json
# import requests 
# import xlwt

# response = requests.get("https://raw.githubusercontent.com/awasekhirni/jsondata/master/100books.json")   # get the data of the link
# books = json.loads(response.text)    # deserialize the text data of response and also loads the json data of response

# books = {'a':'apple','b':'ball','c':'cat','d':'dog'}
# book = xlwt.Workbook(encoding = "utf-8")
# sheet1 = book.add_sheet("AssetsReport0")
# colunm_count = 0
# for country, value in books.items():
#     sheet1.write(0, colunm_count, country)
#     sheet1.write(1, colunm_count, value)
#     colunm_count += 1

# file_name = "test.xls"%()
# book.save(file_name)

# country_list = []
# for i in books:
#     if i['country'] not in country_list:
#         country_list.append(i['country'])

# print(country_list)
# pd.DataFrame(response).to_excel('JSON.xlsx')


# from openpyxl import Workbook
# import json
# import requests

# response = requests.get('https://raw.githubusercontent.com/awasekhirni/jsondata/master/100books.json')
# data = json.loads(response.text)
# country_list = []
# for i in data:
#     if i['country'] not in country_list:
#         country_list.append(i['country'])
# # print(country_list , type(country_list))
# # country_list[0] = False
# # print(country_list)
# for i in country_list:
#     if i == 'Nigeria' or i == 'Denmark' or i == 'United Kingdom':
#         i = "False"
#     print(i)

