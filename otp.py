# Python program to create 
# a file explorer in Tkinter 

# import all components 
# from the tkinter library 
import subprocess
import shutil, os
import sys
from tkinter import *

# import filedialog module 
from tkinter import filedialog 


# Function for opening the 
# file explorer window 
def browseKeyFiles(): 
        filenameKey = filedialog.askopenfilename(initialdir = "/" , title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
	# Change label contents 
        label_key.configure(text=filenameKey)  

def browseEncryptFiles(): 
        filenameMessage = filedialog.askopenfilename(initialdir = "/" , title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 	
	# Change label contents 
        label_file.configure(text= "" + filenameMessage)  
        filepath = label_file.cget("text")
        keypath = label_key.cget("text")
        key = label_key.cget("text").split("/")[-1]
        print(label_key.cget("text").split("/")[-1])  
        file = label_file.cget("text").split("/")[-1]
        print(label_file.cget("text").split("/")[-1]) 
        label_xor.configure(text=key+file)
        xor = label_xor.cget("text").split("/")[-1]
        print(label_xor.cget("text").split("/")[-1])
        print(xor.replace(key, "", 1))
        encpath = (filepath.replace(file, "", 1) + xor)
        print(filepath.replace(encpath, "", 1) + xor)
        temp = ('python enc.py ' + ' ' + str(filepath) + ' ' + str(keypath) +  ' ' + str(encpath) )
        symfile = (str(temp))
        print (temp)
        #print (symfile)
        os.system(symfile)
        # copy key to current working directory
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keys")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = (key)
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = (key)
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        os.remove(source)
        # copy key to used directory 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = (key)
        source = (os.path.join(currentDirectory, filenamepk))
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("used")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = (key)
        destination = (os.path.join(currentDirectory, filenamepk)) 
        shutil.copy(source, destination)     
        os.remove(source)

def browseDecryptFiles(): 
        filenameXor = filedialog.askopenfilename(initialdir = "/" , title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*"))) 	
	# Change label contents 
        label_file.configure(text= "" + filenameXor)  
        filepath = label_file.cget("text")
        keypath = label_key.cget("text")
        key = label_key.cget("text").split("/")[-1]
        print(label_key.cget("text").split("/")[-1])  
        file = label_file.cget("text").split("/")[-1]
        #print(label_file.cget("text").split("/")[-1]) 
        label_xor.configure(text=file)
        xor = label_xor.cget("text").split("/")[-1]
        #print(label_xor.cget("text").split("/")[-1])
        #print(key)
        #print(xor.replace(key, "", 1))
        encpath = (filepath.replace(file, "", 1) + (xor.replace(key, "", 1)))
        print(filepath.replace(encpath, "", 1) + xor)
        temp = ('python enc.py ' + ' ' + str(filepath) + ' ' + str(keypath) +  ' ' + str(encpath) )
        symfile = (str(temp))
        #print (temp)
        #print (symfile)
        os.system(symfile)
        # copy key to current working directory
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("keys")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = (key)
        source = (os.path.join(currentDirectory, filenamepk)) 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = (key)
        destination = (os.path.join(currentDirectory, filenamepk))
        shutil.copy(source, destination)
        os.remove(source)
        # copy key to used directory 
        currentDirectory = os.path.abspath(os.getcwd())
        filenamepk = (key)
        source = (os.path.join(currentDirectory, filenamepk))
        currentDirectory = os.path.abspath(os.getcwd())
        subdir = ("used")
        currentDirectory = (os.path.join(currentDirectory, subdir))
        filenamepk = (key)
        destination = (os.path.join(currentDirectory, filenamepk)) 
        shutil.copy(source, destination)     
        os.remove(source)
															
# Create the root window 
root = Tk() 

# Set window title 
root.title('One Time Pad') 

# Set window size 
root.geometry("750x350") 

#Set window background color 
root.config(background = "white") 

# Create a File Explorer label 
label_key = Label(root, text = "Key", width = 100, height = 4, fg = "blue") 
label_file = Label(root, text = "Message", width = 100, height = 4, fg = "blue") 
label_xor = Label(root, text = "xor", width = 100, height = 4, fg = "blue")

	
button_explore = Button(root, text = "Key Files", command = browseKeyFiles) 
button_explore1 = Button(root, text = "Encrypt", command = browseEncryptFiles) 
button_explore2 = Button(root, text = "Decrypt", command = browseDecryptFiles) 

button_exit = Button(root, text = "Exit", command = exit) 

# Grid method is chosen for placing 
# the widgets at respective positions 
# in a table like structure by 
# specifying rows and columns 
label_key.grid(column = 1, row = 1) 
label_file.grid(column = 1, row = 2)
label_xor.grid(column = 1, row = 3)

button_explore.grid(column = 1, row = 4) 
button_explore1.grid(column = 1, row = 5) 
button_explore2.grid(column = 1, row = 6) 

button_exit.grid(column = 1,row = 7) 

# Let the window wait for any events 
root.mainloop() 
