import threading


import mainController

class consoleListener:
	
	def __init__(self):
		print('In consoleListener');
		
	def run(self, arrCommandToProcess, consoleEvent):
		print('\n')
		__validateCommand = mainController.validateCommand();
		
		while(consoleEvent.isSet()):
			print('consoleListener =====');
			consoleInput = input("Please enter a command like SHUTDOWN or LIST for a list of valid commands: ");
			
			print('You have entered {x}'.format(x=consoleInput));
			print('consoleListener /=====');

			
			retVal = __validateCommand.validateCommand(consoleInput, arrCommandToProcess);
			print('consoleListener: {x}'.format(x= retVal))
			
			if(retVal == 1):
				consoleEvent.clear();
				break;
			else:
				continue;
