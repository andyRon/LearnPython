import sys
from PyQt5.QtWidgets import *

if __name__ == '__main__':
    app = QApplication([])
    label = QLabel("Hello World! PyQt!")
    label.show()
    sys.exit(app.exec_())