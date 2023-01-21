
def Save_file(name, data_save):
    my_file = open(name, "w")
    my_file.write(data_save)
    my_file.close()

def Overwrite_file(name, data_save):
    my_file = open(name, "a")
    my_file.write(data_save)
    my_file.close()