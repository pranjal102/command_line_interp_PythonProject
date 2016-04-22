
import commandHandler
import constants
import os

PROMPT = constants.PROMPT
LINE_SEPARATORS = constants.LINE_SEPARATORS
WELCOME_STRING = constants.WELCOME_STRING
LEAVE = constants.LEAVE
PROMPT = constants.PROMPT

def welcomeText():
	print(LINE_SEPARATORS)
	print(WELCOME_STRING)
	print(LINE_SEPARATORS)

	
	
def startSession():

	HOME_DIR = os.path.expanduser("~")
	os.chdir(HOME_DIR)
	welcomeText()

	#directory_track = [os.getcwd()]
	
	input_entered = "not leave"
	
	while(input_entered != LEAVE):
		input_entered = raw_input(PROMPT) 
		#print(input_entered)
		#commandHandler.checkCommand(input_entered, directory_track)
		commandHandler.checkCommand(input_entered, self)




def main():

		startSession()
		
main()