from calculator import calculator
from classes import grade


class uncurved_letter_grade_percent(calculator):
   __grades_definition=[ (.97,"A+"),
                         (.93,"A"),
                         (.9,"A-"),
                         (.87,"B+"),
                         (.83,"B"),
                         (.8,"B-"),
                         (.77,"C+"),
                         (.73,"C"),
                         (.7,"C-"),
                         (.67,"C+"),
                         (.63,"C"),
                         (.6,"C-"),
                         (.57,"F+"),
                         (.53,"F"),
                         (0.,"F-")]
   __max_grade=100.
   __grade_name=str()
   
   def __init__(self,grade_name,max_grade=100.):
       self.__max_grade=max_grade
       self.__grade_name=grade_name
       calculator.__init__(self,
                                 "Uncurved Percent Based Grade Calculator "+self.__grade_name+" Max="+str(self.__max_grade))
       
   def apply(self,a_grade_book,grade_name=None,**kwargs):
       if grade_name:
           pass
       else:
           grade_name=self.__grade_name
           
 
       for k,a_student in a_grade_book.get_students().iteritems():
           a_grade=a_student[grade_name]

           if not a_grade.numerical():
               print (self.name()+ " Error: Did not get a numerical grade as input.")
               raise Exception
   
           percent=a_grade.value()/self.__max_grade
       
           for i,v in enumerate(self.__grades_definition):
               if percent>=v[0]:
                   break
                           
           a_student.add_grade(grade(grade_name+" Letter",value=self.__grades_definition[i][1]))

