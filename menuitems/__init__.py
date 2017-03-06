from read_override import read_from
from write_override import write_from
from load_ps_stack import load_stack
import subprocess
import nukescripts
import nuke

nuke.menu('Nuke').addCommand('File/Open Explorer Window','subprocess.Popen(\'explorer ""\')','ctrl+alt+o')

# Standard Overrides
nuke.menu('Nodes').addCommand('Image/Read','scripts.read_from()','r')
nuke.menu('Nodes').addCommand('Image/Write','scripts.write_from()','w')