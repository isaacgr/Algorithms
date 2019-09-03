# Given a string, find the first uppercase character.
# Solve with iterative and recursive solution

str_1 = 'lucidProgramming'
str_2 = 'LucidProgramming'
str_3 = 'lucidprogramming'


def find_uppercase_iterative(input_str):
    for char in range(len(input_str)):
        if input_str[char].isupper():
            return input_str[char]
    return 'No uppercase char found'

def find_uppercase_recursive(input_str, index=0):
    if input_str[index].isupper():
        return input_str[index]
    if index == len(input_str) - 1:
        return 'No uppercase char found'
    return find_uppercase_recursive(input_str, index+1)


print find_uppercase_iterative(str_1)
print find_uppercase_iterative(str_2)
print find_uppercase_iterative(str_3)

print find_uppercase_recursive(str_1)
print find_uppercase_recursive(str_2)
print find_uppercase_recursive(str_3)
