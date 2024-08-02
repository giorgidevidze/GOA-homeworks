# task 1


def manual_min(lst):
    return min(lst)

print(manual_min([5, 1, 9, -3, 2]))  
print(manual_min([10, 20, 30]))      


# task 2

def manual_max(lst):
    return max(lst)

print(manual_max([5, 1, 9, -3, 2]))  
print(manual_max([10, 20, 30]))  


# task 3

def manual_len(list1):
    return len(list1)

print(manual_len([5, 1, 9, -3, 2]))  
print(manual_len([10, 20, 30, 88, 33,])) 


# task 4

def manual_sum(list2):
    return sum(list2)

print(manual_sum([5, 1, 9, 3, 2]))  
print(manual_sum([10, 20, 30, 88, 33,])) 


# task 5

def manual_replace(string, replace_value, replace_with):
    result = ""

    for i in range(len(string)):
        if string[i] == replace_value:
            result += replace_with
        else:
            result += string[i]

    print(result)

manual_replace("hello word", "o", "d")


# task 6

def manual_find(string, find_value):

    for i in range(len(string)):
        if string[i] == find_value:
            print(i)
        else:
            pass

manual_find("hello word", "r")