import cx_Freeze
import sys
import os 
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\thesa\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\thesa\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("notepad.py", base=base, icon="mainicon.ico")]


cx_Freeze.setup(
    name = "Notepad",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["mainicon.ico",'tcl86t.dll','tk86t.dll']}},
    version = "0.1",
    description = "Tkinter Application",
    executables = executables
    )