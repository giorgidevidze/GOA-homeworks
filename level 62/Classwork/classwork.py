#  Task 1

def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)


#  Task 2

def print_student_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_student_info(name="John", age=20, grade="A", subject="Mathematics")


#  Task 3

def my_decorator(func):
    def wrapper():
        print("ფუნქცია შესრულებამდე")
        func()
        print("ფუნქცია დასრულდა")
    return wrapper

@my_decorator
def say_hello():
    print("გამარჯობა!")

say_hello()