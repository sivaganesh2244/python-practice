# palindrome check program
name=input("enter your name :")
rev_name=name[::-1]
if name==rev_name:
    print("your name is palindrome")
else:
    print("your name is not palindrome")