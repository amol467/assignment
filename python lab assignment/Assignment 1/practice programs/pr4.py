# Pythom program to print all prime numbers in an interval
lower= int(input("Enter the starting number= "))
upper= int(input("Enter the ending number= "))
for n in range(lower,upper+1):
    for i in range(2,n):
        if n%i==0:
            break
    else:
            print(n,end=" ")