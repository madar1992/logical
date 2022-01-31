'''16. sum of even numbers and sum of odd numbers between 1-n'''
n=int(input("Enter a number to find sum of even and odd in that range"))
sum=0
sum1=0
for i in range(1,n+1):
    if i%2==0:
        sum=sum+i
    else:
        sum1=sum1+i
print("sum of even number is ",sum)
print("sum of odd number is ",sum1)        