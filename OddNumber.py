count=0
odd=1
# while count <10 :
#       print(odd)
#       odd+=2
#       count+=1
l1=[]
while True:
    if count <10:
        print(odd)
        l1.append(odd)
        odd+=2
        count+=1
    else :
        break
l1.reverse()
print(l1)