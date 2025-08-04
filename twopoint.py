name =input("enter your name :")
is_palindrome=True
i=0
j=len(name)-1
while (i<=j):
    if name[i]!=name[j]:
        is_palindrome=False
    i+=1
    j-=1
   
if is_palindrome==True:
    print("your name is palindrome")
else:
    print("your name is not palindrome")
