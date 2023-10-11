l1=[10, 501, 22, 37, 100, 999, 87, 351]
l2 =[]
l3 = set()
for i in l1:
    count =0
    for j in range (1,10):
        if i%j == 0:
            count=count+1
            if count>1:
                l3.add(i)
        if count ==1:
            l2.append(i)
print (l2)