# checking elegibility for 
age=int(input("Enter your age :"))
if age>=18:
    print(f"your age is {age} your elegible for vote")
    if age>50:
        print(f"your age is {age} you can vote at ground flour")
    else:
        print("you want to go to 1st flour to vote")
else:
    print("your not elegible for voteing")