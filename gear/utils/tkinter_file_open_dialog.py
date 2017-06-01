__all__ = ['tkfileOpen']

# import sys
# print sys.version
# sys.path.append('C:\Program Files\Nuke10.5v1\pythonextensions\site-packages')

import Tkinter as tk
# from Tkinter import filedialog

def tkfileOpen():
	root = tk.Tk()
	root.withdraw()
	file_path = tk.filedialog.askopenfilename()