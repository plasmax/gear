__all__ = ['nuke_browserwidget','make_minibrowser','load_browserwidget']

import sys
from PySide import QtGui, QtCore

class nuke_browserwidget(QtGui.QDialog):
    def __init__(self):
        QtGui.QDialog.__init__(self)

        # Build the user interface
        # =======================================
        self.setWindowTitle('Nuke Mini Browser')
        self._layout = QtGui.QVBoxLayout()
        self.setLayout(self._layout)

        self.model = QtGui.QFileSystemModel()
        self.model.setRootPath('C:/')

        self.fileTree = QtGui.QTreeView()
        self.fileTree.setModel(self.model)
        self.fileTree.header().setResizeMode(QtGui.QHeaderView.ResizeToContents) 
        self.fileTree.setRootIndex(self.model.index('C:/'))
        self.fileTree.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self._layout .addWidget(self.fileTree)

        # Signals
        # =======================================
        self.fileTree.clicked.connect(self.clickedAnItem)

    def clickedAnItem(self, item):
        index_sel = self.fileTree.selectedIndexes()[0]
        item = self.model.filePath(index_sel)
        print item

def make_minibrowser():
    global mini_browser
    directory_path = 'C:/' # replace with any path
    mini_browser = nuke_browserwidget()
    mini_browser.show()
    mini_browser.resize(480,320)
    
    
# if __name__ == '__main__':
#     if not QtGui.QApplication.instance():
#         app = QtGui.QApplication(sys.argv)
#         make_panel(directory_path)
#         sys.exit(app.exec_())
#     else:

import nuke
import nukescripts  

def load_browserwidget():
    nukescripts.panels.__panels['uk.co.max.nuke_browserwidget']()

outliner_panel = nukescripts.panels.registerWidgetAsPanel('scripts.nuke_browserwidget', 'Nuke Mini Browser', 'uk.co.max.nuke_browserwidget', True )
nuke.menu('Nodes').addCommand('Scripts/Nuke Mini Browser', 'scripts.load_browserwidget()','shift+b')
nuke.menu('Nodes').addCommand('Scripts/Nuke Mini Browser Panel', 'scripts.make_minibrowser()','shift+alt+b')



