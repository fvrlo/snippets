The fabled fvrloAPI, to automate all the silly tasks I need. I don't wanna keep copy-pasting lines of code. It hurts my hands.

## __init__.py
---
```python
__name__= 'fvrloAPI'
__doc__ = 'Saving my fingers by building a library of common codes.'
__all__ = [
    'autoDebug',
    'edidGet',
    'edidOut',
    'colortest',
]
import os, sys, subprocess
for pkg in __all__:
    exec(f"from . import {pkg}")

# enablers section
# (basic things that need to be declared/done on import for it all to work)
def block(): if 'UTF' in os.getenv('LC_CTYPE'): return "█" else: return "X"
def edidPrint(): edidOut(edidGet())


def regGet():
	import winreg
    KEYLIST = {
        'CROOT': 'CLASSES_ROOT',
        'CUSER': 'CURRENT_USER',
        'LOCAL': 'LOCAL_MACHINE',
        'USERS': 'USERS',
        'PDATA': 'PERFORMANCE_DATA',
        'CRCFG': 'CURRENT_CONFIG',
        'DDATA': 'DYN_DATA'
        }
    KEYOUT = [{"name": x,"key": y,"items": [],"done": False} for x,y in KEYLIST.items()]
    for x in KEYOUT:
        KEY_items = []
        if x['done'] == True:
            break
        for i in range(1024):
            if x['name'] == 'CROOT':
                KEY_items = winreg.EnumKey(eval(f"winreg.HKEY_{x['key']}"), i)
                continue
            try:
                KEY_items.append(winreg.EnumKey(eval(f"winreg.HKEY_{x['key']}"), i))
            except WindowsError:
                break
        x["items"] = KEY_items
        x["done"] = True
    return KEYOUT


def regOut():
    print("---")
    for z in regGet():
        if type(z['items']) == str:
            print(f"Name: {z['name']}    Count: 1")
            print(z['items'])
        elif type(z['items']) == list:
            print(f"Name: {z['name']}    Count: {len(z['items'])}")
            for y in range(len(z['items'])):
                print((z['items'])[y])
        if z['name'] == 'DDATA':
            print("---")

def getNewlines(string, every=64): # Get a list from one string, seperated every x characters.
    lines = []
    for i in range(0, len(string), every):
        lines.append(string[i:i+every])
    return '\n'.join(lines)

def listGen(filler,y):
    return [filler for x in range(y)]

def getConcat(*args): # Merge a list or strings together to one string, and if you don't want spaces, make the last string be 'nospace'.
    if type(args) == tuple: listData = list(args)
    else: listData = args
    if listData[-1] == 'nospace':
        src = ''
        for i in range(len(listData) - 1):
            infor = str(listData[i])
            src = src + infor
    else:
        src = str(listData[0])
        for i in range(1,len(listData)):
            infor = str(listData[i])
            src = src + ' ' + infor
    return src


```

## autoDebug.py
---
```python
import sys
class mod_call:
    def __call__(self,item):
	    print(f"Type: {type(item)}")
        print(f"Value: {item}")
        
        if inType in [list, tuple, range]:
	        print(f'Length: {len(item)}')
            if inType is list:
                if len(item) == 1:
                    print('Inner Item')
                    print('Type: ',str(type(item[0])))
                else:
                    print(f'Contents: {type(item[0])}')
                    print('')
                    print('Values')
                    for x in item: print(str(x))
                    print('')
            elif inType is tuple:
                if len(item) == 1:
                    print('Inner Item')
                    print(f'Type: {str(type(item[0]))}')
                else:
                    print(f'Contents: {type(item[0])}')
                    print('')
                    print('Values')
                    for x in item: print(str(x))
                    print('')
            elif inType is range: print(f"First: {item[0]}\nLast: {item[-1]}")
        elif inType in [dict]:
            print(f'Length: {len(item)}')
            print('')
            print('Values')
            for x in item.keys():
                print(f'Key: {x}')
                print(f'Value: {str(item.get(x))}')
                print('')
        elif inType in [set,frozenset]:
            print('Values')
            for x in item: print(str(x))
sys.modules[__name__] = mod_call()
```

## colortest.py
---
```python
import sys

class mod_call:
    def __call__(self):
        terse = "-t" in sys.argv[1:] or "--terse" in sys.argv[1:]
        write = sys.stdout.write
        for i in range(2 if terse else 10):
            for j in range(30, 38):
                for k in range(40, 48):
                    if terse:
                        write("\33[%d;%d;%dm%d;%d;%d\33[m " % (i, j, k, i, j, k))
                    else:
                        write("%d;%d;%d: \33[%d;%d;%dm Hello, World! \33[m \n" %
                            (i, j, k, i, j, k,))
                write("\n")

sys.modules[__name__] = mod_call()
```

## edidGet.py
---
```python
import sys
import winreg

# EDID is stored in the registry at:
# HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Enum\DISPLAY\$NAME\$ID\Device Parameters
# Where $NAME = Manufacturer Name ID and Product Code ID and $ID is, well, an ID.
class mod_call:
    def __call__(self):
        OpenKey_display = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,r"SYSTEM\CurrentControlSet\Enum\DISPLAY")
        EDID_list = [{"DISPLAY": '',"ID_LIST": []} for x in range(winreg.QueryInfoKey(OpenKey_display)[0])]
        z = 0
        for i in EDID_list:
            i['DISPLAY'] = winreg.EnumKey(OpenKey_display, z)
            idList = i['ID_LIST']
            OpenKey_IDList = winreg.OpenKey(OpenKey_display,i['DISPLAY'])
            for ID in range(winreg.QueryInfoKey(OpenKey_IDList)[0]):
                idList.append(winreg.EnumKey(OpenKey_IDList, ID))
            idTemp = []
            for ID in idList:
                parameters_key = winreg.OpenKey(OpenKey_IDList,r"%s\%s" % (ID, r"Device Parameters"))
                n, v, t = winreg.EnumValue(parameters_key, 0)
                if n == "EDID" and t == winreg.REG_BINARY and v not in idTemp:
                    idTemp.append(v)
                parameters_key.Close()
            i['ID_LIST'] = idTemp
            OpenKey_IDList.Close()
            z = z + 1
        OpenKey_display.Close()
        return EDID_list

sys.modules[__name__] = mod_call()
```

## edidOut.py
---
```python
import sys
from . import debug

class mod_call:
    def __call__(self, *args):
        for item in args:
            print(f'Display: {(item[0])['DISPLAY']}')
            ID_LIST = (item[0])['ID_LIST']
            print(f'Stored EDIDs: {len(ID_LIST)}')
            EDID_count = 1
            for data in ID_LIST:
                print(f"EDID #{EDID_count}:")
                EDID_count = EDID_count + 1
        
                byteData = data         # byteData is format:bytes, 128 long
                byteList = []           # byteList is a list of bytes, 128 long
                for i in range(0, len(byteData), 1):
                    byteList.append(byteData[i:i+1])
        
                hexData = data.hex()    # hexData is format:string, 256 long
                hexList = []            # hexList is a list of hex as string, 128 long
                for i in range(0, len(hexData), 2):
                    hexList.append(hexData[i:i+2])

                edid_Header = hexList[0:7]
                edid_MFG = byteData[8:9]
                print(edid_Header)
                print(edid_MFG)
                print(byteData[8])
                print(byteData[9])

sys.modules[__name__] = mod_call()
```

