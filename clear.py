import os
def clearfiles():
    path = '/home/pi/new'
    listfile = os.listdir(path)
    for element in listfile:
        print element
        if 'detect' in element and '.jpg' in element:
            os.remove(path + '/' + element)
        else:
            if 'result' in element and '.txt' in element:
                os.remove(path + '/' + element)
clearfiles()