n = [10, 501, 22, 37, 100, 999, 87, 351]
def happynum(num):
    a = set()
    while num !=1 and num not in a:
        a.add(num)
        num = sum(int(digit)**2 for digit in str (num))
    return num==1
happy_numbers = [ num for num in n if happynum(num)]
count = len(happy_numbers)
print ("Happy numbers in the list are:", happy_numbers)
print ("Count for happy numbers:", count)