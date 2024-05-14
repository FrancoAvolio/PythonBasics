sum_two_values = lambda first_value, second_value: first_value + second_value

print (sum_two_values(5,8))

multiply = lambda multiply_values, sum_two_values: sum_two_values * multiply_values

print (multiply(5,4))


def sum_three_values(values):
    return lambda first_value, second_value: first_value + second_value + values

print(sum_three_values(5)(2,4))
    

