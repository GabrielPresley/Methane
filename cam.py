from picamera import PiCamera
from time import sleep, strftime

camera = PiCamera()
camera.resolution = (100, 100)

cycle = input("# of photos: ")
for i in range(cycle):
	t = strftime()
        camera.capture('/home/pi/images/image_%s_%s.jpg' % (t, i))
        sleep(1)
