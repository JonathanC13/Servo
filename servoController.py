import time
import wiringpi





class servoController:
	
	def __init__(self):
		print('In servoTest');

	def initializeServo(self):
		
		# save current position
		self.intCurrentBaseServoms = 0;
		self.intCurrentTapServoms = 0;
		
		# Base PIN
		self.intBaseServoPIN = 32
		# Tap PIN
		self.intTapServoPIN = 33
		
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
		
		self.tapTopms = round(tapTopDeg * servoRatio)
		self.tapBotms = round(tapBotDeg * servoRatio)		
		
		
		# use 'GPIO naming'
		wiringpi.wiringPiSetupGpio()

		# set PINs to be a PWM output
		wiringpi.pinMode(self.intBaseServoPIN, wiringpi.GPIO.PWM_OUTPUT)
		wiringpi.pinMode(self.intTapServoPIN, wiringpi.GPIO.PWM_OUTPUT)

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
		self.setCurrentBaseServo (basePullms)
		
		wiringpi.pwmWrite(self.intTapServoPIN, self.tapTopms)
		self.setCurrentTapServo (tapTopms)
		
		

	def setCurrentBaseServo(self,intNewBasePos):
		self.intCurrentBaseServoms = intNewBasePos;
		
	def getCurrentBaseServo(self):
		return self.intCurrentBaseServoms;
		
	def setCurrentTapServo(self,intNewTapPos):
		self.intCurrentTapServoms = intNewTapPos;
		
	def getCurrentTapServo(self):
		return self.intCurrentTapServoms;
		
		
	def moveBaseToPullPos(self, servoEvent):
		
		if(self.getCurrentBaseServo() != self.basePullms):
			
			y = 1
			if (self.getCurrentBaseServo() > self.basePullms):
				y = -1
			else:
				y = 1
				
			for x in range(self.getCurrentBaseServo(), self.basePullms, y):
				if(servoEvent.isSet()):
					wiringpi.pwmWrite(self.intBaseServoPIN, x)
					self.setCurrentBaseServo (x)
					print('moveBaseToPullPos: current base servo: {x}'.format(x= x))
				else:
					break;
					
			time.sleep(2);
	
	def moveBaseToXPos(self, servoEvent):
		
		if(self.getCurrentBaseServo() != self.baseXms):
			
			y = 1
			if (self.getCurrentBaseServo() < self.baseXms):
				y = 1
			else:
				y = -1
				
			for x in range(self.getCurrentBaseServo(), self.baseXms, y):
				if(servoEvent.isSet()):
					time.sleep(1);
					wiringpi.pwmWrite(self.intBaseServoPIN, x)
					self.setCurrentBaseServo (x)
					print('moveBaseToXPos: current base servo: {x}'.format(x= x))
				else:
					break;
					
			time.sleep(2);
					
	def moveTapToTopPos(self, servoEvent):
		
		if(self.getCurrentTapServo() != self.tapTopms):
			
			y = 1
			if (self.getCurrentTapServo() > self.tapTopms):
				y = -1
			else:
				y = 1
				
			for x in range(self.getCurrentTapServo(), self.tapTopms, y):
				if(servoEvent.isSet()):
					wiringpi.pwmWrite(self.intTapServoPIN, x)
					self.setCurrentTapServo (x)
					print('moveTapToTopPos: current tap servo: {x}'.format(x= x))
				else:
					break;
					
			time.sleep(2);
					
	def moveTapToBotPos(self, servoEvent):
		
		if(self.getCurrentTapServo() != self.tapBotms):
			
			y = 1
			if (self.getCurrentTapServo() < self.tapBotms):
				y = 1
			else:
				y = -1
				
			for x in range(self.getCurrentTapServo(), self.tapBotms, y):
				if(servoEvent.isSet()):
					time.sleep(1);
					wiringpi.pwmWrite(self.intTapServoPIN, x)
					self.setCurrentTapServo (x)
					print('moveTapToBotPos: current tap servo: {x}'.format(x= x))
				else:
					break;
			time.sleep(2);
			
					
	def commandPull(self, servoEvent):
		
		if(servoEvent.isSet()):
			if(servoEvent.isSet()):
				# move to pull position
				moveBaseToPullPos(servoEvent);

			if(servoEvent.isSet()):
				# make sure tap is at top position as start
				moveTapToTopPos(servoEvent);
			
			if(servoEvent.isSet()):
				# tap
				moveTapToBotPos(servoEvent);
			
			if(servoEvent.isSet()):
				# reset tap
				moveTapToTopPos(servoEvent);
		
			if(servoEvent.isSet()):
				# pre-emptively move to X / skip position
				moveBaseToXPos(servoEvent);

	def commandXorSkip(self, servoEvent):
		
		if(servoEvent.isSet()):
			if(servoEvent.isSet()):
				# move to pull position
				moveBaseToXPos(servoEvent);

			if(servoEvent.isSet()):
				# make sure tap is at top position as start
				moveTapToTopPos(servoEvent);
			
			if(servoEvent.isSet()):
				# tap
				moveTapToBotPos(servoEvent);
			
			if(servoEvent.isSet()):
				# reset tap
				moveTapToTopPos(servoEvent);

