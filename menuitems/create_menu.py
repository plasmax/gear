__all__ = ['creator_menu']

import nuke

def creator_menu():
    p = nuke.Panel('New Menu Item')
    menu_types = 'Nuke Pane Nodes Properties Animation Viewer'
    p.addEnumerationPulldown('menu', menu_types)
    p.addSingleLineInput('name','File/Example Item')
    p.addSingleLineInput('function', r'myfunction()')
    p.addSingleLineInput('shortcut', 'shift+a')
    p.show()
    nuke.menu(p.value('menu')).addCommand(
        p.value('name'),
        p.value('function'),
        p.value('shortcut'))
        