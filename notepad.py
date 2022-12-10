from tkinter import *
from tkinter import filedialog,messagebox,simpledialog
import os
top = Tk()
top.geometry("600x600")
top.title("Notepad by Ayush")

name=simpledialog.askstring("Enter data","What is your folder name?",parent=top)
if name is not None:
    top.title("Notepad by " + name)
def newFile():
    editor.delete(1.0,END)
def exitCWSNotepad():
    fb=messagebox.askyesno("Confirm?",message="Are you really close the file?")
    if fb:
        top.quit()  
fileType=("Text File","*.txt"),("All File","*.*")
def openFile():
    global fileType
    fd=filedialog.askopenfile(title="Open file here",filetypes=fileType)
    editor.insert(1.0,fd.readlines())
def saveFile():
    global fileType
    fd=filedialog.asksaveasfile(type="Save file her",filetypes=fileType)
    if fd is None:
        return
    
    fd.write(editor.get(0.0,END))
    fd.close()
    
menubar=Menu(top)

fileMenu = Menu(menubar)
fileMenu.add_command(label="New",command=newFile)
fileMenu.add_command(label="New Window")
fileMenu.add_command(label="Open",command=openFile)
fileMenu.add_command(label="Save",command=saveFile)
fileMenu.add_command(label="Save As")
fileMenu.add_separator()
fileMenu.add_command(label="Page Setup")
fileMenu.add_command(label="Print    ctrl + P")
fileMenu.add_separator()
fileMenu.add_command(label="Exite    ctrl + Q",command=exitCWSNotepad)

editMenu=Menu(menubar,tearoff=0)
editMenu.add_command(label="Undo")
editMenu.add_command(label="Cut    Ctrl + X")
editMenu.add_command(label="Copy    Ctrl + C")
editMenu.add_command(label="Paste    Ctrl + V")
editMenu.add_command(label="Delete    Ctrl + DEL")
editMenu.add_separator()
editMenu.add_command(label="Find    Ctrl + DEL")
editMenu.add_command(label="Find Next    Ctrl + DEL")
editMenu.add_command(label="Find Previous    Ctrl + DEL")
editMenu.add_command(label="Replace    Ctrl + DEL")
editMenu.add_command(label="Go to    Ctrl + DEL")
editMenu.add_separator()
editMenu.add_command(label="Select All    Ctrl + DEL")
editMenu.add_command(label="Time/Date    Ctrl + DEL")
editMenu.add_separator()

formatMenu=Menu(menubar,tearoff=0)
formatMenu.add_command(label="WordWrap")
formatMenu.add_command(label="Font")

viewMenu = Menu(menubar,tearoff=0)

zoomMenu=Menu(menubar,tearoff=0)
zoomMenu.add_command(label="Zome In")
zoomMenu.add_command(label="Zome Out")
viewMenu.add_cascade(label="Zoom",menu=zoomMenu)
viewMenu.add_command(label="Status Bar")


menubar.add_cascade(label="File",menu=fileMenu)
menubar.add_cascade(label="Edit",menu=editMenu)
menubar.add_cascade(label="Format",menu=formatMenu)
menubar.add_cascade(label="view",menu=viewMenu)


editor=Text(top,width=700)
editor.pack()

footerText=StringVar()
# footer = Label(top)
footerText.set("Ln 1, Col 1      |    100%    Window (CRLF)          |     UTF-8")
footer=Label(top,textvariable=footerText,bd=1,relief=SUNKEN,anchor="w",padx=10,fg="gray",font=("Arial",10))

footer.pack(side=BOTTOM,fill=X)

top.config(menu=menubar)
top.mainloop()

