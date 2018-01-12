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
# clearfiles()
import time
c = time.time()
time.sleep(10)
d = time.time()
print d-c, ((d-c)>10)