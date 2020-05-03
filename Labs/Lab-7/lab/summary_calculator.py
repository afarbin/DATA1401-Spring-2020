import base as base
import classes as classes

from base import alg
from classes import grade

class summary_calculator(alg):
    def __init__(self,name):
        alg.__init__(self,name)

    def apply(self,a_student):
        raise NotImplementedError

class grade_summer(summary_calculator):
    def __init__(self):
        self.__prefix=''
        self.__n=0
        summary_calculator.__init__(self,"Sum Grades")
        
    def apply(self, **kwargs):
        a_student = kwargs["student"]
        grades = a_student.get_grades()
        
        exam = 'e'
        lab = 'l'
        quiz = 'q'
        
        labCount = 0
        quizCount = 0
        examCount = 0
        for key in grades.keys():
            if (key[0] == quiz and key[len(key) - 1] == 'n'):
                quizCount += 1
            if (key[0] == exam and key[len(key) - 1] == 'n'):
                examCount += 1
            if (key[0] == lab and key[len(key) - 1] == 'n'):
                labCount += 1
        
        self.__sum_grades_for_student_item_with_count__(a_student, exam, examCount)
        self.__sum_grades_for_student_item_with_count__(a_student, lab, labCount)
        self.__sum_grades_for_student_item_with_count__(a_student, quiz, quizCount)

    def __sum_grades_for_student_item_with_count__(self, a_student, item, count):
        for x in range(1,count + 1):
            self.__prefix = item + str(x) + "_"
            labels=[self.__prefix+str(x) for x in range(1,int(a_student[self.__prefix + "n"].value() + 1))]
            grade_sum=0.
            for label in labels:
                grade_sum+=a_student[label].value()
            a_student.add_grade(grade(self.__prefix+"sum",value=grade_sum))

