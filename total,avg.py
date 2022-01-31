#2 WAP to accept 3 subjects marks and print total marks and avg marks.
math_marks=int(input("Enter your math_marks= "));
physic_marks=int(input("Enter your physic_marks= "));
chemistry_marks=int(input("Enter your chemistry_marks= "));

total_marks=(math_marks+physic_marks+chemistry_marks);
avg=total_marks/3;
print("the total marks are= ",total_marks);
print("the average marks are= ",avg);
