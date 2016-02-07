# Downlink v0.00, written by John Gabriel, 07/02/16

class Comp(object): #A computer. Every computer in the game can (security notwithstanding) be controlled.
	def __init__(self, name, address=-1):
		self.name = name #The name of the system. Not used to connect to it! That's the address.
		self.address = address #Defaults to -1 for now. (I can set appropiate addesses if I want - otherwise this will later assign a random IP-like address.)
		self.root = Dir("") #For the purposes of the simulation, all systems have one and only one filesystem. This is just a blank-named directory.
		self.users = [] #By default, all comps will have a root account with some hefty protection. Randomly-generated comps will get randomly-generated users with looser security.

class Dir(object): #A folder/directory.
	def __init__(self, name):
		self.name = name #Used as foldername, seen by player.
		self.files = [] #Folders can store other folders!
		self.dirs = [] #Folders have files in them.

class File(object): #A file. Contains stuff.
	def __init__(self, name, contents=""):
		self.name = name #Used as filename, seen by player.
		self.contents #What's in the file, and what will be shown when the player cats the file. Useful for world-building.
