def moveZero(nums):
    n=len(nums)
    idx=0
    for i in range(0,n):
        if nums[i] != 0:
         nums[idx]=nums[i]
         idx+=1
    while idx < n :
          nums[idx]=0
          idx+=1
nums=[2,0,4,6,0,6,0,7,7,3,0]
moveZero(nums)
print(nums)
    