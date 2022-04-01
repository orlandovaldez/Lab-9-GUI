
from cProfile import label
from email.mime import image

from tkinter.messagebox import showinfo
from breezypythongui import EasyFrame
from tkinter import filedialog as fd
from tkinter import *

#TODO
'''
    -Open A file with file chooser, then once selected open in a new window,
     separate from the application
    -Next action will walk through image modifiers from last lab, until user either clicks
     close or choose. You will need to close and reopen the image each time to accomplish 
     this action.
    -Close closes all the open file and windows and exits the program

    -Image Action List:
        -Original image in an appropriately sized window.
        -Gray scale version
        -black and white version
        -blurred 50 percent version
        -edge detected version
'''

class ChooseButton(EasyFrame):

    def __init__(self):
        '''Sets up the windows and buttons'''
        EasyFrame.__init__(self, title= "New Pic Chooser")
 
        self.label = self.addLabel(text="Image Action List", row=0, column=0, columnspan= 2, sticky= "NSEW")

        self.chooseBtn = self.addButton(text= "Choose",row=1,column=0,command= self.chooseFile)
        self.nextActBtn = self.addButton(text= "Next Action",row=1,column=1)
        self.closeBtn = self.addButton(text= "Close",row=1,column=2, command= self.close)


    def chooseFile(self):
        '''Opens files chooser and opens it in a new window, separate from application'''
        fileList = [("GIF Files","*.gif")]
        filename = fd.askopenfilename(title= "Add a picture file", initialdir= "/",filetypes= fileList)
        #showinfo(title= "Image Selected", message= filename)
        
        Og = Tk()
        Og.title("Original Image")
        img = PhotoImage(file= filename)
        label = Label(image = img)
        label.image = img
        label.pack()
        
        Og.mainloop()


    def close(self):
        '''Closes all open files and windows and exits the program'''
        exit()

def main():
    ChooseButton().mainloop()

if __name__ == "__main__":
    main()