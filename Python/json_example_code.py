
# import json

# def sort_json_data(json_data):
#     sorted_data = sorted(json_data, key=lambda x: x.get('country'))
#     return sorted_data

# # Example JSON data (nested list of dictionaries)
# json_data = [
#     {"name": "John", "age": 30, "country": "USA"},
#     {"name": "Alice", "age": 25, "country": "Canada"},
#     {"name": "Bob", "age": 35, "country": "USA"},
#     {"name": "Emily", "age": 28, "country": "Australia"},
#     {"name": "David", "age": 40, "country": "Canada"}
# ]

# # Sorting the JSON data
# sorted_json_data = sort_json_data(json_data)

# # Printing sorted JSON data
# print(json.dumps(sorted_json_data, indent=4))


import json

def organize_data_by_country(json_data):
    organized_data = {}
    for item in json_data:
        country = item.get('country')
        if country not in organized_data:
            organized_data[country] = []
        organized_data[country].append({k: v for k, v in item.items() if k != 'country'})
    return organized_data

# Example JSON data (nested list of dictionaries)
json_data = [
    {"name": "John", "age": 30, "country": "USA"},
    {"name": "Alice", "age": 25, "country": "Canada"},
    {"name": "Bob", "age": 35, "country": "USA"},
    {"name": "Emily", "age": 28, "country": "Australia"},
    {"name": "David", "age": 40, "country": "Canada"}
]

# Organizing data by country
organized_data = organize_data_by_country(json_data)

# Printing organized data
print(json.dumps(organized_data, indent=4))
