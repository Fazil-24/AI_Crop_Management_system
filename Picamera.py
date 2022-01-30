from picamera import PiCamera
camera = PiCamera()
time.sleep(2)
camera.capture("/home/pi/Cam-Pics/img.jpg")
print("Done.")