# first approch 
def reverseArray(nums,i,j):
    while i<j:
        nums[i],nums[j]=nums[j],nums[i];
        i+=1
        j-=1
nums=[10,30,20,60,50,40]
print(nums)
#second approch
#reverseArray(nums,1,3)
print(nums)  
#third approch      
#nums.reverse()
nums[::-1]
print(nums)
