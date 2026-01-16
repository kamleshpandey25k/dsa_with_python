def targetElement(nums, target):
     n=len(nums)
     for i in range (0,n):
          if nums[i] == target :
               return i
     return -1
nums=[10,20,30,50,90]
print(targetElement(nums, 30))