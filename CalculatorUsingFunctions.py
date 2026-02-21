#making calculator using functions

first=int(input("enter first number"))
second=int(input("enter second number"))
c=input("enter the operation you want to perform")

def add(first,second):
    print("addition of given numbers is:" , first,second)

def multiply(first,second):
    print("multiplication of given numbers is:" , first*second)

def susecondstract(first,second):
    print("substraction of given numbers is:" , first-second)

def divide(first,second):
    print("division of given numbers is:" , first/second)

if(c=="+"):
    add(first,second)

elif(c=="*"):
    multiply(first,second)

elif(c=="-"):
    substract(first.second)

elif(c=="/"):
    divide(first.second)

else:
    print("error")