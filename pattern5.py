'''25. WAP to print following patten.
10 11 12 13 14
90 89 88 87 86 
15 16 17 18 19
85 84 83 82 81
20 21 22 23 24 '''
count=9
count1=89
for i in range(5):
    for j in range(5):
        if i%2==0:
            count=count+1
            print(count,end=" ")
        else:
            count1=count1+1
            print(count1,end=" ")
    print()    
