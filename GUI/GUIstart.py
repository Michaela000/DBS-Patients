#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Hallo David. Ich habe versucht die drei TODO's umzusetzen aber bei dem Verbinden von den zwei GUI's bin ich mir noch sehr unsicher. Durch die erstellte Funktion kann ich bisher
# nur eine weitere Datei öffnen in der ich dann suchen kann, aber ich glaube das soll eher automatisch funktionieren oder?

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, \
    QWidget, QLabel, QFileDialog
import random
import string


class CheckForPID(QDialog):
    """Very first GUI only providing a means to enter a PID (according to the ORBIS system at the
    Department of Neurology at the University Hospital of Gießen and Marburg. Several options are possible
    after entering a PID: 1. if existent -> GuiMain, 2. if inexistent enter data in general table"""

    def __init__(self, parent=None):
        """Initialize."""
        # TODO: 1. code helper function to create random code of numbers and symbols
        # TODO: 2. make the text enter field wider and change geometry, respectively
        # TODO: 3. connect to other GUIs

        super().__init__(parent)
        self.setWindowTitle('Check for existence of subject in database')
        self.setGeometry(400, 100, 500, 300)  # left, right, width, height
        self.move(850, 425)

        self.layout = QVBoxLayout(self)  # entire layout for GUI
        self.content_box = QVBoxLayout(self)  # content of the box

        # ====================    Create Content for First Option box on Top left      ====================
        self.optionbox_guistart = QGroupBox('Please enter PID')
        self.settings_optionsbox1 = QVBoxLayout(self.optionbox_guistart)

        self.subj_name = QLabel('PID:\t\t', )
        self.lineEditFilename = QLineEdit()

        # Todo 2: Change the Width/Height of the text window
        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_name)
        lay1.addWidget(self.lineEditFilename)
        lay1.addStretch()

        self.settings_optionsbox1.addLayout(lay1)
        self.content_box.addWidget(self.optionbox_guistart)

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_buttons = QHBoxLayout()
        self.button_checkPID = QPushButton('Check for \nexistence')
        self.button_checkPID.clicked.connect(self.onClickedCheckPID)

        layout_buttons.addStretch(1)
        layout_buttons.addWidget(self.button_checkPID)

        # ====================    Add boxes and buttons to self.entire_layout      ====================
        self.layout.addLayout(self.content_box)
        self.layout.addLayout(layout_buttons)

        # In the next lines, actions are defined when Buttons are pressed

    # TODO 3: Connect with another GUI
    @QtCore.pyqtSlot()
    def onClickedCheckPID(self):
        self.PID_List()
        print('implement check for PID existence')

    def PID_List(self):
        filename = QFileDialog.getOpenFileName()
        print (filename)

    # Todo 1 - Create random String
    def get_random_alphanumeric_string(self):
        letters_and_digits = string.ascii_letters + string.digits
        result_str = ''.join((random.choice(letters_and_digits) for i in range(self)))
        print("Random alphanumeric String is:", result_str)

    get_random_alphanumeric_string(8)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = CheckForPID()
    dlg.show()
    sys.exit(app.exec_())
