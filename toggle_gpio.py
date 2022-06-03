import time

try:
    import RPi.GPIO as GPIO
except RuntimeError:
    print("Error importing RPi.GPIO!  This is probably because you need superuser privileges.  You can achieve this by using 'sudo' to run your script")

GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(5, GPIO.OUT)

while True:
    print("ON")
    GPIO.output(5, GPIO.HIGH)
    time.sleep(0.5)
    print("OFF")
    GPIO.output(5, GPIO.LOW)
    time.sleep(0.5)
