import time

file1 = open('report.txt', 'w+')
def report(data):
    file1.write(data[0]+' '+data[1]+'\n')
