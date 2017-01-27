import sys
from PySide import QtGui, QtCore

class nuke_browserwidget(QtGui.QDialog):
    def __init__(self, path):
        QtGui.QDialog.__init__(self)

        # Build the user interface
        # =======================================
        self.setWindowTitle('Nuke Mini Browser')
        self._layout = QtGui.QVBoxLayout()
        self.setLayout(self._layout)

        self.model = QtGui.QFileSystemModel()
        self.model.setRootPath(path)

        self.fileTree = QtGui.QTreeView()
        self.fileTree.setModel(self.model)
        self.fileTree.header().setResizeMode(QtGui.QHeaderView.ResizeToContents) 
        self.fileTree.setRootIndex(self.model.index(path))
        self.fileTree.setDragDropMode(QtGui.QAbstractItemView.DragDrop)
        self._layout .addWidget(self.fileTree)

        # Signals
        # =======================================
        self.fileTree.clicked.connect(self.clickedAnItem)

    def clickedAnItem(self, item):
        index_sel = self.fileTree.selectedIndexes()[0]
        item = self.model.filePath(index_sel)
        print item

# mini_browser = nuke_browserwidget('B:/')
# mini_browser.show()

def make_panel():
    global mini_browser
    mini_browser = nuke_browserwidget('B:/')
    mini_browser.show()
    mini_browser.resize(480,320)

if __name__ == '__main__':
    if not QtGui.QApplication.instance():
        app = QtGui.QApplication(sys.argv)
        make_panel()
        sys.exit(app.exec_())
    else:
        make_panel()



