'''28. WAP to print unique elements in a given list
list=[23,45,65,90,45,23]
      output:    65 90'''
list=[23,45,65,90,45,23]
for i in range(len(list)):
    for j in range(i,len(list)):
        if list[i]==list[j]:
            print(list[i],end=" ")

