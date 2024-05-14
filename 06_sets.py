my_set = set()
print (type(my_set))

my_other_set = {"Franco", "Avolio", 22}
my_new_set = {"Meg", "Meg", 25}
my_full_set = my_other_set.union(my_new_set) # Se juntan de manera desordenada
print(my_full_set)
my_other_set.add("FrancoAvolio") #Lo guarda desordenadamente No admite repetidos

print(my_other_set)

print ("Franco" in my_other_set) #Realizar una busqueda > True
print ("Franquito" in my_other_set) #Realizar una busqueda > False
