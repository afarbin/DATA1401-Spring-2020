import base as base
import classes as classes

from base import data

class grade_book(data):
  # New member class to hold arbitrary data associated with the class

  __data=dict()
  __students=dict()
  
  def __init__(self,name):
      data.__init__(self,name+" Course Grade Book")
      self.__students=dict()
      self.__data=dict()
      
  # New method to access data
  def __getitem__(self,key):
      return self.__data[key]
          
  # New method to add data
  def __setitem__(self, key, value):
      self.__data[key] = value
      
  def add_student(self,a_student):
      self.__students[a_student.id_number()]=a_student

  def getData(self):
    return self.__data
  # New method to allow iterating over students
  def get_students(self):
      return self.__students
  
  def assign_grade(self,key,a_grade):
      the_student=None
      try:
          the_student=self.__students[key]
      except:
          for id in self.__students:
              if key == self.__students[id].name():
                  the_student=self.__students[id]
                  break
      if the_student:
          the_student.add_grade(a_grade)
      else:
          print (self.name()+" Error: Did not find student.")
          
  def apply_calculator(self,a_calculator,**kwargs):
    a_calculator.apply(**kwargs)

  def print_grade_calculations(self):
    grades = [];
    for item in self.__data:
        itemName = item[:item.find('_')]
        if itemName not in grades:
            grades.append(itemName)
    print("-----------------------------")
    print("| Grade \t| Mean \t| STD \t|")
    print("-----------------------------")
    for item in grades:
        print("| "+ item + " \t|\t" + str(round(self.__data[item + "_Mean"],2)) + " \t | \t" + str(round(self.__data[item + "_STD"],2)) + " |")
    print("-----------------------------")