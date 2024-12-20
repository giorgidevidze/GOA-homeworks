# Task 1

class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def go(self):
        print(f"{self.brand} is going.")

    def stop(self):
        print(f"The {self.brand} {self.model} has stopped.")

car1 = Car("Toyota", "Corolla", 2020, "Red")

print("Car")
car1.go()
car1.stop()


#  Task 2

class Person:
    total_people = 0
    
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
        Person.total_people += 1

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Job: {self.job}")
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I work as a {self.job}.")

person1 = Person("Alice", 30, "Engineer")

print("Person 1 Information:")
person1.display_info()
person1.greet()


#  Task 3

# dunder method - არის რომელიც იწერება ორი ქვედა ტირით და შუაში იწერება მეთოდი მაგალითად: __init__


#  Task 4

# instance variables - არის ესენი:  self.name = name 


#  Task 5

# Class variebls - არის ცვლადები, რომლებიც განსაზღვრულია კლასში და აქვთ ერთნაირი მნიშვნელობა ყველა ამ კლასის ობიექტისთვის. ისინი გამოიყენება მონაცემების შენახვისთვის, რომლებიც უნდა იყოს საერთო ყველა ობიექტისთვის, და არა ინდივიდუალური თითოეული ობიექტისთვის.


#  Task 6

# Blueprint - (ხშირად ითარგმნება როგორც "პროექტი" ან "გეგმა") არის კონცეფცია, რომელიც გამოიყენება იმ გაორმაგებული, წინასწარ განსაზღვრული სტრუქტურის გამოსახატად, რომელიც ქმნის ან მოიცავს რაიმე ტიპის კონცეფციებს, დიზაინებს ან სისტემებს. პროგრამირების კონტექსტში, blueprint ხშირად გამოიყენება იმის აღსანიშნავად, რომ: