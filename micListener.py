import threading
import speech_recognition as sr

import mainController


class micListener:
	
	def __init__(self):
		print('In micListener');
		
	def run(self, arrCommandToProcess, micEvent):
		print('\n');
		__validateCommand = mainController.validateCommand();
		text = ''
		while(micEvent.isSet()):
			print('micListener =====');
			
			
			# get audio from the microphone                                                                       
			r = sr.Recognizer()                    
			                                                               
			with sr.Microphone() as source:                                                                       
				print("Speak:")                                                                                   
				audio = r.listen(source)   

			try:
				text = r.recognize_google(audio)
				print('micListener =====');
				print('I heard {x}'.format(x=text))
				print('micListener /=====');
				#if  r.recognize_google(audio)) == keyword:
				#	myfunction()
			except sr.UnknownValueError:
				print('micListener =====');
				print("Could not understand audio")
				print('micListener /=====');
			except sr.RequestError as e:
				print('micListener =====');
				print("Could not request results; {0}".format(e))
				print('micListener /=====');
			
			print('micListener =====');
			print('You have entered {x}'.format(x=text));
			print('micListener /=====');

			
			retVal = __validateCommand.validateCommand(text, arrCommandToProcess);
			print('micListener: {x}'.format(x= retVal))
			
			if(retVal == 1):
				micEvent.clear()
				break;
			else:
				continue;
