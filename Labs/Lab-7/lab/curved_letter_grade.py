from calculator import calculator
from classes import grade


class curved_letter_grade(calculator):
    __grades_definition = [(.97, "A+"),
                           (.93, "A"),
                           (.9, "A-"),
                           (.87, "B+"),
                           (.83, "B"),
                           (.8, "B-"),
                           (.77, "C+"),
                           (.73, "C"),
                           (.7, "C-"),
                           (.67, "C+"),
                           (.63, "C"),
                           (.6, "C-"),
                           (.57, "F+"),
                           (.53, "F"),
                           (0., "F-")]

    def __init__(self):
        calculator.__init__(self, "Curved Percent Based Grade Calculator")

    def apply(self, **kwargs):
        gradebook = kwargs["gradebook"]

        grades = []

        students = gradebook.get_students()

        for item in gradebook.getData():
            itemName = item[:item.find('_')]
            if itemName not in grades:
                grades.append(itemName)


        for gradeO in grades:
            for student in students:
                max_grade = students[student][gradeO + "_n"].value() * 10.
                std_dev = gradebook[gradeO + "_STD"]
                mean = gradebook[gradeO + "_Mean"]
                overall_grade = students[student][gradeO + "_sum"]
                percent = overall_grade.value() / max_grade
                shift_to_zero = percent - (mean / max_grade)
                if shift_to_zero == 0:
                    scale_std = 0
                    scaled_percent =  students[student][gradeO + "_sum"].value() / max_grade
                else:
                    scale_std = 0.1 * shift_to_zero / (std_dev / max_grade)
                    scaled_percent = scale_std + 0.8
                if scaled_percent <= (overall_grade.value() / max_grade):
                    scaled_percent = (overall_grade.value() / max_grade)

                curved_grade = None
                for i, v in enumerate(self.__grades_definition):
                    if scaled_percent >= 1.:
                        curved_grade = grade(gradeO + "_curved", value=self.__grades_definition[0][1])
                        break
                    if (scaled_percent >= v[0]):
                        break

                curved_grade = grade(gradeO + "_curved", value=self.__grades_definition[i][1])

                students[student].add_grade(curved_grade)



