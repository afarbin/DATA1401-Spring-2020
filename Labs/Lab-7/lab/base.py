import numpy as np
import math

# Create some virtual classes
class base:
    __name=""
    
    def __init__(self,name):
        self.__name=name

    def name(self):
        return self.__name

class data(base):
    def __init__(self,name):
        base.__init__(self,name)
        
class alg(base):
    def __init__(self,name):
        base.__init__(self,name)
