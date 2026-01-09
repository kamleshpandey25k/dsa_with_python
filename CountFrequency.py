def countFrequency1(ar):
    freq =dict()
    for i in range(0,len(ar)):
        if ar[i] in freq:
            freq[ar[i]]+=1;
        else:
            freq[ar[i]]=1;
    return freq;
def countFrequency2(num):
    hash_map={};
    for i in range(0,len(num)):
        hash_map[num[i]]=hash_map.get(num[i],0)+1;
    return hash_map;

num=[1,2,3,4,5,6,7,8,9,5,4,2];
print(countFrequency2(num));
