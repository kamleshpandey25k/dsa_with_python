def missingNumber(num):
    start=min(num)
    end=max(num)
    
    # for i in range(start,end+1):
    #     if i not in num:
    #         return i
    # return 0
    n=len(num)
    count=end-start+1
    enum=count*(end+start)//2
    return enum-sum(num)
num=[10,11,12,13,14,16]
print(missingNumber(num))