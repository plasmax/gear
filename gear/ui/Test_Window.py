__all__ = ['NukeTestWindow','load_nuke_test_window']

import nuke
import PySide.QtCore as QtCore
import PySide.QtGui as QtGui
from nukescripts import panels

class NukeTestWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setLayout(QtGui.QVBoxLayout())
        self.myTable    = QtGui.QTableWidget()
        self.myTable.header = ['Date', 'Files', 'Size', 'Path' ]
        self.myTable.size = [ 75, 375, 85, 600 ]
        self.myTable.setColumnCount(len(self.myTable.header))
        self.myTable.setHorizontalHeaderLabels(self.myTable.header)
        self.myTable.setSelectionMode(QtGui.QTableView.ExtendedSelection)
        self.myTable.setSelectionBehavior(QtGui.QTableView.SelectRows)
        self.myTable.setSortingEnabled(1)
        self.myTable.sortByColumn(1, QtCore.Qt.DescendingOrder)
        self.myTable.setAlternatingRowColors(True)
        self.myTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.myTable.setRowCount(50)
        self.layout().addWidget(self.myTable)
        self.myTable.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))
        self.setSizePolicy(QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding))

nuke_tw = panels.registerWidgetAsPanel('gear.NukeTestWindow', 'Test table panel', 'uk.co.max.NukeTestWindow', True)

def load_nuke_test_window():
    pane = nuke.getPaneFor('DAG.1')
    nuke_tw.addToPane(pane)