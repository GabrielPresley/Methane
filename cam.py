from picamera import PiCamera
from time import sleep, time

camera = PiCamera()
camera.resolution = (100, 100)
camera.start_preview()

cycle = input("# of photos: ")
for i in range(cycle):
	t = time()
        camera.capture('/home/pi/images/image_%s_%s.jpg' % (t, i))
        sleep(1)
camera.stop_preview()
