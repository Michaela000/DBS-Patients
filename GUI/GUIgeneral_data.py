import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, \
    QWidget, QLabel
import pandas as pds
import os
import numpy as np

from utils.helper_functions import General, Output


# Cool! Ich habe ein Paar kleine Änderungen eingefügt. Bei mir ging es nicht, deswegen habe ich den Befehl am Anfang,
# bei dem sich die Funktion selbst nochmal aufruft weggemacht. Dann habe ich angefangen, die einzelnen
# self.lineEditFilename umzubenennen. Du musst immer dran denken, dass Du die möglichst eindeutig benennen willst, da
# Du sonst die Information später nicht extrahieren kannst.


class CheckForGeneralData(QDialog):
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

        # ====================    Create Content for only option box       ====================
        self.optionbox_guistart = QGroupBox('Please enter general data for new subject:')
        self.settings_optionsbox1 = QVBoxLayout(self.optionbox_guistart)

        self.subj_surname = QLabel('Surname:\t\t')
        self.lineEditSurname = QLineEdit()

        self.lineEditSurname.setFixedWidth(150)
        self.lineEditSurname.setFixedHeight(50)

        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_surname)
        lay1.addWidget(self.lineEditSurname)
        lay1.addStretch()

        self.subj_name = QLabel('Name:\t\t')
        self.lineEditName = QLineEdit()

        self.lineEditName.setFixedWidth(150)
        self.lineEditName.setFixedHeight(50)

        lay2 = QHBoxLayout()
        lay2.addWidget(self.subj_name)
        lay2.addWidget(self.lineEditName)
        lay2.addStretch()

        self.subj_name_suffix = QLabel('Name Suffix:\t\t\t')
        self.lineEditNameSuffix = QLineEdit()

        self.lineEditNameSuffix.setFixedWidth(150)
        self.lineEditNameSuffix.setFixedHeight(50)

        lay3 = QHBoxLayout()
        lay3.addWidget(self.subj_name_suffix)
        lay3.addWidget(self.lineEditNameSuffix)
        lay3.addStretch()

        self.subj_birthdate = QLabel('Birthdate:\t\t')
        self.lineEditBirthdate = QLineEdit()

        self.lineEditBirthdate.setFixedWidth(150)
        self.lineEditBirthdate.setFixedHeight(50)

        lay4 = QHBoxLayout()
        lay4.addWidget(self.subj_birthdate)
        lay4.addWidget(self.lineEditBirthdate)
        lay4.addStretch()

        self.subj_address = QLabel('Address:\t\t')
        self.lineEditAddress = QLineEdit()

        self.lineEditAddress.setFixedWidth(150)
        self.lineEditAddress.setFixedHeight(50)

        lay5 = QHBoxLayout()
        lay5.addWidget(self.subj_address)
        lay5.addWidget(self.lineEditAddress)
        lay5.addStretch()

        self.subj_PID = QLabel('PID-ORBIS:\t\t')
        self.lineEditPID = QLineEdit()

        self.lineEditPID.setFixedWidth(150)
        self.lineEditPID.setFixedHeight(50)

        lay6 = QHBoxLayout()
        lay6.addWidget(self.subj_PID)
        lay6.addWidget(self.lineEditPID)
        lay6.addStretch()

        self.subj_ID = QLabel('ID:\t\t\t')
        self.lineEditID = QLineEdit()

        self.lineEditID.setFixedWidth(150)
        self.lineEditID.setFixedHeight(50)

        lay7 = QHBoxLayout()
        lay7.addWidget(self.subj_ID)
        lay7.addWidget(self.lineEditID)
        lay7.addStretch()

        self.subj_gender = QLabel('Gender:\t\t\t')
        self.lineEditGender = QLineEdit()

        self.lineEditGender.setFixedWidth(150)
        self.lineEditGender.setFixedHeight(50)

        lay8 = QHBoxLayout()
        lay8.addWidget(self.subj_gender)
        lay8.addWidget(self.lineEditGender)
        lay8.addStretch()

        self.subj_diagnosis = QLabel('Diagnosis:\t\t')
        self.lineEditDiagnosis = QLineEdit()

        self.lineEditDiagnosis.setFixedWidth(150)
        self.lineEditDiagnosis.setFixedHeight(50)

        lay9 = QHBoxLayout()
        lay9.addWidget(self.subj_diagnosis)
        lay9.addWidget(self.lineEditDiagnosis)
        lay9.addStretch()

        self.subj_side_dominance = QLabel('Side Dominance:\t\t')
        self.lineEditSideDominance = QLineEdit()

        self.lineEditSideDominance.setFixedWidth(150)
        self.lineEditSideDominance.setFixedHeight(50)

        lay10 = QHBoxLayout()
        lay10.addWidget(self.subj_side_dominance)
        lay10.addWidget(self.lineEditSideDominance)
        lay10.addStretch()

        self.settings_optionsbox1.addLayout(lay1)
        self.settings_optionsbox1.addLayout(lay2)
        self.settings_optionsbox1.addLayout(lay3)
        self.settings_optionsbox1.addLayout(lay4)
        self.settings_optionsbox1.addLayout(lay5)
        self.settings_optionsbox1.addLayout(lay6)
        self.settings_optionsbox1.addLayout(lay7)
        self.settings_optionsbox1.addLayout(lay8)
        self.settings_optionsbox1.addLayout(lay9)
        self.settings_optionsbox1.addLayout(lay10)
        self.content_box.addWidget(self.optionbox_guistart)

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_buttons = QHBoxLayout()
        self.button_addgeneraldata = QPushButton('Add general data \ninformation')
        # self.button_addgeneraldata.clicked.connect(self.onClickedaddgeneraldata)
        self.button_close = QPushButton('Close GUI')
        self.button_close.clicked.connect(self.close)

        layout_buttons.addStretch(1)
        layout_buttons.addWidget(self.button_addgeneraldata)
        layout_buttons.addWidget(self.button_close)

        # ====================    Add boxes and buttons to self.entire_layout      ====================
        self.layout.addLayout(self.content_box)
        self.layout.addLayout(layout_buttons)
        # self.fill_forms() # Sorry, ist an der falschen Stelle eingefügt. Ändere ich noch.

    def fill_forms(self):
        """in this function all text fields are filled with content (iff available) """
        df = General.import_dataframe(os.path.join(os.path.join(os.getcwd(), 'data', 'general_data.csv')))
        try:
            idx = pds.read_csv(os.path.join(os.getcwd(), 'temp', 'current_subj.csv')).iloc[0].idx
        except FileNotFoundError:
            idx = np.nan

        self.lineEditSurname.setText(df.iloc[idx].Surname)
        self.lineEditName.setText(df.iloc[idx].Name)

    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
    def onClickedCheckPID(self):
        """when button is pressed, a series of checks are performed in order to retrieve data/to set the following
        GUI """

        if not self.lineEditFilename.text():
            Output.msg_box(text='Missing input for the PID, please enter a number', title='Missing input')
            return

        filename = 'General.csv'
        df = General.import_dataframe(filename)
        PID2lookfor = self.lineEditFilename.text().lstrip('0')  # string that is searched for in metadata file
        idx_General_data = df.index[
            df['Surname', 'Name', 'Name Suffix', 'Birthdate', 'Address', 'PID_ORBIS', 'ID', 'Gender',
               'Diagnosis', 'Side Dominance'] == int(PID2lookfor)].to_list()

        if not idx_General_data:
            Output.msg_box(text='Please create a new patient', title='Missing Patient')
        elif len(idx_General_data) > 1:
            Output.msg_box(text='Too many entries, please double check file: {}'.format(filename),
                           title='Too many general information entries')
            return
        else:
            General.write_csv_temp(df, idx_General_data)  # writes data to temporary file, so that it may be used later
            self.checkforgeneraldata.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = CheckForGeneralData()
    dlg.show()
    sys.exit(app.exec_())
