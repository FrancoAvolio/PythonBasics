import os

txt_file = open("./my_file.txt", "r+")

# print(txt_file.read())

import json

json_file = open("./my_file.json", "w+")

json_test = {
    "Nombre": "Franco",
    "Apellido": "Avolio",
    "Edad":"22",
    "Lenguajes":"Python",
}
 
json.dump(json_test, json_file)