
my_original_list = [1, 35, 55, 55, 75]

my_list = [i + 1 for i in my_original_list] #my_original_list + 1
print(my_list)

def multiply_range():
    my_new_list = [1, 25, 44, 79]
    my_for = [i * 3 for i in my_new_list]
    if 237 in my_for:
        print("Hola")
    if 75 in my_for:
        print("Funciona normal")
    return my_for 

print(multiply_range())