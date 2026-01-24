def printDigonalTringle(nums):
    for i in range(0,(len(nums))):
        for j in range (0,len(nums[0])):
            if i==j:
                print(nums[i][j],end=" ")
        print("")
nums=[[1,2,3],[4,5,6],[7,8,9]]
printDigonalTringle(nums)
