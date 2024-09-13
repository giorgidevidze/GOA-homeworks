# Task 1

# ეს არი Name error
name = "giorgi"

try:
    print(surname)
except:
    print("Error")


# ეს არი index error
num = [1, 2, 3, 4]

try:
    print(num[5])
except:
    print("Error")


# type error
num = "1"
num1 = 3

try:
    print(num + num1)
except:
    print("Error")


# syntax error
name = "giorgi
try:
    print(name)
except SyntaxError:
    print("Error")


# Task 2
name = "giorgi"

try:
    print(name5)
except:
    print("Error")

# Task 3
num = [1, 2, 3, 4]

try:
    print(num[5])
except:
    print("Error")

# Task 4
myString = "Hello"
myList = ["World"]
try:
    myList.remove(myString)
except:
    print("Error")