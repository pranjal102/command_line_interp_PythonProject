import os
import constants
import errorHandler

def exploreWithFlag(dismantle_command,self):

	if dismantle_command[1] == "-h":
		#print(constants.LINE_SEPARATORS)
		self.displayText(constants.LINE_SEPARATORS)
		cwd = os.getcwd()
		dir_list = os.listdir(cwd)
		for dir in dir_list:
			#print(dir)
			self.displayText(dir)
	
	elif dismantle_command[1] == "-f" :
		
		display_only = dismantle_command[2]
		
		#print(constants.LINE_SEPARATORS)
		self.displayText(constants.LINE_SEPARATORS)
		cwd = os.getcwd()
		dir_list = os.listdir(cwd)
		no_file_with_given_name = True
		
		for dir in dir_list:
			if dir.lower() == display_only.lower():
				#print(dir)
				self.displayText("Found required file/directory : "+dir)
				no_file_with_given_name = False

		if no_file_with_given_name:
			#print("No such file or directory found with name ' " + display_only + " '")
			self.displayText("No such file or directory found with name ' " + display_only + " '")

	elif dismantle_command[1] == "-p":
		display=""
		#print(constants.LINE_SEPARATORS)
		self.displayText(constants.LINE_SEPARATORS)		
		cwd = os.getcwd()
		dir_list = os.listdir(cwd)

		for dir in dir_list:
			permission_octal = oct(os.stat(dir)[0])[-3:]
			display += dir + "		" + permission_octal
			#print(display)
			self.displayText(display)
			display = "" 

	else:
		errorHandler.handle(dismantle_command[1],self)


def explore(input_entered,self):
	#print(constants.LINE_SEPARATORS)
	self.browser.append(constants.LINE_SEPARATORS)
	cwd = os.getcwd()
	dir_list = os.listdir(cwd)
	for dir in dir_list:
		if not dir.startswith('.'):
			#print(dir)
			self.displayText(dir)

