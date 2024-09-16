# BufferArgv
Simple Library to handle the arguments in ( terminal - strings )

## Console Documention
```python
buffer = BufferConsole()

@buffer.addFlag("-h", "--help", mode="in_front_of")
def HelpManager(obj: Things):
    print(obj.help) # or print(obj.h)

@buffer.addFlag("-s", mode="on_call")
def onStart(obj: Things):
    if obj.s:
        print("The Script will start as soon !")
        #---------

buffer.trust() # Run the Objects
```

## String Documention
```python
string = "python x.py --help"

buffer = BufferString(string)

@buffer.addFlag("--help", mode="on_call")
def onCall(obj: Things):
    print(obj.help)

buffer.trust()
```
