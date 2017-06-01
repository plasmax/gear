__all__ = ['parse_nkScript']

import re
import nuke

# regex = re.compile(r'(\w+)( {\n[^}]+name )([a-zA-Z0-9_:/.]+)([^}]+)')
# regex = re.compile(r'({)(.+)(})')


def parse_nkScript():
    """
    Parse .nk files, collects a list of nodes (in .nk string format) and their names.
    """
    # Get .nk contents
    filename = nuke.getInput('Nuke_Script','B:/nktst.nk')

    with open(filename,'r') as f:
        data = f.read()
        f.close()
    # print data

    regex = re.compile(r'(\w+)( {\n)(.+?)(\n}\n)', re.DOTALL)
    node_list = re.findall(regex,data)

    print "".join(node_list[-1]) # Example

    for node in node_list:
        node_string = "".join(node)
        #print node_string
        print re.search(r'name ([a-zA-Z0-9_:/.]+)', node_string).group(1)

    return node_list

def add_parse_to_menu():
    global parse_nkScript
    toolbar = nuke.menu('Nuke')
    toolbar.addCommand('File/Parse Nuke Script', parse_nkScript)

add_parse_to_menu()

# node_list = parse_nkScript(nuke.root().name())
