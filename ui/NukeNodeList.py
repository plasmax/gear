import re
import sys
from PySide.QtCore import * 
from PySide.QtGui import * 

filename = r"D:\allNodes.nk"
# filename = raw_input("Path to .nk file: ")
print filename

def parse_nkScript(filename):
    """
    Parse .nk files, collects a list of nodes (in .nk string format) and their names.
    """
    # Get .nk contents
    with open(filename,'r') as f:
        data = f.read()
        f.close()

    regex = re.compile(r'(\w+)( {\n)(.+?)(\n}\n)', re.DOTALL)
    node_list = re.findall(regex,data)

    node_data = [''.join(n) for n in node_list]
    node_names = [re.search('name (.+)\n',n).group(1) for n in node_data]
    return zip(node_names,node_data)


class CustomModel(QStandardItemModel):
    def __init__(self, filename):
        super(CustomModel,self).__init__()

        self.scene_data = parse_nkScript(filename)

        for nombre,datos in self.scene_data:
            item = QStandardItem(nombre)
            item.setData(datos,Qt.UserRole)
            self.appendRow(item)

    def mimeData(self, indexes):
        print indexes
        i = indexes[0]
        md = QMimeData()
        node_data = i.data(Qt.UserRole)
        print i.data(), node_data
        md.setText(node_data)
        #+':'+self.itemFromIndex(i).parent().text()) #just the name + parent to use in the drop to filter out acceptable drops
        return md

    def mimeTypes(self):
        return ['text/plain']  


class DragDropView(QTreeView):
    def __init__(self):
        super(DragDropView,self).__init__()
        self.model = CustomModel(filename)
        self.setModel(self.model)

        # Everything related to drag/drop
        print self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.DragDrop)
        self.setDragEnabled(True)
        self.setDropIndicatorShown(True)
        self.setDefaultDropAction(Qt.CopyAction)

class DragDropPanel(QWidget):
    def __init__(self):
        super(DragDropPanel, self).__init__()
        self.setWindowTitle('Drag and Drop Test')
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.dragDropView = DragDropView()
        self.layout.addWidget(self.dragDropView)

 
def main():
    global widget
    widget = DragDropPanel()
    widget.show()

if not QApplication.instance():
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        main()
        sys.exit(app.exec_())
else:
    import nukescripts.panels
    filename = nuke.getInput("Path to .nk file: ")
    main()
    nukescripts.registerWidgetAsPanel('nkNodeListPanel', 'Nuke Reader', 'uk.co.max.nkNodeListPanel' )

