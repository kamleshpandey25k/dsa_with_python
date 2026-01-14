def isSorted(num):
    n=len(num)
    for i in range(0,n-1):
        if num[i]>num[i+1] :
            return False
    return True
num=[11,12,13,16,19,2]
print(isSorted(num))