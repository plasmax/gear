__all__ = ['tkfileOpen']

print sys.version
sys.path.append('C:\Program Files\Nuke10.5v1\pythonextensions\site-packages')

import tkinter as tk
from tkinter import filedialog

def tkfileOpen():
	root = tk.Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename()