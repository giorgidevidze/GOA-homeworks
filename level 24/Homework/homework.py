# task 1

def arithmetic_mean(numbers):
    return sum(numbers) / len(numbers) if numbers else None

numbers_list = [10, 20, 30, 40, 50]
print(arithmetic_mean(numbers_list))  


#  task 2

def manual_abs(x):
    return x if x >= 0 else -x

print(manual_abs(-5)) 
print(manual_abs(3))


# task 3


def remove_duplicates(lst):
    return list(set(lst))

input_list = [1, 2, 3, 1]
print(remove_duplicates(input_list))
