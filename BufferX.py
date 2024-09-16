#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# dev: Host1let
"""
BufferArgv Library
~~~~~~

Controll Your Data in Terminal 
```
from Buffer.BufferArgv import BufferConsole
```
"""

import sys
import json

commands: dict = {}
stringCommands: dict = {}

class BufferAttribute(object):
    def __init__(self, dic):
        self.dic = dic
        for key in dic.keys():
            setattr(self, key, dic[key])

class BufferForm(BufferAttribute):
    def __init__(self, dic):
        super().__init__(dic)
        
class BufferList(object):
    def __init__(self,
                 List: list = [],
                 ):
        
        self.list = List
        
    def parse(self):
        bfd = {}

        for i in range(len(self.list)):
            bfd[str(i+1)] = self.list[i]

        return bfd

    def isexists(self, target):
        if target in self.list:
            return True
        else:return False

    def isinfrontof(self, target, indexes):
        isit = False

        if target in self.list:
            try:
                indx = self.list.index(target)
                if indx == indexes:
                    isit = True
                else:isit = False
            except Exception as e:return e
        
        return isit
    
    def indexexists(self, target):
        if target in self.list:
            return self.list.index(target)
        else:return False

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

        return opts

class BufferConsole(object):
    def __init__(self):
        self.data = []
        self.last_things = Things()
        self.handlers = []
        self.buffer_list = BufferList
        self.modes = [
            'in_front_of',
            'on_call'
        ]

    def __setcommands__(self, __key, __value):
        commands[__key] = __value
        return commands
    
    def getDictArgv(self):
        return BufferList(sys.argv).parse()
    
    def addFlag(self, *flags, mode: str = "in_front_of", obj_type: str = "str"):
        def decorator(func):
            self.handlers.append({func: {"flags": list(set(flags)), "mode": mode, "type": obj_type}})
            return func
        return decorator

    def trust(self):
        for handler in self.handlers:
            func = list(handler.keys())[0]
            flags = handler[func]['flags']
            mode = handler[func]['mode']
            type = handler[func]['type']

            argv = self.buffer_list(sys.argv).parse()
            arg_key = list(argv.keys())
            arg_val = list(argv.values())

            if mode == "in_front_of":

                results = []

                for flag in flags:

                    setattr(self.last_things, flag.replace("-", ""), [])

                    if flag in arg_val:
                        arg_index = arg_val.index(flag)
                        ifo_key = str(arg_index+2)
                        cleared_key = argv[str(arg_index+1)].replace("-", "")
                        attrs = getattr(self.last_things, cleared_key)

                        if ifo_key in arg_key:
                            attrs.append(argv[ifo_key])
                            setattr(self.last_things, cleared_key, argv[ifo_key])
                        else:
                            attrs.append("Null")
                            setattr(self.last_things, cleared_key, "Null")

            func(self.last_things)

class BufferString(object):
    def __init__(self,
                 listed_data = [],
                 __help: str = "",
                 __discription: str = ""
                 ):

        self.listed_data = listed_data
        self.forHelp = __help
        self.dis = __discription
        self.status_help = True
        self.status_dis = True
        self.pyVersion = "3"
        self.data = []
    
    def __setcommands__(self, __key, __value):
        stringCommands[__key] = __value
        return stringCommands
    
    def getDictArgv(self):
        return BufferList(self.listed_data).parse()
    
    def addFlag(self, *flags, mode: str = "in_front_of"):
        flg = list(flags)
        for i in range(len(flg)):
            self.__setcommands__(str(i+1), flg[i])

        if mode == "in_front_of":
            for key, val in BufferString(self.listed_data).getDictArgv().items():

                if str(val) in flg:
                    keyx = int(str(key).replace("_", ""))
                    keyx += 1
                    if not f"_{keyx}" in BufferString(self.listed_data).getDictArgv().keys():
                        self.data.append("Null")
                        pass
                    else:
                        self.data.append(BufferString(self.listed_data).getDictArgv()[f"_{keyx}"])
                        pass
                
                else:
                    pass
            return self.data
