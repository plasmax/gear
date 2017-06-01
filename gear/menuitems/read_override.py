__all__ = ['read_from']

import os
import re
import operator
from random import shuffle

import nuke
import nukescripts


def read_from():
    """
    Override for the standard Image/Read item in the nuke Nodes menu.
    If any write nodes are selected, this function creates a read node
    with the write nodes' paths.
    If not, nukescripts.create_read() is called.
    """
    selected_nodes = nuke.selectedNodes()
    write_nodes = [node for node in selected_nodes if node.Class() == 'Write']
    if any(write_nodes):
        for n in write_nodes:
            file_value = n['file'].value()
            xp = n['xpos'].value()
            yp = n['ypos'].value()+80
            read_node = nuke.nodes.Read(
                                file=file_value,
                                xpos=xp,
                                ypos=yp
                                )
    else:
        nukescripts.create_read()

def file_sequence(node):
    """
    Checks a node's file path to see if a sequence exists in the folder.
    If so returns the sequence length
    """
    if node.knob('file'):
        file_value = node['file'].value()
        directory_name = os.path.dirname(file_value)
        directory_list = os.listdir(directory_name)
        file_name = os.path.basename(file_value)
        file_name = os.path.splitext(file_name)[0]
        file_name = file_name.split('%')
        print file_name[0]
        print ( r'\.' + file_value.split('.')[1])
        pattern = '({0})(\d+)(\w+)?({1})'.format(
                                file_name[0],
                                ( r'\.' + file_value.split('.')[1])
                                )

        regx = re.compile(pattern)
        sq = []
        for f in directory_list:
            if re.search(regx,f):
                search = re.search(regx,f).groups()
                print search
                first, num, mid, last = search
                sq.append((first, num, last))
        sq.sort(key=operator.itemgetter(1))
    
    else:
        return None

if __name__ == "__main__":
    file_sequence(nuke.selectedNode())