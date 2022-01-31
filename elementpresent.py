'''19. WAP to search given element is present in list or not'''
list=[23,45,56,23,23,90,77]
num=int(input("Enter a number to check weather it is present in the list or not "))
for i in list:
    if i==num:
        print("Number present in the list")
        break
else:
    print("Number is not present in the list")