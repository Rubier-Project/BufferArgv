# BufferArgv
Simple Library to handle the arguments in ( terminal - strings )

Objects: `BufferConsole`, `BufferString`, `BufferAttribute`

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

+ The `mode` parameter is `in_front_of` by default

## String Documention
```python
string = "python x.py --help"

buffer = BufferString(string)

@buffer.addFlag("--help", mode="on_call")
def onCall(obj: Things):
    print(obj.help)

buffer.trust()
```

+ The `mode` parameter is `in_front_of` by default

## What is 'Things' Object?

The `Things` Object is created for handle the datas simply

Here is `Things` Object

```python
class Things(object):
    def __init__(self) -> None:
        self.def_attrs = ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__']

    def __str__(self) -> str:
        return json.dumps(dir(self), indent=2)
    
    @property
    def options(self) -> list:
        opts = []

        for item in dir(self):
            if item.startswith("__") and item in self.def_attrs:pass
            else:opts.append(item)

        opts.remove("def_attrs")
        opts.remove("options")
        
        return opts
```

## Check Arguments Automaticly

```python
@buffer.addFlag("-h", "--help", mode="on_call")
def onHelp(obj: BufferArgv.Things):
    if obj.h == True or obj.help == True:
        print("Usage: python3", buffer.getDictArgv()['1'], "-r <FILE PATH>")

buffer.setFilter(['-h', '--help'], "Invalid Argument: B@ARGV")
buffer.trust()
```

The Parameters are: `flags_list`, `err_message`, `_exit`

+ Use `B@ARGV` keyword in `err_message` to see invalid argument. 

- **flags_list** (list): The flags used in the script.
- **err_message** (str): Message printed if an invalid argument is detected.
- **_exit** (bool): If True, the program will terminate upon detecting an invalid argument.

## How to add Keys and Values from Dictionary convert them to the attributes of a class?

its Simple, you should use `BufferAttribute` Object

Here is `BufferAttribute` Object

```python
dict_a = {"name": "Jack", "age": 21}

buffer = BufferAttribute(dict_a)
print(buffer.name) # OutPut: Jack
```

# Notice

+ if you want to set a message for `-h` or `--help` on `on_call` mode, please set that as finally decorator
+ if you want to set filter for args, set that before calling `trust` function ( its suggested to use this by that way, after all its optional )

## Basicly Things
+ Created by `python 3.11.0`
+ Module Git `https://github.com/Rubier-Project/BufferArgv`

```bash
python3 file.py
```
