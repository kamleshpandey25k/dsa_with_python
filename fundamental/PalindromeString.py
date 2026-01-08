
def isPalindrome(text):
    start=0
    end=len(text)-1;
    while start < end :
         if text[start] != text[end]:
             return False;
         start+=1;
         end-=1;
    return True;

n=input("You can enter").strip().replace(" ","").lower();
if isPalindrome(n):
    print("It is palindrome")

else:
    print("It is not palindrome")