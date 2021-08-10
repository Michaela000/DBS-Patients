# Hi David, da ich mich bislang erst mit Preoperative bschäftigt habe, stehen hier noch keine Informationen drin.
# Aber ich wollte die GUI schon einmal erstellen, damit GUIMain durchlaufen kann.

import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QFileDialog, QWidget, QRadioButton, QGridLayout, QLineEdit, QLabel


class IntraoperativeDialog(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super(IntraoperativeDialog, self).__init__(parent)

        grid = QGridLayout(self)
        grid.addWidget(self.createGroup1(), 0, 0)
        self.setLayout(grid)

        self.setWindowTitle('Intraoperative Information')
        self.setGeometry(200, 100, 280, 170)
        self.move(850, 200)

    def createGroup1(self):
        groupBox1 = QGroupBox("Basic Information")
        info1 = QRadioButton("PID")
        info2 = QRadioButton("ID")
        info3 = QRadioButton("Gender")
        info4 = QRadioButton("Diagnosis")
        info1.setChecked(True)
        info2.setChecked(True)
        info3.setChecked(True)
        info4.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info1)
        vbox.addWidget(info2)
        vbox.addWidget(info3)
        vbox.addWidget(info4)
        vbox.addStretch(1)
        groupBox1.setLayout(vbox)
        return groupBox1

        layout_bottom = QHBoxLayout()
        self.button_save_return = QPushButton('Save settings \nand return')
        self.button_save_return.clicked.connect(self.onClickedSaveReturn)
        self.button_close = QPushButton('Save and \nclose')
        self.button_close.clicked.connect(self.close)

        layout_bottom.addStretch(1)
        layout_bottom.addWidget(self.button_save_return)
        layout_bottom.addWidget(self.button_close)

        self.layout.addWidget(self.optionbox1)
        self.layout.addLayout(layout_bottom)

    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
    def onClickedSaveReturn(self):
        self.saveFileDialog()

    def close(self):
        self.saveFileDialog()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "test.txt", "All Files(*)", options=options)
        print(fileName)

    # for opening
    def open_dialog_box (self):
        option = QFileDialog.Options()
        # first parameter is self; second is the Window Title, third title is Default File Name, fourth is FileType,
        # fifth is options
        file = QFileDialog.getOpenFileName(self, "Save File Window Title", "default.txt", "All Files (*)", options=option)
        print(file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = IntraoperativeDialog()
    dlg.show()
    sys.exit(app.exec_())

