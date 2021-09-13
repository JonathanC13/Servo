import time
import wiringpi

if __name__ == "__main__":
	# use 'GPIO naming'
	wiringpi.wiringPiSetupGpio()

	# set PINs to be a PWM output
	wiringpi.pinMode(7, wiringpi.GPIO.OUTPUT)
	
	wiringpi.digitalWrite(7,0)
	
	# set PINs to be a PWM output
	wiringpi.pinMode(26, wiringpi.GPIO.PWM_OUTPUT)
	
	wiringpi.pwmWrite(26,150)
	
	time.sleep(10)
