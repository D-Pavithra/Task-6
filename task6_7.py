a = list(input("Enter few numbers:"))
def ele(arr):
    ele_count = {}
    for element in arr:
        if element in ele_count:
            ele_count[element]+=1
        else:
            ele_count[element] = 1
    for element in arr:
        if ele_count[element] ==1:
            return element
    return none
result = ele(a)
print ("First non-repeating element is", result)