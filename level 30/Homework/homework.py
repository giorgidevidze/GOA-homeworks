# Task 1

my_dict = {
    "name" : "giorgi",
    "year" : 16,
    "citi" : "rustavi"
}

for key, value in my_dict.items():
    print(f"Key:{key}, value:{value}")


# Task 2

cars = [
    {
        "მოდელი":" BMW X5",
        "წელი": 2021,
        "ფასი": "45,000"
    },
    {
        "მოდელი": "Audi Q7",
        "წელი": 2022,
        "ფასი": "50,000"
    },
    {
        "მოდელი": "Mercedes-Benz GLE",
        "წელი": 2020,
        "ფასი": "47,500"
    }
]

for index, car in enumerate(cars, start=1):
    print(f"car {index}:")
    for key, value in car.items():
        print(f"  {key}: {value}")
    print()