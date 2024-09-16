import BufferArgv
import os

buffer = BufferArgv.BufferConsole()

def isHumanReadable(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            # Check for non-printable characters
            if all(32 <= ord(char) <= 126 or char in '\n\r\t' for char in content):
                return True
            else:
                return False
    except (UnicodeDecodeError, FileNotFoundError):
        return False
    
@buffer.addFlag("-r")
def onRead(obj: BufferArgv.Things):
    if not obj.r == "NONECALL":
        if os.path.exists(obj.r):
            if os.path.isfile(obj.r):
                if isHumanReadable(obj.r):
                    print(open(obj.r, "r").read())
                else:print("File is not human readable")
            else:print("Path is not a file")
        else:print("Path does not exist")

@buffer.addFlag("-h", "--help", mode="on_call")
def onHelp(obj: BufferArgv.Things):
    if obj.h == True or obj.help == True:
        print("Usage: python3", buffer.getDictArgv()['1'], "-r <FILE PATH>")

buffer.trust()
