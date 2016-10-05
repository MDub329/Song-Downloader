
'''
Created on October 2, 2016

Matthew W
'''



from functions import *
import tkinter as tk
from tkinter import ttk
    
def main():
    win = tk.Tk()
   
    
    bitrateVariable = tk.IntVar()
    urlVariable = tk.StringVar()
    
    bitrateVariable.set(192)

    
    settingsLabel = ttk.Label(win,text = "  Enter URL  ", foreground = "blue")
    settingsLabel.grid(row = 0 , column = 1)
    
    
    
    songLabel = ttk.Label(win,text = "Song")
    songEntry = ttk.Entry(win, textvariable = urlVariable)  
    songLabel.grid(row = 4,column = 0 , sticky = 'w' )
    songEntry.grid(row = 4, column = 1, sticky = 'w' )
 
    goButton = ttk.Button(text = "Go", command = lambda: download(urlVariable.get(),bitrateVariable.get(),win ))
    goButton.grid(row = 5, column = 2, sticky = "w")
    win.mainloop()
    
main()



    

