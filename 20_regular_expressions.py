import re
import numpy


my_string = "Esta es la leccion numero 20 Leccion"
my_new_string = "Esta no es la leccion numero 21"

match = re.match("Esta es la leccion", my_string)
if match is not None:
    print(match)
    start, end = match.span() 
    print(my_string[start:end])
    print(re.match("Esta es la leccion", my_new_string))


print(re.split("20", my_string))

my_subbed_string = re.sub("Esta", "esta", my_string)
print(my_subbed_string)
 
pattern = r"[lL]eccion"
print(re.findall(pattern, my_string))