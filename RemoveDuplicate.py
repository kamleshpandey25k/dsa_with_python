def removeDuplicate(num):
    n=len(num)
    map_freq={}
    for i in range(0,n):
        map_freq[num[i]]=0
    j=0
    for k in map_freq:
        num[j]=k
        j=j+1
    print(num[:j])

def removeDuplicateOptimal(num):
    n=len(num)
    i=0
    j=i+1
    while j < n:
        if num[i] !=num[j]:
            i=i+1
            num[i],num[j]=num[j],num[i]
        j+=1

num=[10,10,22,3,3,4,5,22,5,4]
removeDuplicateOptimal(num)
print(num)