import BufferArgv

buffer = BufferArgv.BufferString("python3 python_script.py --number=43")

@buffer.addFlag("-n", "--number", mode="equals_with", obj_type='integer')
def onNumber(obj):
    print(obj.number)

buffer.trust()
