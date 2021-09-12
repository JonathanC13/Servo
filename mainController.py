import threading
#import asyncio
import time


import consoleListener
import micListener

class validateCommand:
	
	def __init__(self):
		pass;
		
	# Desc: function to determine if command is valid and if it can be added to be processed
	# In: @strCommandToValidate: command to validate ;
	# Ret: 1 if shutdown ; 0 if other
	def validateCommand(self,strCommandToValidate, arrCommandToProcess):
		arrValidCommands = ['SHUTDOWNCONSOLE','SHUTDOWN','STOP','PULL','NEXT','SKIP','LIST','SHUTDOWN2'];
		
		strCommandToValidateUpper = strCommandToValidate.upper()
		
		
			
		if(strCommandToValidateUpper in arrValidCommands):
			if (len(arrCommandToProcess) == 0):
				print('validateCommand: Currently no command being processed, adding {x}'.format(x=strCommandToValidate));
				
				if(strCommandToValidateUpper == 'LIST'):
					print('List of commands: =====');
					for i in arrValidCommands:
						print(i);
						
					print('List of commands /=====');	
				elif(strCommandToValidateUpper == 'STOP'):
					print('validateCommand: STOP command');
					arrCommandToProcess.append(strCommandToValidateUpper);
					return 0;
				else:			
					arrCommandToProcess.append(strCommandToValidateUpper);
				
				if(strCommandToValidateUpper == 'SHUTDOWNCONSOLE' or strCommandToValidateUpper == 'SHUTDOWN'):
					print('validateCommand: shutdown command ; {x}'.format(x=strCommandToValidateUpper));
					return 1;
				else:
					return 0;
				
			else:
				print('validateCommand: A command is already being processed, discarding {x}'.format(x=strCommandToValidate));
				return 0;
		else:
			print('validateCommand: The command is not valid, {x}'.format(x=strCommandToValidate));
			return 0;
			




if __name__ == "__main__":
	
	# empty command array
	arrCommandToProcess = []
	
	consoleEvent = threading.Event();
	consoleEvent.set();
	
	micEvent = threading.Event();
	micEvent.set();
	
	__consoleListener = consoleListener.consoleListener();
	__micListener = micListener.micListener();
	
	
	thdConsoleListener = threading.Thread(target=__consoleListener.run, args=(arrCommandToProcess,consoleEvent,))
	thdConsoleListener.start()
	
	thdMicListener = threading.Thread(target=__micListener.run, args=(arrCommandToProcess,micEvent,))
	thdMicListener.start()
	
	while(True):
		
		if ('SHUTDOWNCONSOLE' in arrCommandToProcess):
			print('main SHUTDOWNCONSOLE')
			arrCommandToProcess.clear()
			
			
			consoleEvent.clear()
			thdConsoleListener.join(1);
			print('Joining console listener')
			
			#print(thdConsoleListener.is_alive());
			#print(thdMicListener.is_alive());
			if (thdConsoleListener.is_alive() == False and thdMicListener.is_alive() == False):
				break;
				
		elif ('SHUTDOWN' in arrCommandToProcess):
			print('main SHUTDOWN')
			arrCommandToProcess.clear()
				
			
			micEvent.clear()
			thdMicListener.join(1);
			print('Joining mic listener')
			#print(thdConsoleListener.is_alive());
			#print(thdMicListener.is_alive());
			
			if (thdConsoleListener.is_alive() == False and thdMicListener.is_alive() == False):
				break;
			
		else:
			arrCommandToProcess.clear()
	
	#print('outside');
	
	if (thdConsoleListener.is_alive() == True):
		thdConsoleListener.join(1);
				
	if (thdMicListener.is_alive() == True):
		thdMicListener.join(1);
		
	#print('outside2');
