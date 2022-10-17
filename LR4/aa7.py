a = input().split()
c = 0
v = []
b = 0
for i in a:
    if i not in v:
        c += 1
        v.append(i)
    else:
        b += 1
print(c)


