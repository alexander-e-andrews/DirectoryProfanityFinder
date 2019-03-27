from os import listdir, walk, scandir
 
# Various file name constants
IGNORE = "ignore.setting"
ACCEPT = "accepted.setting"
# Reading constants
# Comment Line
RCOMMENT = '?'
# Directory line
RDIR = '/'
# Begins with wildcard
RBEG = '*'

# fully named directories ignored
ignoreDirs = []
# Begining named directories ignored
ignoreDirsBWild = []
# fully named files ignored
ignoreFiles = []
# Begining name files ignored
ignoreFilesBWild = []

# File endings that are accepted
acceptedTypes = []

'''
Reads file at IGNORE, then add names to be ignored
'''
def ignoreBuilder():
    with open(IGNORE, 'r') as fr:
        line = fr.readline()
        while line:
            # Check for wildcard symbol in begging
            if line[0] == RBEG:
                line = line[1:]
                if line[0] == RCOMMENT:
                    # This should not happen, but keep it defined
                    pass
                elif line[0] == RDIR:
                    # Remove /
                    # Read line includes the \n at the end, so remove it
                    ignoreDirsBWild.append(line[1:-1])
                else:
                    # Read line includes the \n at the end, so remove it
                    ignoreFilesBWild.append(line[0:-1])
            else: 
                if line[0] == RCOMMENT:
                    pass
                elif line[0] == RDIR:
                    # Remove /
                    # Read line includes the \n at the end, so remove it
                    ignoreDirs.append(line[1:-1])
                else:
                    # Read line includes the \n at the end, so remove it
                    ignoreFiles.append(line[0:-1])
            line = fr.readline()

def acceptedTypesBuilder():
    with open(ACCEPT, 'r') as fr:
        line = fr.readline()
        while line:
            if line[0] == RCOMMENT:
                pass
            else:
                # Read line includes the \n at the end, so remove it
                acceptedTypes.append(line[0:-1])
            line = fr.readline()

'''
Builds the fileTree to explore
'''
class fileTree:
    def __init__(self, directory):
        self.directory = directory
        self.files = []
        self.directories = []
        with scandir(directory) as it:
            for entry in it:
                if entry.is_file():
                    if (entry.name not in ignoreFiles) and not (entry.name.startswith(tuple(ignoreFilesBWild))):
                        if entry.name.endswith(tuple(acceptedTypes)):
                            #print(entry.name + " " + entry.path)
                            self.files.append(entry.path)
                elif entry.is_dir():
                    if (entry.name not in ignoreDirs) and not (entry.name.startswith(tuple(ignoreDirsBWild))):
                        print(entry.name + " " + entry.path)
                        #self.directories.append(fileTree(entry.path))
    
    def toString(self):
        stR  = self.directory
        stR = stR + " \n Files: "
        for entry in self.files:
            stR = stR + entry + ", "
        stR = stR + "\n"
        for entry in self.directories:
            stR = stR + entry.toString() + ", "
        return stR

'''
change
'''
def where():
    return input("What is the full path of directory: ")

'''
Builds a file tree
'''
def directoryFileListBuilder():
    ignoreBuilder()
    acceptedTypesBuilder()
    return fileTree(where())