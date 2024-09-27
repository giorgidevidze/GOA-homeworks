# Task Lambda 

tuples_list = [(1, 'banana'), (3, 'apple'), (2, 'orange')]

sorted_list = sorted(tuples_list, key=lambda x: x[1])

print(sorted_list)



numbers = [1, 2, 3, 4, 5]

squared_numbers = list(map(lambda x: x**2, numbers))

print(squared_numbers)



words = ['apple', 'dog', 'banana', 'cat', 'kiwi']

filtered_words = list(filter(lambda word: len(word) < 4, words))

print(filtered_words)



# Task Map

strings = ['hello', 'world', 'python', 'lambda']

uppercased_strings = list(map(lambda s: s.upper(), strings))

print(uppercased_strings)



numbers = [1, 2, 3, 4, 5]

added_numbers = list(map(lambda x: x + 5, numbers))

print(added_numbers)



words = ['apple', 'banana', 'cherry']

modified_words = list(map(lambda word: 'start' + word[0] + word[1:], words))

print(modified_words)



# Task Filter

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)



words = ['apple', 'banana', 'avocado', 'grape', 'apricot']

words_starting_with_a = list(filter(lambda word: word.lower().startswith('a'), words))

print(words_starting_with_a)



numbers = [10, -5, 3, -1, 0, 7, -8, 4]

positive_numbers = list(filter(lambda x: x >= 0, numbers))

print(positive_numbers)
