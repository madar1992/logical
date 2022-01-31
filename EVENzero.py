#WAP to accept number and check it is Even or odd or Zero
num=int(input("Enter a number to check EVEN or ODD or ZERO "))
if num%2==0 and num!=0 :
    print("Entered number is EVEN")
elif num%2!=0:
    print("Entered number is ODD")
else:
    print("Entered number is ZERO")