import json

data = {

        "coffee" : 200,

        "milk" : 300,

        "water" : 1000,
        
        "totalbalance" : 1000,

        "Espresso" : 50,

        "Americano" : 120,

        "Latte" : 200
        
        }


with open("materials.json", "w") as outfile:
    json.dump(data, outfile)

