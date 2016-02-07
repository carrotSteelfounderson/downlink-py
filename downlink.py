# Downlink, written by John Gabriel, 07/02/16

class Comp: #A computer. Every computer in the game can (security notwithstanding) be controlled.
	def __init__(self, name, address):
		self.name = name #The name of the system. Not used to connect to it! That's the address.
		self.address = address #Defaults to -1 for now. (I can set appropiate addesses if I want - otherwise this will later assign a random IP-like address.)
		self.drive = Dir("") #For the purposes of the simulation, all systems have one and only one 'drive'. This is just a blank-named directory.
		self.users = [] #By default, all comps will have a root account with some hefty protection. Randomly-generated comps will get randomly-generated users with looser security.
		
	@property
	def name(self):
		return self.name
	
	@property
	def users(self):
		return self.users
		
	@property
	def users(self):
		return self.users
		
	@property
	def drive(self):
		return self.drive
		
class User: #An account on a computer. For sake of avoiding potential headaches, one instance of a user should only ever be used by one comp! (Unless... hm.)
	def __init__(self, name, password=-1):
		self.name = name #The username, seen by player.
		self.password = password #Used for logging in. Will be randomly generated unless it's specified.

class Dir: #A folder/directory.
	def __init__(self, name):
		self.name = name #Used as foldername, seen by player.
		self.files = [] #Folders can store other folders!
		self.dirs = [] #Folders have files in them.
		
	@property
	def name(self):
		return self.name
		
	@property
	def files(self):
		return self.files
		
	@property
	def dirs(self):
		return self.dirs
		
	def addFile(self, fileToAdd):
		self.files.append(fileToAdd)
		
	def addDir(self, dirToAdd):
		self.dirs.append(dirToAdd)
		
	def listFiles(self):
		for nextFile in self.files:
			print nextFile.name

class File: #A file. Contains stuff.
	def __init__(self, name, extension="", contents=""):
		self.name = name #Used as filename, seen by player.
		self.extension = extension #Filetype, seen by played. Can be blank.
		self.contents = contents #What's in the file, and what will be shown when the player cats the file. Useful for world-building.
	
	@property
	def name(self):
		return self.name

#del folder(fileIndex)

testComp = Comp("localhost", "127.0.0.1")
testFile = File("test", "txt", "Lorem ipsum...")
testComp.drive.addFile(testFile)
testComp.drive.listFiles()
