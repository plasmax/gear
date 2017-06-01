__all__ = ['CustomModel','DragDropView','Outliner','outliner_panel', 'load_outliner']

from PySide.QtGui import *
from PySide.QtCore import *
import nukescripts
import nuke

class CustomModel(QStandardItemModel):
    def __init__(self):
        super(CustomModel,self).__init__()
        self.setHorizontalHeaderLabels (['Name','Label','Properties','Enabled'])

    def mimeData(self, indexes):
        print indexes
        i = indexes[0]
        md = QMimeData()
        node = i.data(Qt.UserRole)
        print i.data()
        node_data = self.tcl_node(node)
        md.setText(node_data)
        return md

    def mimeTypes(self):
        return ['text/plain']  

    def tcl_node(self, node):
        node_data = node.Class() + ' {'
        node_data += node.writeKnobs(nuke.WRITE_NON_DEFAULT_ONLY | nuke.TO_VALUE)
        node_data += '\n}'
        return node_data

class DragDropView(QTreeView):
    def __init__(self):
        super(DragDropView,self).__init__()

        # Everything related to drag/drop
        print self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)
        self.setDefaultDropAction(Qt.CopyAction)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

class Outliner(QWidget):
    """
    Maya's Outliner for Nuke
    How to import: from gear.ui.Nuke_Outliner import *
    How to reload: reload(gear.ui.Nuke_Outliner)
    pane = nuke.getPaneFor('DAG.1')
    nukescripts.panels.registerWidgetAsPanel('Outliner', 'Nuke10 Outliner', 'uk.co.max.NukeOutliner', True ).addToPane(pane)
    # Select item == select 'object' (node or geo)
    # Edit list item name => change node name
    # Label column
    # Enable/disable
    """
    def __init__(self):
        super(Outliner, self).__init__()
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self.treeWidget = DragDropView()
        self._layout.addWidget(self.treeWidget)

        self._model = CustomModel()
        self.treeWidget.setModel(self._model)

        # Signals
        self.treeWidget.clicked.connect(self.select_node)

        self.build_list()

    def build_list(self):
        nodes = nuke.allNodes()
        for n in nodes:
            item = QStandardItem(n.fullName())
            item.setData(n,Qt.UserRole)
            self._model.appendRow(item)

    def select_node(self, index):
        node = index.data(Qt.UserRole)
        print node.fullName()
        node_fullName = index.data(Qt.DisplayRole)
        node.setSelected(True)

    def makeUI(self): # Here in case I decide to add this to a PyCustom knob 
        return self

    def updateValue(self):
        pass

outliner_panel = nukescripts.panels.registerWidgetAsPanel('gear.Outliner', 'Nuke10 Outliner', 'uk.co.max.NukeOutliner', True )
nuke.menu('Nodes').addCommand('Scripts/Outliner', 'gear.load_outliner()','shift+o')

def load_outliner():
    nukescripts.panels.__panels['uk.co.max.NukeOutliner']()