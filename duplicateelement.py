'''27. WAP to print duplicate elements in a given list.
list=[23,45,65,90,45,23]
    output:  23  45'''

list=[23,45,65,90,45,23]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i]==list[j]:
            print(list[j],end=" ")
