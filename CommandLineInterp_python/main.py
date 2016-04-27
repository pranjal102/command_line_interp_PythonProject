import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import commandHandler
import constants
import os

class CLI(QDialog):
	
	def __init__(self,parent=None):
		
		super(CLI,self).__init__(parent)
		
		self.browser = QTextBrowser()
		self.linedit = QLineEdit("Type command here")
		self.linedit.selectAll()	
		layout = QVBoxLayout()
		layout.addWidget(self.browser)
		layout.addWidget(self.linedit)
		self.setLayout(layout)
		self.linedit.setFocus()
		self.resize(720,430)	
		self.cmdHistory = []
		self.yesNo_option_handler = ""
		self.temp_data = ""               # first element - function's name using -> second number of temp data stored -> then data
		self.topKeyHistory = len(self.cmdHistory) - 1
		self.backHistory = 0;
		self.currentDirectory = os.path.expanduser("~")
		self.previousDirectory = os.path.expanduser("~")	
		self.linedit.returnPressed.connect(self.updateUi)
		self.setWindowTitle("Command Line Interpreter")
		self.startSession()


	def keyPressEvent(self, e):

		if e.key() == Qt.Key_Up and len(self.cmdHistory) != 0:
			#print("pressed")
			#self.displayText("pressed up key")
			if self.topKeyHistory == -1:
				self.topKeyHistory = len(self.cmdHistory) - 1  
			
			self.linedit.setText(self.cmdHistory[self.topKeyHistory])
			self.backHistory = self.topKeyHistory + 1
			self.topKeyHistory -= 1;
			


		elif e.key() == Qt.Key_Down and len(self.cmdHistory) != 0 :
			
			if self.backHistory == len(self.cmdHistory):
				self.backHistory = 0	
			

			self.linedit.setText(self.cmdHistory[self.backHistory]) 
			self.topKeyHistory = self.backHistory - 1
			self.backHistory += 1
			

		else :
			self.topKeyHistory = len(self.cmdHistory) - 1
			self.backHistory = 0

	 	
	
	def startSession(self):
		self.HOME_DIR = os.path.expanduser("~")
		os.chdir(self.HOME_DIR)
		self.resetDisplay()
		#print(os.getcwd())


	def updateUi(self):
		cmd = unicode(self.linedit.text())
		self.cmdHistory.append(cmd)
		self.browser.append(constants.PROMPT+cmd)
		self.linedit.clear()
		commandHandler.checkCommand(cmd, self)

	def resetDisplay(self):
		self.browser.clear()
		self.displayText(constants.WELCOME_STRING)
		self.displayText(constants.LINE_SEPARATORS)	

	def displayText(self ,displayText):
		self.browser.append(displayText)

app = QApplication(sys.argv)
cli = CLI()
cli.show()
app.exec_()



