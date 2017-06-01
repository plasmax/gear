from read_override import read_from
from write_override import write_from
from load_ps_stack import load_stack
from create_menu import creator_menu

# import subprocess
import nukescripts
import nuke

def menu_setup():
	"""
		As some of these commands are overrides for standard nuke menu items, a small line of code is required in menu.py:
		gear.menu_setup()
		This is necessary to override existing commands.
	"""
	toolbar_menu = nuke.menu('Nuke')
	nodes_menu = nuke.menu('Nodes')

	# New Menu items
	toolbar_menu.addCommand('File/Open Explorer Window','gear.open_explorer()','ctrl+alt+o')
	toolbar_menu.addCommand('Create/Create New Menu Item','gear.creator_menu()')

	# Standard Overrides
	nodes_menu.addCommand('Image/Read','gear.read_from()','r')
	nodes_menu.addCommand('Image/Write','gear.write_from()','w')

def open_explorer():
	import subprocess
	subprocess.Popen('explorer ""')


