# The worst Hex editor ever concieved.
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import re
from textwrap import wrap
#this absolutely will not work without these imports.

editor = tk.Tk()
def openfile(*args):
    editor.filename = filedialog.askopenfilename(title = "Select file")
    editor.txtarea.delete("1.0",END)
    data = []
    count = 0
    in_file = open(editor.filename, 'rb')
    try:
        while True:
            count += 1
            hexdata = in_file.read(8).hex()
            if(len(hexdata) != 16 and len(hexdata) != 0):
                hexdata = hexdata.ljust(16,'z')
            chunk1 = "0x" + hexdata[0] + hexdata[1]
            chunk2 = "0x" + hexdata[2] + hexdata[3]
            chunk3 = "0x" + hexdata[4] + hexdata[5]
            chunk4 = "0x" + hexdata[6] + hexdata[7]
            chunk5 = "0x" + hexdata[8] + hexdata[9]
            chunk6 = "0x" + hexdata[10] + hexdata[11]
            chunk7 = "0x" + hexdata[12] + hexdata[13]
            chunk8 = "0x" + hexdata[14] + hexdata[15]
            hexdata = f"{chunk1} {chunk2} {chunk3} {chunk4} {chunk5} {chunk6} {chunk7} {chunk8}\n"
            data.append(hexdata)
            if len(hexdata) == 0:
                break
    except:
        pass
    for line in data:
        editor.txtarea.insert(END,line)
    in_file.close()
def savefile(*args):
    if editor.filename:
        data = editor.txtarea.get("1.0",'end-1c')
        outbound = saves(data)
        outfile = open(editor.filename,"wb")
        outfile.write(outbound)
        outfile.close()
    else:
        saveasfile()
def saveasfile(*args):
    untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
    data = editor.txtarea.get("1.0",'end-1c')
    outbound = saves(data)
    print(outbound)
    outfile = open(untitledfile,"wb")
    outfile.write(outbound)
    outfile.close()
    editor.filename = untitledfile
def infoabout():
    messagebox.showinfo("about","doing the best i can\n(with python of all things)\nI HATE PYTHON BUT AT LEAST IT\'S NOT JAVA")
def saves(data):
    outbound = bytearray()
    data = data.replace(" ","")
    data = data.replace("z","")
    data = data.replace("0x ","")
    data = data.replace("0x","")
    data = wrap(data, 16)
    for i in data:
        zz = bytearray.fromhex(i)
        outbound += zz
    return outbound
def validate(value):
    pattern = r'\b[A-Fa-f0-9]+@[A-Fa-f0-9]+\.[A-F|a-f]{2,}\b'
    if re.fullmatch(pattern, value) is None:
        return False

    return True
    
editor.title("Matt's Hex Editor")
editor.geometry("1200x700+200+150")
editor.titlebar = Label(textvariable=editor.title,font=("comic sans ms",18),bd=2)
editor.titlebar.pack(side=TOP,fill=BOTH)
editor.statusbar = Label(editor,anchor=W,text="here's your file, in HEX FORM!",font=("comic sans ms",8),bd=2,relief=GROOVE)
editor.statusbar.pack(side=BOTTOM,fill=BOTH)

editor.menubar = Menu(editor,font=("comic sans ms",15),activebackground="skyblue")
editor.config(menu=editor.menubar)
editor.menubar.add_command(label="Open",accelerator="Ctrl+O",command=openfile)
editor.menubar.add_command(label="Save",accelerator="Ctrl+S",command=savefile)
editor.menubar.add_command(label="Save As",accelerator="Ctrl+A",command=saveasfile)
editor.menubar.add_command(label="About",command=infoabout)
editor.menubar.add_command(label="Exit",accelerator="Ctrl+E",command=exit)
scroll_y = Scrollbar(editor,orient=VERTICAL)
editor.txtarea = Text(editor,yscrollcommand=scroll_y.set,font=("Lucida Console",15,"bold"),state="normal",relief=GROOVE)
scroll_y.pack(side=RIGHT,fill=Y)
scroll_y.config(command=editor.txtarea.yview)
editor.txtarea.pack(fill=BOTH,expand=1)

editor.mainloop()
