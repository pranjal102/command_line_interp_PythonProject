import constants
import os
import errorHandler
import exploreCommand, changeDirectory_command, createDir_command,fileManipulation_command

def parameterCommand(dismantle_command, self):

	if dismantle_command[0] == "explore" :
		exploreCommand.exploreWithFlag(dismantle_command,self)
	elif dismantle_command[0] == "goto" :
		changeDirectory_command.changeDir(dismantle_command,self)
	
	elif dismantle_command[0] == "make" :
		directory_to_make = dismantle_command[1]
		createDir_command.createDir(directory_to_make, self)
	elif dismantle_command[0] == "del" :
		directory_to_del = dismantle_command[1]
		createDir_command.deleteDir(directory_to_del,self)

	elif dismantle_command[0] == "rename":
		directory_to_rename = dismantle_command[1]
		name = dismantle_command[2]
		createDir_command.renameDir(directory_to_rename,name, self)  

	elif dismantle_command[0] == "create":
		file_to_create = dismantle_command[1]
		fileManipulation_command.createEmptyFile(file_to_create,self)	

	elif dismantle_command[0] == "open":
		flagOrFile = dismantle_command[1]
		if flagOrFile == "-def":
			fileManipulation_command.openFileWithDefaultApplication(dismantle_command[2],self)
		else:
			fileManipulation_command.openFile(dismantle_command[1],self)

	elif dismantle_command[0] == "write":
		file_to_input = dismantle_command[1]
		data_to_write = ""
		for i in range(2,len(dismantle_command)):
			data_to_write = data_to_write + dismantle_command[i] + " "
		fileManipulation_command.writeFileWithData(file_to_input,data_to_write,self)			

	
	elif dismantle_command[0] == "append":
		file_to_input = dismantle_command[1]
		data_to_write = ""
		for i in range(2,len(dismantle_command)):
			data_to_write = data_to_write + dismantle_command[i] + " "
		fileManipulation_command.appendFileWithData(file_to_input,data_to_write,self)

	elif dismantle_command[0] == "copy":
		source = dismantle_command[1]
		dest = dismantle_command[2]
		fileManipulation_command.copyFile(source,dest,self)


	else:
		error = ""
		for item in dismantle_command:
			error += item + " "
		errorHandler.handle(error,self)

	


def singleWordCommand(input_entered, self):

	if input_entered == constants.LEAVE:
		exit()

	elif input_entered == "cwd":
		self.displayText("Your current working directory is : " + os.getcwd())
		#print("Your current working directory is : " + os.getcwd())

	elif input_entered == "explore":     # TODO \\dont show hidden files
		exploreCommand.explore(input_entered,self)

	elif input_entered == "guide":
		guide = open(constants.GUIDE_PATH)
		#print(guide.read())
		self.displayText(guide.read())
		guide.close()
	
	elif input_entered.lower() == "y":
		if self.yesNo_option_handler != "":
			#split temp data , retrieve dir's name to be deleted, call the required handler
			#self.createDir_command.
			temp_data_split = self.temp_data.split()
			function_used = temp_data_split[0]
			if function_used == "deleteDir":
				dirName = temp_data_split[1]
				createDir_command.deleteDir_confirmed(dirName,self)


		else:
			errorHandler.handle(input_entered,self)

	elif input_entered.lower() == "n":
		if self.yesNo_option_handler != "" :
			self.yesNo_option_handler = ""
			self.temp_data = ""
		else:
			errorHandler.handle(input_entered,self)
			


	else:
		errorHandler.handle(input_entered,self)



def checkCommand(input_entered, self):

		dismantle_command = input_entered.split(" ")

		if len(dismantle_command) > 1 :
			parameterCommand(dismantle_command, self)

		else:
			singleWordCommand(input_entered, self)



