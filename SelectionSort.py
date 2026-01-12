def selectionSort(num):
    n=len(num)
    for i in range(0,n):
        min_idx=i
        for j in range(i+1,n):
            if num[j] < num[min_idx]:
               min_idx=j
        num[i],num[min_idx]=num[min_idx],num[i]

num=[20,19,17,13,15,14]
selectionSort(num)
print(num)