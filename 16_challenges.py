#Fizz Buzz#


def fizzbuzz():
    for i in range(101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
# fizzbuzz()

#check anagrama
def anagrama(word_one, word_two):
     if word_one.lower() == word_two.lower():
      return False
     if sorted(word_one.lower()) != sorted(word_two.lower()):
      return False
     return sorted(word_one.lower()) == sorted(word_two.lower())

print(anagrama("amor", "roma"))
 

def fibonacci ():
    prev_number = 0
    next_number = 1
    for i in range(0,51):
        print(prev_number)
        fib = prev_number + next_number
        prev_number = next_number
        next_number = fib

fibonacci()

def numero_primo():
    for number in range(1, 101):
        if number >= 2:
            is_divisible = False
            for index in range(2, number):
                if number % index == 0:
                    is_divisible = True
                    break
            if not is_divisible:
                print(number)
 
numero_primo()


def reverse(text):
    text_len = len(text)
    reversed_text = ""
    for i in range(0, text_len):
        reversed_text += text[text_len - i - 1]
    return reversed_text

print (reverse("Hola Mundo"))