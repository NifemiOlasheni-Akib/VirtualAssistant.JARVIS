# Import relevant modules:
import os
import subprocess as sp

paths = {
    'notepad': r"C:\Windows\System32\notepad.exe",
    'calculator': "C:\WINDOWS\system32\calc.exe",
    'zoom': r"C:\Users\HP\AppData\Roaming\Zoom\bin\zoom.exe"
    }
# Define function to open camera:
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
    
# Define function to open notepad:
def open_notepad():
    os.startfile(paths['notepad'])

# Define function to open command prompt:
def open_cmd():
    os.system('start cmd')

# Define function to open calculator:
def open_calculator():
    sp.Popen(paths['calculator'])

# Define function to open Zoom:
def open_zoom():
    os.startfile(paths['zoom'])







