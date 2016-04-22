import os
import constants
import errorHandler


def changeDir(dismantle_command, self):
	
	if dismantle_command[1] != "back" and dismantle_command[1] != "prev" and dismantle_command[1] != "~":
		if os.path.isdir(dismantle_command[1]):
			os.chdir(dismantle_command[1])
			#print(os.getcwd())
			self.displayText(os.getcwd())
			#directory_track.append(os.getcwd())
		else:
			#print("'"+dismantle_command[1]+"' No such directory.")
			self.displayText("'"+dismantle_command[1]+"' No such directory.")

	#elif dismantle_command[1].lower() == "prev":
	#	_ = directory_track.pop()
	#	print("Your prev directory was" + directory_track.pop())
	#	self.browser.append("Your prev directory was" + directory_track.pop())

	elif dismantle_command[1] == "~":
		os.chdir(os.path.expanduser("~"))	
		#print(os.getcwd())	
		self.displayText(os.getcwd())

	else:
		cur = os.getcwd()
		path_split = cur.split("/")
		#print(path_split)
		back_path = ""
		for i in range(0,len(path_split)-2):
			back_path += path_split[i] + "/"
		back_path += path_split[len(path_split)-2]
		#print(back_path)
		os.chdir(back_path)
		#print(os.getcwd())
		self.displayText(os.getcwd())


