
def factorial(num):
    if num==0:
        return 1
    fact=1
    for i in range(1,num+1):
         fact=fact*i
    return fact
def factrRecursion(num):
    if num==1 or num==0:
     return 1
    return num* factrRecursion(num-1)

num=int(input("Enter the number"))
print(factrRecursion(num))

