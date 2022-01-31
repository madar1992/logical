'''20. WAP to count number of occurrences of search element.
Sample input:
list=[23,45,56,23,23,90,77]
search elements: 23
Expected output: 3'''

list=[23,45,56,23,23,90,77]
num=int(input("Enter a number to know nom of occurences in list "))
count=0
for i in list:
    if i==num:
        count=count+1
print("no of occurence of entered number is:",count)    

    