list1 = [1, 2, 3, 4]

number = list(map(lambda a, : a + 1, list1))

print(number)


def create_sentence(*args):
    return ' '.join(args) + '.'

sentence = create_sentence("ეს", "არის", "მანქანა", "რომელიც", "მიყვარს", "BMW")
print(sentence)


def filter_bad_words(sentence, bad_words):
    words = sentence.split()
    filtered_sentence = ' '.join(word for word in words if word not in bad_words)
    return filtered_sentence


bad_words = {'ზარმაცი', 'მეზარება'}
sentence = "მე მეზარება ის საქმე, რადგან ზარმაცი ვარ."
filtered = filter_bad_words(sentence, bad_words)
print(filtered)


list1 = (1, 2, 3, 4, 5)
list2 = (6, 7, 8, 9, 2)

num = list(map(lambda a, b: a + b * 2, list1, list2))

print(num)