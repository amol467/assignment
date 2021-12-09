# Python program to find the sum of natural numbers
lower= int(input("Enter the lower range= "))
upper= int(input("Enter the upper range= "))
sum=0
for i in range(lower,upper+1):
    sum+=i
print("Sum of natural numbers= ",sum)