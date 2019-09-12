def next_number(s):
    result = []
    i = 0
    while i < len(s):
        count = 1
        while i + 1 < len(s) and s[i] == s[i+1]:
            i += 1
            count +=1
        result.append(str(count) + s[i])
        i += 1
    return ''.join(result)


def nth_sequence(n, s):
    for i in range(n-1):
        s = next_number(s)
        return s

print(nth_sequence(4, '1'))
