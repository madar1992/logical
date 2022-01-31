'''WAP to accept basic salary and find gross salary.
 Gross_salary= basic+HRA+DA
 DA is 80% on basic
 HRA is 76% on basic'''
 
basic_salary=float(input("Enter your basic salary"))
DA=80*basic_salary/100;
HRA=76*basic_salary/100;
Gross_salary=basic_salary+HRA+DA;
print("The gross salary is ",Gross_salary)