first=input("enter the first number :")
operator=input("enter the operation you want to perform (+,-,*,/) :")
second =input("enter the second number")

if operator=="+":
    print(first+second)

elif operator=="*":
    print(first*second)

elif operator=="-":
    print(first-second)

elif operator=="/":
    print(first/second)

else:
    print("invalid operation")