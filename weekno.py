'''WAP to accept week_number and print weekday
    1 -- monday
    2. tuesday
    7 sunday'''
num=int(input("Enter a number to know day of the week"))
if num==1:
    print("monday")
elif num==2:
    print("tuesday")
elif num==3:
    print("wednesday")    
elif num==4:
    print("thursday")
elif num==5:
    print("friday")
elif num==6:
    print("saterday")
elif num==7:
    print("sunday") 
else:
    print("user entered a invaild number")