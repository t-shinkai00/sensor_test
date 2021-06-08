import datetime
import picamera
import subprocess

camera = picamera.PiCamera()
dt_now = datetime.datetime.now()
camera.close()
subprocess.run(['raspistill','-o','images/'+str(dt_now.year)+'-'+str(dt_now.month)+'-'+str(dt_now.day)+'-'+str(dt_now.hour)+'-'+str(dt_now.minute)+'.jpg'])

# print(dt_now)