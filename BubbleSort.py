def bubbleSort(num):
    n=len(num)
    for i in range(n-1):
        for j in range(n-1-i):
            if num[j]>num[j+i]:
                num[j],num[j+1]=num[j+1],num[j]

num=[10,20,30,80,70,90]
bubbleSort(num)
print(num)

