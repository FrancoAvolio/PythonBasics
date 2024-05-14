from functools import reduce


def sum_one(value):
    return value + 1

def sum_two_values_and_one(first_value, second_value):
    return sum_one(first_value + second_value)

# print(sum_two_values_and_one(45,28))

#Closures#


def sum_ten():
    def add(value):
        return value + 10
    return add

add_closure = sum_ten()
print(add_closure(5))


numbers = [2,5,8,21,28]

def multiply_two (number):
    return number * 2


print(list(map(multiply_two, numbers)))
print(list(map(lambda number: number * 2, numbers)))



#Filter

def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False

print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


#Reduce

def sum_two_values (first_value, second_value):
    return first_value + second_value

print(reduce(sum_two_values, numbers))