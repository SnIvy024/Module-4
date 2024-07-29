# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.

exam_one = int(input("Input exam grade one: "))

exam_two = input("Input exam grade two: "))

exam_3 = str(input("Input exam grade three: "))

grades = [exam_one exam_two exam_three]
sum = 0
for grade in grade:
  sum = sum + grade

avg = sum / len(grdes)

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C'
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
elif:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

    print("Average: " + str(avg))

    print("Grade: " + letter_grade)

if letter-grade is "F":
    print "Student is failing."
else:
    print "Student is passing."


#Ivette Mujica
#CSS-225 Module 4
#Calculating Grades

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: ")) 

# Corrected input conversion to int

exam_three = int(input("Input exam grade three: ")) 

# Corrected input conversion to int

grades = [exam_one, exam_two, exam_three] 

# Corrected list syntax

total = 0 

# Changed variable name from 'sum' to 'total'

for grade in grades: 
    
     # Corrected loop variable name

    total += grade

avg = total / len(grades)  

# Corrected variable name

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:
    letter_grade = "B"
elif avg >= 70 and avg < 80:  
    # Corrected condition
    letter_grade = "C"
elif avg >= 60 and avg < 70:  
    # Corrected condition
    letter_grade = "D"
else:  # Changed `elif` to `else` for the final condition
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))

print("Average: " + str(avg))  

# Moved outside the loop

print("Grade: " + letter_grade)  

# Moved outside the loop

if letter_grade == "F":  
    
    # Corrected comparison operator

    print("Student is failing.")
else:
    print("Student is passing.")
