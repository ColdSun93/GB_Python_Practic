def Save_file(name, data_save, operat):
    my_file = open(name, operat)
    for key, value in data_save.items():
        my_file.writelines(f'{key}\n')
        for key_o, value_t in value.items():
            my_file.writelines(f'\t{key_o}\t{value_t}\n')
    my_file.close()


def Open_file(name):
    file = open(name, 'r')
    data = {}
    predmet = dict()
    name_st =''
    for line in file:
        if '\t' in line:
            elem = str(line.replace("\n", ""))
            lesson = (elem[elem.find('\t')+1: elem.rfind('\t')])
            valuation = str(
                elem[elem.find("\t[")+2: elem.find("]'")].replace(" ", "")).split(',')
            for i in range(0, len(valuation)):
                if valuation[i] != '':
                    valuation[i] = int(valuation[i])
                else:
                    valuation = []
            predmet[lesson] = valuation
        elif ' ' in line and name_st !='':
            data[name_st]=predmet
            predmet = {}
            name_st = str(line[:-1].replace("\n", ""))
        elif ' ' in line and name_st =='':
            name_st = str(line[:-1].replace("\n", ""))

    file.close
    return data


# name_file = 'student/direct_student.txt'

# Open_file(name_file)
