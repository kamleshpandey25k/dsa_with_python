def sortWord(s1):
    s2 = s1.split(" ")
    for i in range(0, len(s2)):
        s2[i] = ''.join(sorted(s2[i]))

    print(type(s2))
    print(s2)

ss = "Hello every one What Are You Doing"
sortWord(ss)
