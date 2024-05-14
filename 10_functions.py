def my_function ():
    print("Hola Mundo")
    if not my_function:
        print("holakease")
    else: print("hola ke ase")
my_function()


def sum_two_values (a , b):
    print(a+b)
    if a+b > 15:
        print("wtf?")
sum_two_values(4,25)


def sum_two_values_with_return (first, second):
    return first + second

my_result = sum_two_values_with_return(44, 26) # con return hay que guardar en una variable
print (my_result) # > 70


