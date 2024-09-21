# Task 2

# Python-ის map()ფუნქცია იყენებს ფუნქციას iterable-ის (მაგ. სიის) ელემენტებზე, საშუალებას აძლევს დაბრუნდეს ახალი iterable, ძირითადი ელემენტი ფუნქციის გამოყენების შედეგია. ეს არის მთავარი, რაც map()სასარგებლოა, როდესაც გსურთ ოპერაციების გაძლიერება ყველა ელემენტზე.

numbers = [1, 2, 3, 4]
result = list(map(lambda x: x + 1, numbers))
print(result)


# Task 3

#filter()ფუნქცია Python-ში გამოიყენებაTrueანFalse, და `filter()არჩევანისTrue-ს ა
numbers = [1, 2, 3, 4, 5, 6]
result
list(filter(lambda x: x % 2 == 0, numbers))
print(result)


# Task 4

lists = [1, 2, 3],[4, 5, 6],[7, 8, 9]

averages = []
for lst in lists:
    avg = sum(lst) / len(lst)      
    averages.append(avg)

print(averages)


lists2 = [5, 2, 7],[12, 11, 6],[9, 1, 10]

averages2 = []
for lst in lists2:
    avg = sum(lst) / len(lst)      
    averages2.append(avg)

print(averages2)



# Task 5

products = {
    "ლობიო": True,
    "პომიდორი": False,
    "ბოსტნეული": True,
    "კარტოფილი": False,
    "ხახვი": True,
}

out_of_stock = dict(filter(lambda item: not item[1], products.items()))

print(out_of_stock)