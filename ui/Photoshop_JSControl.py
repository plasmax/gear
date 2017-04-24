__all__ = ['PhotoshopControl','load_psctrl']

import sys
import os

from PySide.QtGui import *
from PySide.QtCore import *
import _winreg
import subprocess
import time

class PhotoshopControl(QWidget):
    def __init__(self):
        super(PhotoshopControl, self).__init__()
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)

        self._btnwidget = QWidget()
        self._layout.addWidget(self._btnwidget)
        self._btnbar = QHBoxLayout()
        self._btnwidget.setLayout(self._btnbar)
        # self.script_document_page()
        self.btn_new_tab = QPushButton('New Tab')
        self._btnbar.addWidget(self.btn_new_tab)
        self.new_script_path = QLineEdit('C:\ps_js\include.jsx')
        self._btnbar.addWidget(self.new_script_path)
        self.tabWidget = QTabWidget()
        self._layout.addWidget(self.tabWidget)
        self.btn_new_tab.clicked.connect(self.new_tab)


    def new_tab(self):
        jsx_file = self.new_script_path.text()
        self.ww = ScriptPage(jsx_file)
        self.tabWidget.addTab(self.ww,self.ww.get_script_name())

class ScriptPage(QWidget):
    def __init__(self, script_path):
        super(ScriptPage, self).__init__()
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        #JScript path bar
        self._jswidget = QWidget()
        self._jslayout = QHBoxLayout()
        self._jswidget.setLayout(self._jslayout)

        # UI components
        self.js_path = QLineEdit(script_path)
        self.btn_loadjs = QPushButton('Load')
        self.btn_savejs = QPushButton('Save')
        self.ret_path = QLineEdit('c:\\temp\\ps_temp_ret.txt')
        self.ps_path = QLineEdit('C:\Program Files\Adobe\Adobe Photoshop CC 2017\Photoshop.exe')
        self.js_content = QPlainTextEdit()
        self.btn_shelf = QDialogButtonBox()
        self.btn_loadps = QPushButton('Load Photoshop')

        # Add to layout
        self._layout.addWidget(self._jswidget)
        self._jslayout.addWidget(self.js_path)
        self._jslayout.addWidget(self.btn_loadjs)
        self._jslayout.addWidget(self.btn_savejs)
        self._layout.addWidget(self.ps_path)
        self._layout.addWidget(self.js_content)
        self._layout.addWidget(self.btn_shelf)
        self._layout.addWidget(self.btn_loadps)
        
        # Signals
        self.btn_loadps.clicked.connect(self.loadps)
        self.btn_loadjs.clicked.connect(self.loadjs)
        self.btn_savejs.clicked.connect(self.savejs)

        print(self.get_script_name())

    def get_script_name(self):
        return self.js_path.text().split('\\')[-1].split('.')[0]

    def loadps(self):
        self.js_file = self.js_path.text()
        self.ps_exe = self.ps_path.text()
        print self.ps_exe
        if os.path.isfile(self.ps_exe):
            self.PS_APP = self.ps_exe
        else:
            self.PS_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, "SOFTWARE\\Adobe\\Photoshop\\110.0")
            print(self.PS_key)      
            self.PS_APP = _winreg.QueryValueEx(self.PS_key, 'ApplicationPath')[0] + 'Photoshop.exe'   

        # # Ensure the return file exists...
        # with open(self.js_file, 'w') as f:
        #         f.close()  

        # Establish the last time the temp file was modified. We use this to listen for changes. 
        self.savejs()
        self._last_mod_time = os.path.getmtime(self.js_file)      
        self.target = '"' + self.PS_APP +'"' + " " +  '"' + self.js_file + '"'
        ret = subprocess.Popen(self.target)     # Use ret later to return data from ps

    def loadjs(self):
        print self.js_content.toPlainText()
        if not self.js_content.toPlainText() == '':
            # if nuke.ask('Save Current?'):
            if self.check_before():
                self.savejs(js_file=self.open_file)
        self.open_file = self.js_path.text()
        # Check/Load default .js file
        if os.path.isfile(self.js_path.text()):
            with open(self.js_path.text(), 'r') as f:
                data = f.read()
                f.close()
            # print data
            self.js_content.document().setPlainText(data)

    def savejs(self,js_file=None):
        if js_file is None:
            self.js_file = self.js_path.text()
        else:
            self.js_file = js_file
        print self.js_file
        print self.js_content.toPlainText()
        # Get the path to the return file. Create it if it doesn't exist.
        if not os.path.exists(os.path.dirname(self.js_file)):
            os.makedirs(os.path.dirname(self.js_file))
        # write .js file
        with open(self.js_file, "wb") as f:
            f.write(self.js_content.toPlainText())

    def check_before(self):
        msgBox = QMessageBox()
        msgBox.setText("Has the document been modified?")
        # msgBox.setInformativeText("Do you want to save your changes?")
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Ignore)
        msgBox.setDefaultButton(QMessageBox.Save)
        ret = msgBox.exec_()

        if ret == QMessageBox.Save: # Save was clicked
            return True
        elif ret == QMessageBox.Ignore: # Don't save was clicked
            return False
        else: # should never be reached
            pass

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    photoshop_control = PhotoshopControl()
    photoshop_control.show()
    sys.exit(app.exec_())
else:
    import nuke
    import nukescripts
    def load_psctrl():
        nukescripts.panels.__panels['uk.co.max.PhotoshopJSIDE']()

    outliner_panel = nukescripts.panels.registerWidgetAsPanel('scripts.Photoshop_JSControl.PhotoshopControl', 'Photoshop JS IDE', 'uk.co.max.PhotoshopJSIDE', True )
    nuke.menu('Nodes').addCommand('Scripts/Photoshop JS IDE', 'scripts.load_psctrl()','shift+j')
    
    # def setup_JSControl():
    #     from scripts.Photoshop_JSControl import PhotoshopControl
    #     from scripts.Photoshop_JSControl import load_psctrl

    #     global PhotoshopControl
    #     global load_psctrl
    #     outliner_panel = nukescripts.panels.registerWidgetAsPanel('PhotoshopControl', 'Photoshop JS IDE', 'uk.co.max.PhotoshopJSIDE', True )

    #     node_toolbar = nuke.menu('Nodes')
    #     node_toolbar.addCommand('Scripts/Photoshop JS IDE', 'load_psctrl()','shift+j')
    #     return PhotoshopControl

    # setup_JSControl()



# # A Mini Python wrapper for the JS commands...
# class PhotoshopJSWrapper(object):
#     def __init__(self):
#         # Get the Photoshop exe path from the registry. 
#         self.PS_key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE, 
#                                       "SOFTWARE\\Adobe\\Photoshop\\110.0")
#         self.PS_APP = _winreg.QueryValueEx(self.PS_key, 'ApplicationPath')[0] + 'Photoshop.exe'          

#         # Get the path to the return file. Create it if it doesn't exist.
#         self.return_file = 'c:\\temp\\ps_temp_ret.txt'
#         if not os.path.exists('c:\\temp\\'):
#             os.mkdir('c:\\temp\\')

#         # Ensure the return file exists...
#         with open(self.return_file, 'w') as f:
#                 f.close()  
            
#         # Establish the last time the temp file was modified. We use this to listen for changes. 
#         self._last_mod_time = os.path.getmtime(self.return_file)         
        
#         # Temp file to store the .jsx commands. 
#         self.temp_jsx_file = "c:\\temp\\ps_temp_com.jsx"

#     def js_execute_command(self):
#         """Pass the commands to the subprocess module."""
#         self._compile_commands()
#         self.target = '"' + self.PS_APP +'"' + " " +  '"' + self.temp_jsx_file + '"'
#         prin(self.target)
#         ret = subprocess.Popen(self.target) 