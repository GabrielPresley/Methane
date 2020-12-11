from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (100, 100)
camera.start_preview()

cycle = input("# of photos: ")
for i in range(cycle):
	t = time.time()
        camera.capture('/home/pi/images/image_%s_.jpg' % (t, i))
        sleep(1)
camera.stop_preview()
