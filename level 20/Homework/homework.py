# task 1

num1 = 21
num2 = 21

print(num1 + num2)


# task 2

# Concatenation is - In formal language theory and computer programming, string concatenation is the operation of joining character strings end-to-end. For example, the concatenation of "snow" and "ball" is "snowball". In certain formalisations of concatenation theory, also called string theory, string concatenation is a primitive notion.

num1 = "giorgi"
num2 = "devidze"

print(num1 + num2)


# task 3

num1 = 20
num2 = 2

print(num1 / num2)

#That is, the program does not know in advance that the answer will be an int, and that's why it produces a float


# task 4


num1 = 20
num2 = 25
print(num1 > num2)

num1 = 20
num2 = 25
print(num1 < num2)

num1 = 20
num2 = 25
print(num1 >= num2)

num1 = 20
num2 = 25
print(num1 <= num2)

num1 = 20
num2 = 25
print(num1 != num2)

num1 = 20
num2 = 25
print(num1 == num2)


# task 5


print(10 + 10 > 10 + 3)

print(10 + 10 < 10 + 3)

print(10 + 10 >= 10 + 3)

print(10 + 10 <= 10 + 3)

print(10 + 10 == 10 + 3)

print(10 + 10 != 10 + 3)


# task 6


True or False

False or True

True or True

False or False


True and False

False and True

True and True

False and False


# task 7


True or (5 > 10)

False or (10 > 21)

True or (5 <= 10)

False or (10 <= 21)

True and (5 >= 10)

False and (10 >= 21)

True and (5 <= 10)

False and (10 <= 21)





# task 8


for i in range(10):
    print(i)



# task 9


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum1 = 0

for i in list1:
    sum1 += i
    print(sum1)

    

# task 10

str1 = "Hello Word"

for i in str1:
    print(i)



# task 11


num = 1

while num < 10:
    print(num)
    num += 1



# task 12

num = 0

while num < 100:
    if num >= 50 and num <= 60:
        num += 1
    else:
        print(num)
        num += 1




# task 13

num = 0
sum1 = 50

while num < 1:
    sum1 = sum1 + num
    num = num + 1
    print(sum1)



# task 14

number = int(input("Enter your num: "))

def num(num1):
    if num1 % 5 == 0 and num1 % 3 == 0:
        print("iyofa oriveze")
    elif num1 % 3 == 0:
        print("iyofa 3ze")
    elif num1 % 5 == 0:
        print("iyofa 5ze")
    
num(number)



# task 15

def find_maximum(numbers):
    if not numbers: 
        return 
    return max(numbers)

test_case = [1, 3, 4, 5, 2]
max_output = find_maximum(test_case)
print("მაქსიმალური მნიშვნელობა:", max_output)



# task 16

def alternate_uppercase(s):
    result = ""
    for i in range(len(s)):
        if i % 2 == 0:
            result += s[i].upper()
        else:
            result += s[i]
    return result

test_string = "hello"
output = alternate_uppercase(test_string)
print( output) 


# task 17

def square_list(numbers):
    return [x**2 for x in numbers]

print(square_list([3, 12, 5, 2, 6]))


# task 18

str1 = "hello word"

print(str1.upper())


str1 = "hello word"

print(str1.lower())


str1 = "hello word"

print(str1.capitalize())


str1 = "hello peopel"

print(len(str1))


str1 = "hello giorgi"

print(str1.find("i"))


list1 = ["cat", "dog", "aplle",]

print(list1.index("aplle"))


list1 = [1, 2, 3, 4, 5, 6]

print(list1)
list1.append(12)
print(list1)


list1 = [1, 2, 3, 4, 5, 6]

print(list1)
list1.insert(12, "gio")
print(list1)


list1 = [1, 2, 3, 4, 5, 6]

print(list1)
list1.pop(4)
print(list1)


list1 = [1, 2, 3, 4, 5, 6]

print(list1)
list1.remove(2)
print(list1)