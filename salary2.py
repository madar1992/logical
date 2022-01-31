''' WAP to accept basic salary and find gross salary.
  Gross_salary= basic+HRA+DA
    if basic salary <10000
          DA is 70% on basic
          HRA is 65% on basic 
   basic salary is between 10000 to 20000
         DA is 75% on basic
         HRA is 73% on basic
   basic salary above 20000
         DA is 80% on basic
          HRA is 76% on basic'''
basicsal=float(input("Enter your basic salary"))
if basicsal<10000:
    DA=70*basicsal/100;
    HRA=65*basicsal/100;
    Gross_salary=basicsal+HRA+DA;
    print("YOUR GROSS SALARY IS ",Gross_salary)
elif basicsal>10000 and basicsal<20000:
    DA=75*basicsal/100;
    HRA=73*basicsal/100;
    Gross_salary=basicsal+HRA+DA;
    print("YOUR GROSS SALARY IS ",Gross_salary)
else:
    DA=80*basicsal/100;
    HRA=76*basicsal/100;
    Gross_salary=basicsal+HRA+DA;
    print("YOUR GROSS SALARY IS ",Gross_salary)