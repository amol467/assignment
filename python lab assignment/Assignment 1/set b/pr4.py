# Python program to check armstrong number
num= int(input("Enter the number= "))
sum=0
temp=num
while temp>0:
    d=temp%10
    sum+=d**3
    temp//=10
if num==sum:
    print("The number is armstrong number")
else:

    print("The number is not a armstrong  number")