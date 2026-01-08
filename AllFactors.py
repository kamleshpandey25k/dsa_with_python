from math import sqrt
def findAllFactorsM1(n):
    factors=[]
    for i in range(1,(n//2)+1):
      if n%i==0:
       factors.append(i); 
    factors.append(n);
    return factors;
# optimize
def findAllFactorsM2(n):
   factors=[];
   for i in range(1,int(sqrt(n)+1)):
       if n%i==0:
          factors.append(i);
       if n//i !=i:
          factors.append(n//i);
   factors.sort();
   return factors;
n=int(input("Enter the number"));

for x in findAllFactorsM2(n):
   print(x);    