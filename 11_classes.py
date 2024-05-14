class Person:
        def __init__(self, name, surname):
                self.name = name
                self.surname = surname
                self.__fullname = f"{name} {surname}" #Privada
        def get_name (self):
               return self.__fullname
        def walk (self):
            print (f" {self.name} {self.surname} esta caminando!!")

my_person = Person("Franco", "Avolio")
print (f"Hola, mi nombre es {my_person.name}, mi apellido es {my_person.surname} y")
print(my_person.get_name())
my_person.walk()