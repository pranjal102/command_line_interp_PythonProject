import os
import shutil
import constants

def createNewFile(file_to_create,self):
	newFile = open(file_to_create,"wb")
	self.displayText("'" + file_to_create + "' created successfully.") 

def openFile(file_to_open,self):
	file_object = open(file_to_open,"rb")
	self.displayText(constants.LINE_SEPARATORS)
	self.displayText(file_object.read())
	self.displayText(constants.LINE_SEPARATORS)
