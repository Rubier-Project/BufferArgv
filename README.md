# BufferArgv
Simple Library to handle the arguments in ( terminal - strings )

# Console Documention
```python
buffer = BufferConsole()

@buffer.addFlag("-h", "--help", mode="in_front_of")
def HelpManager(obj: Things):
    print(obj.help) # or print(obj.h)

buffer.trust()
```
