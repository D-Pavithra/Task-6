a = list(input("Enter few numnbers:"))
a.sort()
def minimum(a):
    if len(a)==0:
        return None
    return a[0]
mini = minimum (a)
if mini is not None:
    print("Minimum element in the list is:", mini)
else:
    print("It is an empty list")