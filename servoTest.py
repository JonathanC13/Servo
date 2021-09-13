import time
import wiringpi





class servoTest:
	
	def __init__(self):
		print('In servoTest');

	def initializeServo(self):
		
		# save current position
		self.intCurrentBaseServoms = 0;
		self.intCurrentTapServoms = 0;
		
		# Base PIN
		self.intBaseServoPIN = 12
		# Tap PIN
		#self.intTapServoPIN = 33
		
		## servo ratio
		# 180 deg = 250ms
		# (250 ms / 180 deg) * X = new ms
		self.servoRatio = 250/180
		
		# Base ms
		self.basePullDeg = 0
		self.baseXDeg = 53
		
		# Tap ms
		self.tapTopDeg = 0
		self.tapBotDeg = 10
		
		# conversion to pwm value
		self.basePullms = round(self.basePullDeg * self.servoRatio)
		self.baseXms = round(self.baseXDeg * self.servoRatio)
		
		self.tapTopms = round(self.tapTopDeg * self.servoRatio)
		self.tapBotms = round(self.tapBotDeg * self.servoRatio)		
		
		
		# use 'GPIO naming'
		wiringpi.wiringPiSetupGpio()

		# set PINs to be a PWM output
		wiringpi.pinMode(self.intBaseServoPIN, wiringpi.GPIO.PWM_OUTPUT)
		#wiringpi.pinMode(self.intTapServoPIN, wiringpi.GPIO.PWM_OUTPUT)

		# set the PWM mode to milliseconds stype
		wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

		## divide down clock
		# PWM Frequency in Hz = 19,200,000 Hz / pwmClock / pwmRange
		# want 50 Hz = 19 200 000 Hz , let pwmClock = 192
		# therefore pwmRange = 2000
		# divide down clock
		wiringpi.pwmSetClock(192)
		wiringpi.pwmSetRange(2000)

		
		wiringpi.pwmWrite(self.intBaseServoPIN, self.basePullms)
		self.setCurrentBaseServo (self.basePullms)
		
		#wiringpi.pwmWrite(self.intTapServoPIN, self.tapTopms)
		#self.setCurrentTapServo (self.tapTopms)
		
		

	def setCurrentBaseServo(self,intNewBasePos):
		self.intCurrentBaseServoms = intNewBasePos;
		
	def getCurrentBaseServo(self):
		return self.intCurrentBaseServoms;
		
	def setCurrentTapServo(self,intNewTapPos):
		self.intCurrentTapServoms = intNewTapPos;
		
	def getCurrentTapServo(self):
		return self.intCurrentTapServoms;
		
	def testBaseServoFullRange(self):
		
		for x in range(0,250,1):
			wiringpi.pwmWrite(self.intBaseServoPIN, x)
			self.setCurrentBaseServo (x)
				
		
		time.sleep(5);	
		print('mid');
		for x in range(250,0,-1):
			wiringpi.pwmWrite(self.intBaseServoPIN, x)
			self.setCurrentBaseServo (x)
				
		
		
			
	def testTapServoFullRange(self):
		for x in range(0,250 + 1,1):
			
			self.setCurrentBaseServo (x)
	
		time.sleep(5);	
		
		for x in range(250,0 - 1,-1):
			wiringpi.pwmWrite(self.intTapServoPIN, x)
			self.setCurrentTapServo (x)

if __name__ == "__main__":

	__servoTest = servoTest();
	__servoTest.initializeServo();
	
	__servoTest.testBaseServoFullRange();
	
	print('end');
	#time.sleep(5);	
	
	#__servoTest.testTapServoFullRange();
	
