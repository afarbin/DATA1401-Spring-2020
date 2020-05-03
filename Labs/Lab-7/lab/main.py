import base as base
import classes as classes
import gradebook as gradebook
import csv_reader as csv_reader
import mean_std_calculator as mean_std_calculator
import summary_calculator as summary_calculator
from curved_letter_grade import curved_letter_grade
from final_grade_calculator import final_grade_calculator

from gradebook import grade_book
from classes import student
from classes import grade
from summary_calculator import grade_summer
from mean_std_calculator import mean_std_calculator

class_data= csv_reader.csv_reader("Data1401-Grades.csv")

a_grade_book=grade_book("Data 1401")

grade_summer = grade_summer()
mean_std_calculator = mean_std_calculator()
curved_grade_calc = curved_letter_grade()
final_grade_calc = final_grade_calculator()

for student_i in range(len(class_data)):
    a_student_0=student("Student",str(student_i),student_i)

    for k in class_data[student_i].keys():
        a_student_0.add_grade(grade(k,value=class_data[student_i][k]))

    a_grade_book.add_student(a_student_0)
    students = a_grade_book.get_students()
    a_grade_book.apply_calculator(grade_summer,
                                  student=students[student_i])

a_grade_book.apply_calculator(mean_std_calculator, a_grade_book = a_grade_book)
a_grade_book.apply_calculator(curved_grade_calc, gradebook = a_grade_book)
a_grade_book.apply_calculator(final_grade_calc, gradebook = a_grade_book, numberToDrop = 4)
a_grade_book.print_grade_calculations()


for student in a_grade_book.get_students():
    print()
    students[student].print_grades()
