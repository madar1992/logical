''' WAP to accept salary and 3 shopping bills from user and find 
   1. total shopping amount
   2. find how much % of amount he/she spent on shopping on his salary.'''
   
salary=float(input("Enter your salary "))
shop_bill1=float(input("Enter your shopping bill1 amount "))
shop_bill2=float(input("Enter your shopping bill2 amount "))
shop_bill3=float(input("Enter your shopping bill3 amount "))
total=shop_bill1+shop_bill2+shop_bill1;
percentage=total*100/salary;

print("total amount spent on shopping ",total)
print("percentage of amount spent on shopping from salary",percentage,"%")