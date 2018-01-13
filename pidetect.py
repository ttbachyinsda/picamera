#coding=utf-8
import time
from picamera import PiCamera
import facetest
import shutil
import os
import random
import json
import zipfile
import sys
import pymongo
reload(sys)
sys.setdefaultencoding('utf8')
lock = 0

dburi = "mongodb://127.0.0.1"
client = pymongo.MongoClient(dburi)
db = client["data"]
facedatadb = db["facedata"]
resultdb = db["resultdata"]

if facedatadb.count() == 0:
    facedatadb.insert_one({"token": 'FACE', "facename": 'GuoFangZe'})


def getfacedata():
    res = []
    for element in facedatadb.find():
        res.append(element)
    return res


def toreport(start_time, filename):
    global lock
    # res = facetest.search(facetest.key, facetest.secret, filename, 'testset')
    res = {}
    if random.random() > 0.9:
        prefix1 = '/home/pi/new/'
        prefix2 = '/home/pi/old/'
        shutil.copyfile(prefix1+filename, prefix2+filename)
        res = {'Face': [], 'Report': 'WrongFace', 'Filepath': filename, 'Time': start_time}
        resultdb.insert_one(res)
    else:
        if random.random() > 0.8:
            facedata = getfacedata()
            prefix1 = '/home/pi/new/'
            prefix2 = '/home/pi/old/'
            shutil.copyfile(prefix1 + filename, prefix2 + filename)
            res = {'Face': [facedata[0]], 'Report': 'RightFace', 'Filepath': filename, 'Time': start_time}
            resultdb.insert_one(res)


def generatemarkdown():
    global lock
    prefix2 = '/home/pi/old/'
    nowtime = str(time.time())
    os.mkdir(nowtime)
    markdownstr = "###人脸检测报告\n\nBy ttbachyinsda\n\n"
    while lock == 1:
        3+2
    lock = 1
    for st in resultdb.find().sort("Time", pymongo.ASCENDING):
        if st['Face'] == []:
            filename = st['Filepath']
            shutil.copyfile(prefix2 + filename, './'+nowtime+'/'+filename)
            markdownstr = markdownstr + "未知人脸：!["+filename+"]("+filename+")\n\n"
        else:
            filename = st['Filepath']
            shutil.copyfile(prefix2 + filename, './' + nowtime + '/' + filename)
            markdownstr = markdownstr + "已知人脸："+ st['Face'][0][1]+"![" + filename + "](" + filename + ")\n\n"
    lock = 0

    file1 = open("./"+nowtime+"/report.md", 'w')
    file1.write(markdownstr)
    file1.close()

    z = zipfile.ZipFile(nowtime + '.zip', 'w', zipfile.ZIP_DEFLATED)
    startdir = "./"+nowtime
    for dirpath, dirnames, filenames in os.walk(startdir):
        for filename in filenames:
            z.write(os.path.join(dirpath, filename))
    z.close()
    return nowtime


if __name__ == '__main__':
    camera = PiCamera()
    camera.resolution = (640, 480)
    time.sleep(2)
    camera.start_preview()
    detectfilenamelist = []
    timelist = []
    while True:
        prefix = '/home/pi/new/'
        start_time = time.time()
        filename = '%s.jpg' % start_time
        camera.capture(prefix + filename)
        detectfilenamelist.append(filename)
        timelist.append(start_time)

        toreport(start_time, filename)

        # generatemarkdown()
        if (start_time - timelist[0] > 60):
            timelist.remove(0)
            detectfilenamelist.remove(0)