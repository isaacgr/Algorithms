# Given a string, calculate the length

input_str = 'LucidProgramming'

print(len(input_str))

def iterative_str_len(input_str):
    count = 0
    for char in input_str:
        count += 1
    return count

def recursive_str_len(input_str):
    if input_str == '':
        return 0
    return 1 + recursive_str_len(input_str[1:])

print iterative_str_len(input_str)
print recursive_str_len(input_str)
