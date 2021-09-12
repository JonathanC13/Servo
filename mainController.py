


class validateCommand:
	
	def __init__(self):
		pass;
		
	# Desc: function to determine if command is valid and if it can be added to be processed
	# In: @strCommandToValidate: command to validate ;
	# Ret: 1 if shutdown ; 0 if other
	def validateCommand(self,strCommandToValidate, arrCommandToProcess):
		arrValidCommands = ['SHUTDOWN','STOP','PULL','NEXT','SKIP'];
		
		strCommandToValidateUpper = strCommandToValidate.upper()
		
		if(strCommandToValidateUpper == 'STOP'):
			print('validateCommand: STOP command');
			arrCommandToProcess.append(strCommandToValidateUpper);
			return 0;
			
		elif(strCommandToValidateUpper in arrValidCommands):
			if (len(arrCommandToProcess) == 0):
				print('validateCommand: Currently no command being processed, adding {x}'.format(x=strCommandToValidate));
				arrCommandToProcess.append(strCommandToValidateUpper);
				
				if(strCommandToValidateUpper = 'SHUTDOWN'):
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
