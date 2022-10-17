a = '1', '2', '3', '4', '5', '6', '7', '8', '9'
spisok = []
for i in a:
    if '1 3 5 7 9'.find(i) % 2:
        spisok.append(int(i))
print(spisok)

