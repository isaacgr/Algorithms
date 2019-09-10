# Given a string, count the number of consonants

input_1 = 'abc de'
input_2 = 'LuCiDProgrAmMiNg'

vowels = 'aeiou'

def iterative_count(input_str):
    count = 0
    for i in range(len(input_str)):
        if input_str[i].lower() not in vowels and input_str[i].isalpha():
            count += 1
    return count

def recursive_count(input_str):
    if input_str == '':
        return 0
    if input_str[0].lower() not in vowels and input_str[0].isalpha():
        return 1 + recursive_count(input_str[1:])
    else:
        return recursive_count(input_str[1:])

print iterative_count(input_1)
print iterative_count(input_2)

print recursive_count(input_1)
print recursive_count(input_2)




