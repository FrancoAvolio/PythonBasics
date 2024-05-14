import numpy
import requests

numpy_array = numpy.array([35,11,45,88,121,22])
print(numpy_array * 3)

response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
# print(response)
# print(response.json())

from arithmetics import sum

print(sum(16,28))