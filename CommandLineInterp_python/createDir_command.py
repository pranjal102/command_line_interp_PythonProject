import os
import shutil

def createDir(directory_to_make, self):
	if not os.path.isdir(directory_to_make):
			os.mkdir(directory_to_make)
			self.displayText(directory_to_make + " created successfully.")

	else:
		self.displayText("directory with the given name already exists")

def deleteDir(directory_to_del, self):
	if  os.path.isdir(directory_to_del) or os.path.isfile(directory_to_del):
		#shutil.rmtree(directory_to_del)
		#self.displayText(directory_to_del+" directory removed successfully.")
		self.displayText("Are you sure, you wanto to delete the directory/file?(Y/n)")
		self.yesNo_option_handler = "deleteDir "
		self.temp_data = "deleteDir " + directory_to_del
	else:
		self.displayText("Directory/File with the given name don't exist")


def deleteDir_confirmed(dirName, self):
	if(os.path.isdir(dirName)):
		shutil.rmtree(dirName)
	else:
		os.remove(dirName)
		
	self.displayText(dirName+" directory removed successfully.")
	self.yesNo_option_handler = ""
	self.temp_data = ""



def renameDir(directory_to_rename, name, self):
	if  os.path.isdir(directory_to_rename):
		if os.path.isdir(name):
			self.displayText("Directory with the name "+name+" already exists.")
		else:
			os.rename(directory_to_rename, name)
			self.displayText("Directory renamed successfully.")

	elif os.path.isfile(directory_to_rename):
		if os.path.isfile(name):
			self.displayText("File with name "+name+" already exists.")
		else:
			os.rename(directory_to_rename,name)
			self.displayText("File renamed successfully.")

	else:
		self.displayText("No such directory found")