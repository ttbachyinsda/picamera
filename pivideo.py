import time
from picamera import PiCamera
import facetest
camera = PiCamera()
camera.resolution=(320,240)
for i in range(0,10):
    camera.start_recording('/home/pi/new/video.h264')
    time.sleep(2)
    camera.stop_recording()
    camera.stop_preview()