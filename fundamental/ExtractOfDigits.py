n = int(input("Enter the number: "))
num = n
ans = 0

while num > 0:
    lastDigit = num % 10
    ans = ans * 10 + lastDigit
    num = num // 10

print("Reverse of the number is:", ans)
