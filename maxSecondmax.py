'''18. WAP to accept 6 values and find max and second max value'''
max=0
max1=0
for i in range(6):
    num=int(input("Enter a number"))
    if num>max:
        max1=max
        max=num
    elif num>max1:
        max1=num
print("first maximum number is: ",max)
print("second maximum number is: ",max1)

        
        