a = [10, 20, 30, 9]
sumvalue = 59
def sums(lst, total):
    n = len(lst)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if lst[i]+lst[j]+lst[k] == total:
                    return [lst[i], lst[j], lst[k]]
    return None
triplet_sum = sums(a, sumvalue)
if triplet_sum:
    print(f"Triplet with sum {sumvalue}: {triplet_sum}")
else:
    print("No triplet found")