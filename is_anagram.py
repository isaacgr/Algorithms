s1 = 'fairy talex'
s2 = 'rail safety'

# requires nlogn time (since any
# comparison based sorting algorithm requires this)
def bad_is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    print(sorted(s1) == sorted(s2))


def is_anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()
    ht = dict()

    if len(s1) != len(s2):
        return False

    for i in s1:
        if i in ht:
            ht[i] += 1
        else:
            ht[i] = 1

    for i in s2:
        if i in ht:
            ht[i] -= 1
        else:
            ht[i] = 1

    for i in ht:
        if ht[i] != 0:
            return False
    return True

print(is_anagram(s1, s2))
