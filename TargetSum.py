def targetSum(nums, target):
    ans=[]
    for i in range(0,len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                ans.append(i)
                ans.append(j)
                return ans
    return ans
def targetSum2(nums,target):
    n=len(nums)
    hash_map={}
    for i in range(0,n):
        remaining=target-nums[i]
        if remaining in hash_map:
            return [hash_map[remaining],i]
        hash_map[nums[i]]=i

nums=[1,2,3,4,5,6,7]
print(targetSum2(nums,13))