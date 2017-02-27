import os
import re
import operator
from random import shuffle

import nuke
import nukescripts


def write_from():
    """
    Override for the standard Image/Write item in the nuke Nodes menu.
    If any write nodes are selected, this function creates a write node
    below each with the read nodes' paths.
    If not, nuke.createNode('Write') is called.
    """
    selected_nodes = nuke.selectedNodes()
    read_nodes = [node for node in selected_nodes if node.Class() == 'Read']
    if any(read_nodes):
        for n in read_nodes:
            file_value = n['file'].value()
            write_node = nuke.nodes.Write(
                                inputs=[n],
                                file=file_value,
                                )
    else:
        for n in selected_nodes:
            nuke.nodes.Write(inputs=[n])
