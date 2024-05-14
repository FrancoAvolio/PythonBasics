my_list = [1, 35, 55, 55, 75]
my_dict = {"Nombre": "Franco", "Apellido": "Avolio", "Edad":"22", 1: "Python"}
for element in my_list: #For con List.
    print(element)

# For con Dicts.
for element in my_dict:
    print(element)
    if element == "Nombre":
        break
    print("Se ejecuta")
else: print("No funciona")