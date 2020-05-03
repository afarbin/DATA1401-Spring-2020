import numpy as np
import math

from calculator import calculator


class mean_std_calculator(calculator):
    def __init__(self):
        calculator.__init__(self,"Mean and Standard Deviation Calculator")

    def apply(self,a_grade_book,**kwargs):
        students = a_grade_book.get_students()
        exam = 'e'
        lab = 'l'
        quiz = 'q'

        labCount = 0
        quizCount = 0
        examCount = 0

        for key in students[0].get_grades().keys():
            if (key[0] == quiz and key[len(key) -1] == 'm'):
                quizCount += 1
            if (key[0] == exam and key[len(key) - 1] == 'm'):
                examCount += 1
            if (key[0] == lab and key[len(key) - 1] == 'm'):
                labCount += 1

        self.__calculate_mean_std__(a_grade_book, students, lab, labCount)
        self.__calculate_mean_std__(a_grade_book, students, quiz, quizCount)
        self.__calculate_mean_std__(a_grade_book, students, exam, examCount)

    def __calculate_mean_std__(self, gradebook, students, type, count):
        for x in range(1, count + 1):
            prefix = type + str(x) + "_"
            sum_label = prefix + "sum"
            grades = list()
            for student_i in students:
                grades.append(students[student_i][sum_label].value())
            gradebook[prefix + "Mean"] = np.mean(grades)
            gradebook[prefix + "STD"] = math.sqrt(np.var(grades))