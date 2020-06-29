import os
##REPLACE WITH YOUR OWN DIRECTORY##
directory = "/Users/confuzedone/Downloads"
files = []

def getTerminalSize():
    env = os.environ
    def ioctl_GWINSZ(fd):
        try:
            import fcntl, termios, struct, os
            cr = struct.unpack('hh', fcntl.ioctl(fd, termios.TIOCGWINSZ,
        '1234'))
        except:
            return
        return cr
    cr = ioctl_GWINSZ(0) or ioctl_GWINSZ(1) or ioctl_GWINSZ(2)
    if not cr:
        try:
            fd = os.open(os.ctermid(), os.O_RDONLY)
            cr = ioctl_GWINSZ(fd)
            os.close(fd)
        except:
            pass
    if not cr:
        cr = (env.get('LINES', 25), env.get('COLUMNS', 80))

    
    return int(cr[1]), int(cr[0])

def search(fileType):
	"""SEARCHES FOR ALL OF THE FILES IN THE DIRECTORY AND DISPLAYS THEM"""
	num = 1
	print("")
	(width, height) = getTerminalSize()
	print("-" * width)
	print("")
	for filename in os.listdir(directory):
		if filename.endswith("." + fileType):
			files.append(filename)
	for k in files:
		name = k
		print(str(num) + '.', name)
		num = num + 1

def delete(fileToRemove):
	"""COMPLETELY DELETES THE FILE FROM COMPUTER"""
	fileToRemove = int(fileToRemove) - 1
	os.remove(directory + '/' + files[fileToRemove])

def main(fileType):
	"""RESPONSIBLE FOR THE ENTIRE DELETION PROCESS"""
	finished = False
	while not finished:
		search(fileType)
		fileToRemove = input("\nWould you like to delete any files? If yes, type the number of the file. If no, type 'n':")
		if (str(fileToRemove) == 'n'):
			print("Goodbye!")
			finished = True
		else:
			delete(fileToRemove)
		files.clear()

fileType = input('What type of files would you like to delete? (docx, pdf, dmg, txt)' )	
main(fileType)
