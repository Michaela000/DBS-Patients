import sys
import GUI_Main
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, \
    QWidget, QLabel, QComboBox

from GUI.GUIgeneral_data import CustomLineEdit
from utils.helper_functions import General

textfield_width = 450


class TemporaryFile(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.calendarWindow = QWidget()
        self.setWindowTitle('Please enter all data for the new subject:')
        self.setGeometry(400, 100, 1000, 400)  # left, right, width, height
        self.move(850, 425)

        self.layout = QVBoxLayout(self)  # entire layout for GUI
        self.content_box = QVBoxLayout(self)  # content of the box
        textfield_width = 450

        # ====================    Create Content for only option box       ====================
        self.optionbox_guistart = QGroupBox('General data for new subject in the temporary file:')
        self.settings_optionsbox1 = QVBoxLayout(self.optionbox_guistart)

        self.subj_surname = QLabel('Surname:\t\t')
        self.lineEditSurname = QLineEdit()

        self.lineEditSurname.setFixedWidth(textfield_width)
        self.lineEditSurname.setFixedHeight(50)

        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_surname)
        lay1.addWidget(self.lineEditSurname)
        lay1.addStretch()

        self.subj_name = QLabel('Name:\t\t\t')
        self.lineEditName = QLineEdit()

        self.lineEditName.setFixedWidth(textfield_width)
        self.lineEditName.setFixedHeight(50)

        lay2 = QHBoxLayout()
        lay2.addWidget(self.subj_name)
        lay2.addWidget(self.lineEditName)
        lay2.addStretch()

        self.subj_name = QLabel('Name Suffix:\t\t')
        self.lineEditNameSuffix = QLineEdit()

        self.lineEditNameSuffix.setFixedWidth(textfield_width)
        self.lineEditNameSuffix.setFixedHeight(50)

        lay3 = QHBoxLayout()
        lay3.addWidget(self.subj_name)
        lay3.addWidget(self.lineEditNameSuffix)
        lay3.addStretch()

        self.subj_birthdate = QLabel('Birthdate:\t\t')
        self.lineEditBirthdate = CustomLineEdit()
        self.lineEditBirthdate.setFixedWidth(textfield_width)
        self.lineEditBirthdate.clicked.connect(self.open_calendar)

        lay4 = QHBoxLayout()
        lay4.addWidget(self.subj_birthdate)
        lay4.addWidget(self.lineEditBirthdate)
        lay4.addStretch()

        self.subj_address = QLabel('Address:\t\t')
        self.lineEditaddress = CustomLineEdit()
        self.lineEditaddress.setFixedWidth(textfield_width)
        self.lineEditaddress.setFixedHeight(50)

        lay5 = QHBoxLayout()
        lay5.addWidget(self.subj_address)
        lay5.addWidget(self.lineEditaddress)
        lay5.addStretch()

        self.subj_PID = QLabel('PID-ORBIS:\t\t')
        self.lineEditPID = QLineEdit()

        self.lineEditPID.setFixedWidth(textfield_width)
        self.lineEditPID.setFixedHeight(50)

        lay6 = QHBoxLayout()
        lay6.addWidget(self.subj_PID)
        lay6.addWidget(self.lineEditPID)
        lay6.addStretch()

        self.subj_ID = QLabel('ID:\t\t\t')
        self.lineEditID = QLineEdit()
        self.lineEditID.setText(General.generate_code(8))

        self.lineEditID.setFixedWidth(textfield_width)
        self.lineEditID.setFixedHeight(50)

        lay7 = QHBoxLayout()
        lay7.addWidget(self.subj_ID)
        lay7.addWidget(self.lineEditID)
        lay7.addStretch()

        self.subj_gender = QLabel('Gender:\t\t\t')
        self.lineEditGender = QComboBox()
        self.lineEditGender.addItems(['female', 'male', 'diverse'])
        self.lineEditGender.setFixedWidth(textfield_width)
        self.lineEditGender.setFixedHeight(50)

        lay8 = QHBoxLayout()
        lay8.addWidget(self.subj_gender)
        lay8.addWidget(self.lineEditGender)
        lay8.addStretch()

        self.subj_diagnosis = QLabel('Diagnosis:\t\t\t')
        self.lineEditdiagnosis = QComboBox()
        self.lineEditdiagnosis.addItems(['hypokinetic-rigid parkinson-syndrome (PD1)', 'tremordominant parkinson-syndrome (PD2)', 'mixed-type parkinson-syndrome (PD3)', 'dystonia (DT)', 'essential tremor (ET)', 'Other'])
        self.lineEditdiognosis.setFixedWidth(textfield_width)
        self.lineEditdiagnosis.setFixedHeight(50)

        lay8 = QHBoxLayout()
        lay8.addWidget(self.subj_gender)
        lay8.addWidget(self.lineEditGender)
        lay8.addStretch()

        self.settings_optionsbox1.addLayout(lay1)
        self.settings_optionsbox1.addLayout(lay2)
        self.settings_optionsbox1.addLayout(lay3)
        self.settings_optionsbox1.addLayout(lay4)
        self.settings_optionsbox1.addLayout(lay6)
        self.settings_optionsbox1.addLayout(lay7)
        self.settings_optionsbox1.addLayout(lay8)
        self.content_box.addWidget(self.optionbox_guistart)

        layout_buttons = QHBoxLayout()
        self.button_savegeneraltemp = QPushButton('Add general data \ninformation in temporary file')
        self.button_savegeneraltemp.clicked.connect(self.onClickedSaveGeneralTemp)
        self.button_close = QPushButton('Close GUI')
        self.button_close.clicked.connect(self.close)

        layout_buttons.addStretch(1)
        layout_buttons.addWidget(self.button_savegeneraltemp)
        layout_buttons.addWidget(self.button_close)

        # ====================    Add boxes and buttons to self.entire_layout      ====================
        self.layout.addLayout(self.content_box)
        self.layout.addLayout(layout_buttons)

    def onClickedSaveGeneralTemp(self):
        open(GUI_Main)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = TemporaryFile()
    dlg.show()
    sys.exit(app.exec_())