import base as base
import numpy as numpy
from base import data


class grade(data):
    __value=0
    __numerical=True
    __gradebook_name=str()
    __letter_grades=["F-","F","F+","D-","D","D+","C-","C","C+","B-","B","B+","A-","A","A+"]
    
    def __init__(self,name,numerical=True,value=None):
        if value:
            if isinstance(value,(int,float)):
                self.__numerical=True
            elif isinstance(value,str):
                self.__numerical=False
            self.set(value)
        else:
            self.__numerical=numerical
        self.__gradebook_name=name
        data.__init__(self,name+" Grade Algorithm")

    def set(self,value):
        if isinstance(value,(int,float)) and self.__numerical:
            self.__value=value
        elif isinstance(value,str) and not self.__numerical:
            if value in self.__letter_grades:
                self.__value=value
        else:
            print (self.name()+" Error: Bad Grade.")
            raise Exception
    
    def value(self):
        return self.__value
    
    def numerical(self):
        return self.__numerical
    
    def gradebook_name(self):
        return self.__gradebook_name
    
    def __str__(self):
        return self.__gradebook_name+": "+str(self.__value)

class student(data):
    __id_number=0
    __grades=dict()
    
    def __init__(self,first_name, last_name,id_number):
        self.__id_number=id_number
        self.__grades=dict()
        data.__init__(self,first_name+" "+last_name+" Student Data")

    def add_grade(self,a_grade,overwrite=False):
        if overwrite or not a_grade.gradebook_name() in self.__grades:
            self.__grades[a_grade.gradebook_name()]=a_grade
        else:
            print (self.name()+" Error Adding Grade "+a_grade.name()+". Grade already exists.")
            raise Exception

    def id_number(self):
        return self.__id_number
    
    def __getitem__(self,key):
        return self.__grades[key]
    
    def get_grades(self):
        return dict(self.__grades)
    
    def print_grades(self):
        for grade in self.__grades:
            print (self.__grades[grade])
    
