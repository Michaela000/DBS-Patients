import os
import sys

import pandas as pds
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, \
    QWidget, QButtonGroup

from GUI.GUI_Intraoperative import IntraoperativeDialog
from GUI.GUI_Postoperative import PostoperativeDialog
from GUI.GUI_Preoperative_old import PreoperativeDialog
from dependencies import ROOTDIR


class ChooseGUI(QDialog):
    """This GUI is responsible to open further GUI'S:
    1. Preoperative 2. Intraoperative 3. Postoperative"""

    def __init__(self, parent=None):
        """Initialize GUImain, a window in which all other "sub-GUIs" may be called from."""

        super().__init__(parent)
        try:
            subj_details = pds.read_csv(os.path.join(ROOTDIR, 'temp', 'current_subj.csv'))  # Read currently used subj.
        except FileNotFoundError:
            print('Data not found! Please make sure that a file named "current_subj.csv" exists in the "temp" folder')
            return

        # ====================    Create General Layout      ====================
        self.layout = QVBoxLayout()  # layout for the central widget
        widget = QWidget(self)
        widget.setLayout(self.layout)

        self.setWindowTitle('Choose GUI for subj with PID: {}'.format(str(int(subj_details.code))))
        self.setGeometry(400, 100, 500, 300)  # left, right, width, height
        self.move(750, 375)

        # ====================    Create Content for Buttons of GUImain      ====================
        self.button_openGUI_Preoperative = QPushButton('Open GUI \nPreoperative')
        self.button_openGUI_Preoperative.setText("Preoperative")
        self.button_openGUI_Preoperative.setCheckable(True)

        self.button_openGUI_Intraoperative = QPushButton('Intraoperative')
        self.button_openGUI_Intraoperative.setText("Intraoperative")
        self.button_openGUI_Intraoperative.setCheckable(True)

        self.button_openGUI_Postoperative = QPushButton('Postoperative')
        self.button_openGUI_Postoperative.setText("Postoperative")
        self.button_openGUI_Postoperative.setCheckable(True)

        self.button_close = QPushButton('Close GUI')
        self.button_close.clicked.connect(self.close)

        # ====================    Add ButtonGroup and buttons to self.layout      ====================
        btn_grp = QButtonGroup(widget)
        btn_grp.setExclusive(True)
        btn_grp.addButton(self.button_openGUI_Preoperative)
        btn_grp.addButton(self.button_openGUI_Intraoperative)
        btn_grp.addButton(self.button_openGUI_Postoperative)
        btn_grp.buttonClicked.connect(self.on_click)

        self.layout.addStretch(1)
        self.layout.addWidget(self.button_openGUI_Preoperative)
        self.layout.addWidget(self.button_openGUI_Intraoperative)
        self.layout.addWidget(self.button_openGUI_Postoperative)
        self.layout.addWidget(self.button_close)
        self.layout.addStretch(1)

    # ====================    In the next lines, actions are defined when Buttons are pressed      ====================
    @QtCore.pyqtSlot()
    def on_click(self):
        if self.button_openGUI_Preoperative.isChecked():  # selects three different options available
            dialog = PreoperativeDialog(parent=self)
        elif self.button_openGUI_Intraoperative.isChecked():
            dialog = IntraoperativeDialog(parent=self)
        else:
            dialog = PostoperativeDialog(parent=self)

        self.hide()
        if dialog.exec():
            pass
        self.show()

    def close_all(self):
        """closes GUImain when work is done!"""
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = ChooseGUI()
    dlg.show()
    sys.exit(app.exec_())
