import os
import shutil
import constants

def createEmptyFile(file_to_create,self):
	newFile = open(file_to_create,"wb")
	newFile.close()
	self.displayText("'" + file_to_create + "' created successfully.") 

def openFile(file_to_open,self):
	file_object = open(file_to_open,"rb")
	self.displayText(constants.LINE_SEPARATORS)
	self.displayText(file_object.read())
	self.displayText(constants.LINE_SEPARATORS)
	file_object.close()

def openFileWithDefaultApplication(file_to_open,self):
	if os.path.isfile(file_to_open):
		ret = os.system('xdg-open ' + ' "'+ file_to_open + '"')
		if ret == 0:
			self.displayText("File opened with default application.")
		else:
			self.displayText("Sorry! Something went wrong.")
	else:
		self.displayText("No such file exists in current directory.")	



def writeFileWithData(file_to_create,data_to_write,self):
	newFile = open(file_to_create,"wb")
	newFile.write(data_to_write)
	newFile.close()
	self.displayText("File created with the input data.")


def appendFileWithData(file_to_append,data_to_write,self):
	newFile = open(file_to_append,"ab")
	newFile.writelines("\n"+data_to_write)
	newFile.close()
	self.displayText("Given data appended to the file.") 


def copyFile(source_file,desitination_file,self):
	shutil.copy(source_file,desitination_file)
	self.displayText("File copied succesfully.")




