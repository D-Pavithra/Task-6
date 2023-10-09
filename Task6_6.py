a = [23,234,56,78,345,2,45,78]
b = [2,234,5,78,45,2,45,78,90]
c = [23,2,24,56,8,35,21,4,78,756,242]
d = print(set(a))
e = print(set(b))
f = print(set(c))
g = d.union(e)
h = g.intersection(f)
print (h)