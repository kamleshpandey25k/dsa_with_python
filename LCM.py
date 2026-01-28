def lcm(n1,n2):
    max_value=max(n1,n2)
    while True :
        if max_value % n1 ==0 and max_value % n2 == 0 :
            break
        else :
            max_value+=1
    
    print(max_value)
lcm(2,10)
