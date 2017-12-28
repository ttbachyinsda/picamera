import time
from picamera import PiCamera
import facetest
camera = PiCamera()
camera.resolution=(640,480)
time.sleep(2)
camera.start_preview()
while True:
    start_time = time.time()
    filename = '/home/pi/new/detect%s.jpg'%start_time
    camera.capture(filename)
    res = facetest.detect_api(facetest.key, facetest.secret, filename)
    output = open('/home/pi/new/result%s.txt'%start_time,'w')
    output.write(res)
    output.close()