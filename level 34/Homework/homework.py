# Task 4

# NameError

name = "aplle"
try:
    print(frut)
except NameError:
    print("Error")


surname = "devidze"
try:
    print(name1)
except NameError:
    print("Error")


# IndexError

list1 = ["aplle", "mellon", 4, 6]
try:
    print(list1[4])
except IndexError:
    print("Error")

list2 = [5, 6, 2, 6, 7]
try:
    print(list2[6])
except IndexError:
    print("Error")

# TypeError
try:
  print(len(5))
except TypeError:
  print("Error")


try:
    a, b, c = "values"
except ValueError:
    print("Error")


# Task 5

def sum_mixed_list(mixed_list):
    valid_numbers = []

    for item in mixed_list:
        if isinstance(item, int):
            valid_numbers.append(item)
        elif isinstance(item, str) and item.isdigit():
            valid_numbers.append(int(item))
    
    return sum(valid_numbers)