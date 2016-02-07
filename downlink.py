# Downlink, written by John Gabriel, 07/02/16

class Comp: #A computer. Every computer in the game can (security notwithstanding) be controlled.
	def __init__(self, name, address):
		self.name = name #The name of the system. Not used to connect to it! That's the address.
		self.address = address #Defaults to -1 for now. (I can set appropiate addesses if I want - otherwise this will later assign a random IP-like address.)
		self.drive = Dir("") #For the purposes of the simulation, all systems have one and only one 'drive'. This is just a blank-named directory.
		self.users = [] #By default, all comps will have a root account with some hefty protection. Randomly-generated comps will get randomly-generated users with looser security.

		self.drive.makeDir("bin")
		self.drive.makeDir("home")
		self.drive.makeDir("log")
		self.drive.makeDir("var")

class User: #An account on a computer. For sake of avoiding potential headaches, one instance of a user should only ever be used by one comp! (Unless... hm.)
	def __init__(self, name, password=-1):
		self.name = name #The username, seen by player.
		self.password = password #Used for logging in. Will be randomly generated unless it's specified.

class Dir: #A folder/directory.
	def __init__(self, name, parent=None):
		self.name = name #Used as foldername, seen by player.
		self.dirs = [] #Folders can store other folders!
		self.files = [] #Folders have files in them.
		self.parent = parent
		
	def addFile(self, fileToAdd):
		self.files.append(fileToAdd)
		
	def addDir(self, dirToAdd):
		self.dirs.append(dirToAdd)
		
	def makeDir(self, dirName):
		newDir = Dir(dirName, self)
		self.dirs.append(newDir)
		
	def findDir(self, dirName):
		for nextDir in self.dirs:
			if (nextDir.name == dirName):
				return nextDir
		return None

	def ls(self):
		for nextDir in self.dirs:
			print(nextDir.name)
		for nextFile in self.files:
			print(nextFile.name + "." + nextFile.ext)

class File: #A file. Contains stuff.
	def __init__(self, name, ext="", contents=""):
		self.name = name #Used as filename, seen by player.
		self.ext = ext #Filetype, seen by played. Can be blank.
		self.contents = contents #What's in the file, and what will be shown when the player cats the file. Useful for world-building.

#Populate the 'world'.
testComp = Comp("localhost", "127.0.0.1")
testComp.drive.addFile(File("test", "txt", "Lorem ipsum..."))

#Set up some gameplay variables.
wantToQuit = False #Game continues as long as this is false. Currently, game only ends when the player wants it to - might have other gameover scenarios.
currentComp = testComp #Which comp the player is connected to.
currentDir = testComp.drive #Which folder the player is currently browsing.

while (wantToQuit == False):	
	command = input(currentComp.name + ":/" + currentDir.name + "$ ").split() #Get user command and split into list of words.
	
	if (command[0] == "ls"):
		currentDir.ls()

	elif (command[0] == "cd"):
		if (command[1] == ".."):
			if (currentDir.parent != None):
				currentDir = currentDir.parent
		else:
			newDir = currentDir.findDir(command[1])
			if (newDir != None):
				currentDir = newDir
			else:
				print(command[1] + ": No such directory")
	elif (command[0] == "quit"):
		wantToQuit = True
	else:
		print(command[0] + ": command not found")
