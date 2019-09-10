# Given two numbers, find their product using recusion

x = 5
y = 3

def recursive_product(x, y):
    # cuts down on recursive calls
    if y > x:
        return recursive_product(y, x)

    if y == 0:
        return 0
    return x + recursive_product(x, y-1)

print recursive_product(5,3)
