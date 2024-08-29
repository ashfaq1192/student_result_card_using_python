#Result Card#
'''In this brief program I created result card of the student
on the basis of three subjects, Math, Physics, and chemistry
and in the end we get the total marks, percentage obtained and
grade obtained by the student'''

#STEPS#

#1. Getting input for student.
name:str= input("Enter your name: ")
roll_no:int = int(input("Enter your Roll No: "))
registration_no:int = int(input("Entr Registration No: "))
math_marks:float=float(input("Enter obtained marks in Mathematics:-"))
physics_marks:float=float(input("Enter obtianed marks in Physics:-"))
chemistry_marks:float=float(input("Enter obtianed marks in Chemistry:-"))

#2. calculating total marks
total_obtained_marks:float= math_marks+chemistry_marks+physics_marks

#maximum marks
maximum_marks:int=300

#3. calculating percentage
percentage:float=(total_obtained_marks/maximum_marks) * 100

#4. calcuation Grade
if percentage>=85:
    grade = 'A'
elif percentage>=70 and percentage <=84:
    grade = 'B'
elif percentage >=60 and percentage <=69:
    grade = 'C'
elif percentage >=40 and percentage <=59:
    grade = 'D'
else:
    print("You Failed the exam")

#5. Displaying Result Card

print("\n*****************************************")
print("*************BISE, Lahore******************")
print("___________________________________________")

print(f"\nName:             {name}")
print(f"Roll No:            {roll_no}")
print(f"Registration No:    {registration_no}")

print("\n\n____________________________________________")
print("      SUBJECT              OBTAINED MARKS  ")
print("--------------------------------------------")

print(f"\n        Mathematics           {math_marks}")
print(f"        Physics               {physics_marks}")
print(f"        Chemistry             {chemistry_marks}")

print("\n--------------------------------------------")
print(f"      TOTAL MARKS OBTAINED      {total_obtained_marks}")
print(f"      PERCENTAGE                {percentage}")
print(f"      OVERALL GRADE OBTAINED    {grade}")

print("_______________________________________________")
