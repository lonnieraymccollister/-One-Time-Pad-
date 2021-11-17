# Python program to create 
# a file explorer in Tkinter 

# import all components 
# from the tkinter library 
import subprocess
import shutil, os
import sys
from tkinter import *
from sys import argv,exit

# import filedialog module 
from tkinter import filedialog 


# Function for opening the 
# file explorer window 
def browseKeyFiles(): 
        filenameKey = filedialog.askopenfilename(initialdir = os.path.abspath(os.getcwd()) , title = "Select a File", filetypes = (("Text files", "*.txt*"), ("all files", "*.*")))
	# Change label contents 
        label_key.configure(text=filenameKey)  
        file = str(filenameKey)
        print(filenameKey)
        symfile = ("python sp800_22_tofile.py " + file)
        print(symfile)
        os.system(symfile)
															
# Create the root window 
root = Tk() 

# Set window title 
root.title('SP800_22 Random Number Test') 

# Set window size 
root.geometry("750x350") 

#Set window background color 
root.config(background = "white") 

# Create a File Explorer label 
label_key = Label(root, text = "Key", width = 100, height = 4, fg = "blue") 


	
button_explore = Button(root, text = "Key Files", command = browseKeyFiles) 

button_exit = Button(root, text = "Exit", command = exit) 

# Grid method is chosen for placing 
# the widgets at respective positions 
# in a table like structure by 
# specifying rows and columns 
label_key.grid(column = 1, row = 1) 


button_explore.grid(column = 1, row = 4) 


button_exit.grid(column = 1,row = 7) 

# Let the window wait for any events 
root.mainloop() 
