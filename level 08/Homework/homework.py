# Task 1
print(20 != 25) # True
print(15 != 19) # True
print(25 != 25) # False

print(20 >= 10) # True
print(30 >= 35) # False
print(25 >= 15) # True

print(20 <= 10) # False
print(30 <= 35) # True
print(25 <= 15) # False

#Task 2
num1 = 20
num2 = 25
print(num1 == num2) # False
num1 = 20
num2 = 20
print(num1 == num2) # True
num1 = 25
num2 = 24
print(25 == 24) #False

num1 = 20
num2 = 25
print(num1 != num2) # True
num1 = 20
num2 = 20
print(num1 != num2) # False
num1 = 25
num2 = 24
print(25 != 24) # True

num1 = 20
num2 = 25
print(num1 >= num2) # False
num1 = 25
num2 = 20
print(num1 >= num2) # True
num1 = 25
num2 = 24
print(25 >= 24) # True

num1 = 20
num2 = 25
print(num1 <= num2) # True
num1 = 25
num2 = 20
print(num1 <= num2) # False
num1 = 25
num2 = 24
print(25 <= 24) # False

num1 = 20
num2 = 25
print(num1 > num2) # False
num1 = 20
num2 = 25
print(num1 > num2) # False
num1 = 25
num2 = 24
print(25 > 24) # True

num1 = 20
num2 = 25
print(num1 < num2) # True
num1 = 20
num2 = 25
print(num1 < num2) # True
num1 = 25
num2 = 24
print(25 < 24) # False

num1 = 20
num2 = 30
num3 = 25
num4 = 20
print(num1 > num2 and num3 < num4) # False
num1 = 20
num2 = 30
num3 = 25
num4 = 20
print(num1 < num2 and num3 > num4)  # True
num1 = 20
num2 = 30
num3 = 25
num4 = 20
print(20 < 30 and 25 > 20) # True

num1 = 20
num2 = 30
num3 = 25
num4 = 20
print(num1 > num2 or num3 < num4) # False
num1 = 20
num2 = 30
num3 = 25
num4 = 20
print(num1 < num2 or num3 < num4)  # True
num1 = 20
num2 = 30
num3 = 25
num4 = 20
print(20 < 30 or 25 > 20) # True

# Task 3
#And the rule of the operator is that if there is one mistake, then it outputs a lie. And if everything is true, it outputs the truth.
#Or the rules of the operator, if there is one truth in the errors, the terminal will output the truth. If everything is an error, then it will output a lie.

# Task 4
num1 = input()
num2 = input()
print(num1 > num2) # True
num1 = input()
num2 = input()
print(num1 > num2) # False
num1 = input()
num2 = input()
print(num1 < num2) # True
num1 = input()
num2 = input()
print(num1 < num2) # False