a = [10 , 501, 22, 37, 100, 999, 87, 351]
b=[]
c=[]
for i in a:
    if (i%2==0):
        b.append(i)
    else:
        c.append(i)
print(b)
print(c)