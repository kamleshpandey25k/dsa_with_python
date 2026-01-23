def reArrange(nums):
    p=0
    n=1
    result=[0]*len(nums)
    for i in range(0,len(nums)):
        if nums[i] >=0:
            result[p]=nums[i]
            p+=2
        if nums [i]<0 :
            result[n]=nums[i]
            n+=2
    print(result)
    return result
nums=[5,-10,-20,8,-4,9,78]
reArrange(nums)
