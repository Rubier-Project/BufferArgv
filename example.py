import BufferArgv
import httpx

buffer = BufferArgv.BufferConsole()

@buffer.addFlag("-u")
def onRequest(obj: BufferArgv.Things):
    if not obj.u == "NONECALL":
        if not obj.u == "Null":
            try:
                data = httpx.get(obj.u)
                print("Status Code:", data.status_code)
            except Exception as ERROR:
                print("Error:", ERROR)

        else:
            print("Please put a link in front of -u flag")

@buffer.addFlag("-h", "--help", mode="on_call")
def onHelp(obj: BufferArgv.Things):
    if obj.h == True or obj.help == True:
        print("Usage: python3 test.py -u <URL LINK>")
    if obj.h == False and obj.help == False:
        if hasattr(obj, "u"):
            if getattr(obj, "u") == "NONECALL":
                print("Use -h or --help flag to see usage")
        else:
            print("Use -h or --help flag to see usage")

buffer.trust()
