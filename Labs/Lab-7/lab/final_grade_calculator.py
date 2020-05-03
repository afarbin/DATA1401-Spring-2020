import base as base
import classes as classes

from base import alg
from classes import grade

class final_grade_calculator(alg):
    GradeMap = {"A+": 12,
                "A": 11,
                "A-": 10,
                "B+": 9,
                "B": 8,
                "B-": 7,
                "C+": 6,
                "C": 5,
                "C-": 4,
                "D+": 3,
                "D": 2,
                "D-": 1,
                "F": 0}

    GradeMapR = {12: "A+",
                11: "A",
                10: "A-",
                9 : "B+",
                8 : "B",
                7 : "B-",
                6 : "C+",
                5 : "C",
                4 : "C-",
                3 : "D+",
                2 : "D",
                1 : "D-",
                0 : "F"
                }

    def __init__(self):
        self.__prefix=''
        self.__n=0
        alg.__init__(self, "Final Grade Calculator")
        
    def apply(self, **kwargs):
        gradebook = kwargs["gradebook"]
        numberToDrop = kwargs["numberToDrop"]

        students = gradebook.get_students()
        print(gradebook)
        exam = 'e'
        lab = 'l'
        quiz = 'q'

        for student in students:
            examGrades = self.__final_and_drop_grades_for_student_item__(students[student], exam)
            labGrades = self.__final_and_drop_grades_for_student_item__(students[student], lab)
            quizGrades = self.__final_and_drop_grades_for_student_item__(students[student], quiz)

            for i in range(numberToDrop):
                minVal = 99999999
                min = 0
                if (len(labGrades) == 0):
                    break
                for gradeVal in range(len(labGrades)):
                    if labGrades[gradeVal] < minVal:
                        minVal = labGrades[gradeVal]
                        min = gradeVal
                labGrades.pop(min)

            examTotal = 0
            labTotal = 0
            quizTotal = 0
            total = 0
            for eg in examGrades:
                examTotal += eg * .2
            for lab in labGrades:
                labTotal += lab
            for qz in quizGrades:
                quizTotal += qz
            total = (examTotal * .4) + (labTotal * .5) + (quizTotal * .1)

            total /= (len(examGrades) + len(labGrades) + len(quizGrades))
            total = round(total)

            if (total > 12) :
                total = 12

            final_grade = grade("FINAL_GRADE", value=self.GradeMapR[total][0])

            students[student].add_grade(final_grade)



    def __final_and_drop_grades_for_student_item__(self, a_student, item):
        items = []

        for grade in a_student.get_grades():
            if grade[0] == item and grade[len(grade) - 1] == 'd':
                items.append(grade)

        gradesVals = []
        for item in items:
            gradesVals.append(self.GradeMap[a_student[item].value()])
        return gradesVals