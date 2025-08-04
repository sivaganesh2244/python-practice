#checking the name of a prson name starting and ending with same character or not
name=input("enter your name :")
first_chr=name[0]
last_chr=name[len(name)-1]
if first_chr==last_chr:
    print("you are name has same starting and ending characters")
else:
    print("your name has different starting and ending characters")