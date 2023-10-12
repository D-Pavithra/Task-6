a = [4, 2, -3, 1, 6]
def sums(arr):
    b= 0
    s = set()
    for num in arr:
        b +=num
        if b == 0 or b in s:
            return True
        s.add(b)
    return False
if sums(a):
    print ("subarray with 0 sum exists")
else:
    print ("Subarray with 0 sum does not exist")