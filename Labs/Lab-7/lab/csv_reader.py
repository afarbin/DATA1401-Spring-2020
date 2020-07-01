def csv_reader(filename):
    file = open(filename, 'r')
    columns = None
    data = []
    final = []

    for line in file:
        if columns == None:
            columns = (line.rstrip('\n').split(','))
        else:
            data.append(line.rstrip('\n').split(','))

    for line in range(len(data)):
        student_grade_dict = dict()
        for grade in range(len(data[line])):
            try:
                float(data[line][grade])
                student_grade_dict[columns[grade]] = float(data[line][grade])
            except ValueError:
                student_grade_dict[columns[grade]] = data[line][grade]
                
        final.append(student_grade_dict)

    return final
