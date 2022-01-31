'''30. WAP to print sorting order (ASC/DESC) of a given list'''
list=[23,45,12,90,55,33]
temp=0
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]<list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp

print(list) 




