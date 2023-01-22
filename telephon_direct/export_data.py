
def Save_file(name, data_save, operat):
    my_file = open(name, operat)
    for i in data_save:
        my_file.writelines("%s\t" % st for st in i)
        my_file.writelines("\n")  
    my_file.close()
