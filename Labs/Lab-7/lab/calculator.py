from base import alg


class calculator(alg):
    def __init__(self,name):
        alg.__init__(self,name)

    def apply(self,a_grade_book):
        raise NotImplementedError
