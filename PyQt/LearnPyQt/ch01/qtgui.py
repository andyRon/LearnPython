#!/opt/homebrew/bin/python3

import sys
from PyQt6 import QtGui
from PyQt6.QtWidgets import QApplication

def window():
   app = QApplication(sys.argv)
   w = QtGui.QWidget()
   b = QtGui.QLabel(w)
   b.setText("Hello World!")
   w.setGeometry(100,100,200,50)
   b.move(50,20)
   w.setWindowTitle("PyQt")
   w.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   window()