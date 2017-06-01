__all__ = ['load_stack']

import nuke

def load_stack(load_stack_js = r'C:\ps_js\load_stack.jsx', js_file = r'c:\ps_js\test_load_stack.jsx', psApp = r'C:\Program Files\Adobe\Adobe Photoshop CC 2017\Photoshop.exe' ):
    import os
    import subprocess
    sn = nuke.selectedNode()
    js_commands = '#include {0}\nloadStack(\'{1}\', \'{2}\', \'{3}\');'.format(
            load_stack_js,
            os.path.dirname(sn['file'].value())+'/',
            sn.name(),
            sn['file'].value().split('.')[-1]
            )
    with open(js_file, 'wb') as f:
        f.write(js_commands)
    target = r'"{0}" "{1}"'.format(psApp, js_file)
    subprocess.Popen(target)

nuke.menu('Nodes').addCommand('Scripts/Load Photoshop Stack','gear.load_stack()','shift+l')
