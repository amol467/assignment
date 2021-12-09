# Python program to find armstrong number in an interval
lower= int(input("Enter lower range="))
upper= int(input("Enter upper range="))
for num in range(lower,upper+1):
    sum=0
    temp=num
    while temp>0:
        d= temp%10
        sum+=d**3
        temp//=10
    if sum==num:
        print(num,end=" ")
