n=int(input("Enter the number"))
num=n
countDigits=0
while num>0:
    num=num//10;
    countDigits+=1;
print(countDigits);