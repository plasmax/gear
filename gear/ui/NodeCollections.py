__all__ = ['NodePanel','node_collections','create_collector_node']

from PySide.QtGui import *
from PySide.QtCore import *
import nukescripts
import nuke

class NodePanel(QDialog):
    """
    A PySide QDialog panel that can be displayed in a 
        Node Panel (via a PyCustom_Knob), 
        Nuke Panel Dock (nukescripts.registerWidgetAsPanel), 
        or QDialog window (widget.show()) parented to the Nuke Main Window.
        Stores/Retrieves data from a node in the scene.
    """
    def __init__(self, node=None, parent=None):
        super(NodePanel, self).__init__()
        if not parent == None:
                self.setParent(parent)
        self.node = node
        self._layout = QGridLayout()
        self.setLayout(self._layout)

        self._model = QStandardItemModel()
        self.listWidget = QListView()
        self.listWidget.setModel(self._model)
        self._layout.addWidget(self.listWidget)
        self.testButton = QPushButton('Close')
        self._layout.addWidget(self.testButton)
        self.testButton.clicked.connect(self.closeDialog)

        # self.setWindowFlags(Qt.Tool)
        #self.setWindowFlags(Qt.WindowStaysOnTopHint)

    def closeDialog(self):
        self.close()
        
    def makeUI(self):
        return self

    def updateValue(self):
        pass

def node_collections():
    nuke_main_window = _nuke_main_window()
    # widget = NodePanel()
    pane = nuke.getPaneFor('DAG.1')
    widget = NodePanel(parent=pane)
    # # widget = NodePanel(parent=nuke_main_window)
    widget.setParent(nuke_main_window)
    widget.show()
    # # widget.raise_()
    # nukescripts.registerWidgetAsPanel('widget', 'Node Collector', 'uk.co.max.NodeCollector', True )
    # nukescripts.restorePanel('uk.co.max.NodeCollector')

def create_collector_node():
    noop = nuke.nodes.NoOp()
    pyknob = nuke.PyCustom_Knob( "MyWidget", "", "widget" ) 
    noop.addKnob(pyknob)