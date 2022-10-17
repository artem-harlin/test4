from functools import reduce
 
a = [17, 18, 19]
b = [['q', 'w', 'e'], ['r', 't'], ['z', 'x', 'c', 'v']]
c = list( reduce(lambda x, y: x + y, b) )
 
print(len(c), min(b, key=len), max(b, key=len), sorted(c))
