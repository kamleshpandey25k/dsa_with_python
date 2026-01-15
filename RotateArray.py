def swap(num , i,j):
    while i < j :
     num[i],num[j]=num[j],num[i]
     i=i+1
     j=j-1
def rotateArray(num , k):
   n=len(num)
   k=k % n
   swap(num,0, n-1)
   swap(num,0,k-1)
   swap(num , k ,n-1 )
 
num=[10,20,30,40,50,60,70]
rotateArray(num,2)
print(num)