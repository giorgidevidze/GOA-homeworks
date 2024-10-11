# Task 1

def dir_reduc(arr):

    #აქ გვაქვს Mapping, რომელიც ასახავს, რომელი მიმართულებებია ერთმანეთის საპირისპირო.
    opposites = {
        "NORTH": "SOUTH",
        "SOUTH": "NORTH",
        "EAST": "WEST",
        "WEST": "EAST"
    }

    #ეს არის ცარიელი სია, სადაც მოვინახავთ გადაწყვეტილებებს.
    stack = []

    #ვატარებთ თითოეულ მიმართულებას მიღებულ სიაში.
    for direction in arr:

        #თუ სტეკში უკვე არის ელემენტი და ის არის საპირისპირო მოქმედი მიმართულების, მაშინ ვშლით უკანასკნელს.
        # თუ არა, ახალი მიმართულება უნდა დაემატოს სტეკში.
        if stack and stack[-1] == opposites[direction]:
            stack.pop()
        else:
            stack.append(direction)
    
    # საბოლოოდ, ვაბრუნებთ სტეკში დარჩენილ ელემენტებს.
    return stack


# Task 3

def alphanumeric(password):
    #მეთოდი isalnum()აბრუნებს True-ს, თუ ყველა სიმბოლო ანბანურია, რაც ნიშნავს ანბანის ასოს (az) და ციფრებს (0-9).
    # სიმბოლოების მაგალითი, რომლებიც არ არის ანბანური: (ფართი)!#%&? და ა.შ.
    return password.isalnum()


# Task 4

def multiply_by_five(x):
    return x * 5

numbers = [1, 2, 3, 4, 5]

result = list(map(multiply_by_five, numbers))

print(result)



string_numbers = ["1", "2", "3"]

result = list(map(int, string_numbers))

print(result)



words = ["hello", "world", "python"]

result = list(map(lambda word: word + "!", words))

print(result)



import math

numbers = [1, 4, 9, 16, 25]

result = list(map(math.sqrt, numbers))

print(result)



numbers = [1, 2, 3, 4, 5, 6]

result = list(map(lambda x: f"{x} is even" if x % 2 == 0 else f"{x} is odd", numbers))

print(result)