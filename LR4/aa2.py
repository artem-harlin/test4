a, b = map(int, input("a, b = ").split())
lst = [a]
for i in range(1, 10):
    lst.append(a + i * b)
print(*lst)
