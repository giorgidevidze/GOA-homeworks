# task 1

guess = int(input("Enter your guess: "))
num = 4

if guess == 1:
    print("It's incorrect")
elif guess == 2:
    print("It's incorrect")
elif guess == 3:
    print("It's incorrect")
elif guess == 4:
    print( "It's correct")
elif guess == 5:
    print("It's incorrect")
else:
    print("It's incorrect")

# task 2

sum = 0
for num in range (1, 100,) :
    print(num)
    sum = sum+num
print(sum)

# task 3

sum = 0

for num in range(1000):
    if num >= 500 and num <= 600:
        continue
    else:
        sum += num
    
print(sum)

# task 4
guess = int(input("Enter your guess: "))
num = 4

while num == 4:
    if guess == 1:
      print("It's incorrect")
      num = num + 1
    elif guess == 2:
      print("It's incorrect")
      num = num + 1
    elif guess == 3:
      print("It's incorrect")
      num = num + 1
    elif guess == 4:
      print( "It's correct")
      num = num + 1
    elif guess == 5:
      print("It's incorrect")
      num = num + 1
    elif guess == 6:
      print("It's incorrect")
      num = num + 1
    elif guess == 7:
      print("It's incorrect")
      num = num + 1
    elif guess == 8:
      print("It's incorrect")
      num = num + 1
    elif guess == 9:
      print("It's incorrect")
      num = num + 1
    elif guess == 10:
      print("It's incorrect")
      num = num + 1
    else:
      print("It's incorrect")
      num = num + 1

# task 5

num = 1
num_sun = 1

while num < 10:
    num_sun = num_sun * num
    num = num + 1

print(num_sun)

# task 6

num = int (input ("Enter any number to test whether it is odd or even: "))

if (num % 2) == 0:
   print ("The number is even")
else:
   print ("The provided number is odd")

# task 7 

user_grade = int(input("Enter your grade: "))

if user_grade >= 90:
    print("A")

elif user_grade >= 80 and user_grade <= 89:
    print("B")

elif user_grade >= 70 and user_grade <= 79:
    print("C")

elif user_grade >= 60 and user_grade <=69:
    print("D")

else:
    print("F")
