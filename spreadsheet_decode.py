def spreadsheet_decode(col):
    num = 0
    count = len(col) - 1
    for s in col:
        num += 26**count * (ord(s) - 64)
        count -= 1
    return num

print spreadsheet_decode('A')
print spreadsheet_decode('B')
print spreadsheet_decode('AB')
