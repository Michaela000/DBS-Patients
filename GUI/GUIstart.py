#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import string
import sys
import csv
import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, \
    QWidget, QLabel

from GUI.GUIcheckPID import CheckPID
import GUI_Preoperative
from utils.helper_functions import General, Output
from dependencies import ROOTDIR

# Liebe Michaela, ich habe ein Paar Änderungen eingefügt, schau mal, ob Du das alles nachvollziehen kannst. Zwei Dinge,
# dich ich Dir raten würde (und die Du findest) ist zum einen das Auslagern von Funktionen, die man immer wieder
# benötigt bzw. die den Code unnötig lang machen (siehe auch ./utils/helper_functions.py). Außerdem habe ich angefangen,
# die Verknüpfungen für die anderen GUIs zu erstellen (siehe self.checkPID = CheckPID() ... ).
# TODO: 1. GUIcheckPID erweitern, sodass alle Daten von df drin vorkommen,
# TODO: 2. weitere Verknüfungen erstellen.
# TODO: 3. Eine Funktion erstellen, die alle csv Dateien aus dem Ordner ./temp löscht beim schließen von GUIstart


class CheckForPID(QDialog):
    """Very first GUI only providing a means to enter a PID (according to the ORBIS system at the
    Department of Neurology at the University Hospital of Gießen and Marburg. Several options are possible
    after entering a PID: 1. if existent -> GuiMain, 2. if inexistent enter data in general table"""

    def __init__(self, parent=None):
        """Initialize."""

        super().__init__(parent)
        self.setWindowTitle('Check for existence of subject in database')
        self.setGeometry(400, 100, 500, 300)  # left, right, width, height
        self.move(850, 425)

        self.layout = QVBoxLayout(self)  # entire layout for GUI
        self.content_box = QVBoxLayout(self)  # content of the box

        # ====================    Create Content for First Option box on Top left      ====================
        self.optionbox_guistart = QGroupBox('Please enter PID')
        self.settings_optionsbox1 = QVBoxLayout(self.optionbox_guistart)

        self.subj_name = QLabel('PID:\t\t')
        self.lineEditFilename = QLineEdit()

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
        self.button_close = QPushButton('Close GUI')
        self.button_close.clicked.connect(self.close)

        layout_buttons.addStretch(1)
        layout_buttons.addWidget(self.button_checkPID)
        layout_buttons.addWidget(self.button_close)

        # ====================    Add boxes and buttons to self.entire_layout      ====================
        self.layout.addLayout(self.content_box)
        self.layout.addLayout(layout_buttons)

    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
    def onClickedCheckPID(self):
        """when button is pressed, a series of checks are performed in order to retrieve data/to set the following GUI"""

        if not self.lineEditFilename.text():
            Output.msg_box(text='Missing input for the PID, please enter a number', title='Missing input')
            return

        filename = 'general_data.csv'
        df = General.import_dataframe(filename)
        PID2lookfor = self.lineEditFilename.text().lstrip('0') # string that is searched for in metadata file
        idx_PID = df.index[df['PID_ORBIS'] == int(PID2lookfor)].to_list()

        if not idx_PID:
            Output.msg_box(text='No corresponding subject found, please create new entry', title='Missing PID')
        elif len(idx_PID)>1:
            Output.msg_box(text='Too many entries, please double check file: {}'.format(filename),
                           title='Too many PID entries')
            return
        else:
            General.write_csv_temp(df, idx_PID) # writes data to temporary file, so that it may be used later
            self.checkPID = CheckPID()
            self.checkPID.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = CheckForPID()
    dlg.show()
    sys.exit(app.exec_())
