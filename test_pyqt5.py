# Filename: test_pyqt5.py
"""Dialog-Style application."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QLabel

# Da stimmt etwas noch nicht. Ich erhalte bei beiden Optionen die gleiche Antowrt "Please Try Again!". 
# Ich schätze es liegt an dieser Zeile "btns.clicked.connect(greeting)". 
# Aber der Rest läuft. 

def greeting():
    """Function."""
    if QDialogButtonBox.Cancel:
        print('Please Try Again!')
    else:
        print('Thank You!')


class Dialog(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Dialog_Test')
        self.setGeometry(200, 100, 280, 170)
        self.move(850, 425)
        helloMsg = QLabel('<h1>Hello!</h1>', parent=self)
        helloMsg.move(15, 125)
        dlgLayout = QVBoxLayout()
        formLayout = QFormLayout()
        formLayout.addRow('Name:', QLineEdit())
        formLayout.addRow('Age:', QLineEdit())
        formLayout.addRow('Birthdate:', QLineEdit())
        formLayout.addRow('Job:', QLineEdit())

        dlgLayout.addLayout(formLayout)
        btns = QDialogButtonBox()
        btns.setStandardButtons(
           QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        btns.clicked.connect(greeting)

        dlgLayout.addWidget(btns)
        self.setLayout(dlgLayout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
