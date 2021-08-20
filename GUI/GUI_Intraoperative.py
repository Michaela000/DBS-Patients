# Hallo David. Vielen Dank für die Hilfe. Jetzt hat eigentlich alles geklappt.

# Ich bin heute nochmal alle GUI's durchgegangen und hab einiges nochmal geändert bzw. verbessert anhand Deiner Bilder.
# Dabei sind mir ein paar Sachen aufgefallen:
# 1. Sollen wir noch einen Callback_Savebutton einführen? Wenn ja gehört er dann zu GUIcheckPID?
# 2. ich bekomme die GUI_Main buttons nicht zentriert, obwohl addStretch da ist (das gilt auch für ein paar andere Buttons später in pre- post und intraoperative GUI)
# 3. die beiden if present Bilder sind etwas anders, weil wir dafür GUI_Start haben. Daher hab ich das bisher noch nicht verändert
# 4. Das Layout besonders von Preoperative ist noch etwas detaillierter als auf den Bildern, aber ich fand es eigentlich nicht so schlecht,
# deswegen habe ich es bisher nicht verändert, soll ich das noch tun?
# 5. Das Layout von Intra und Postoperative muss ich noch etwas anpassen. Ich habe ein paar Schwierigkeiten damit, die Wörter
#    "Right Hemisphere" und "Left Hemisphere" über die Tabelle zu bekommen und ich finde es sehr schwierig alle "Tests" in Postoperative
#    auf eine Höhe zu bekommen.

import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QGroupBox,  QSpacerItem, QSizePolicy, \
    QHBoxLayout, QFileDialog, QWidget, QGridLayout, QLineEdit, QLabel, QListWidget, QCheckBox
from GUI.GUI_Medication import MedicationDialog

textfield_width = 450

class IntraoperativeDialog(QDialog):
    """Dialog to introduce all important information of intraoperative patients. """

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        self.setWindowTitle('Please insert the data from the intraoperative patint contact ...')
        self.setGeometry(200, 100, 280, 170)
        self.move(400, 100)

        layout_general = QGridLayout(self)
        self.setLayout(layout_general)

        # Optionbox upper left corner
        self.optionbox1 = QGroupBox('Admissions')
        self.optionbox1Content = QVBoxLayout(self.optionbox1)
        layout_general.addWidget(self.optionbox1, 0, 0)

        self.admission_NCh = QLabel('Admission Neurosurgery (dd/mm/yyyy):\t')
        self.lineEditAdmNCh = QLineEdit()
        self.admission_Neur = QLabel('Admission Neurology (dd/mm/yyyy):\t')
        self.lineEditAdmNeur = QLineEdit()
        self.dismission_NCh = QLabel('Dismission Neurosurgery (dd/mm/yyyy):\t')
        self.lineEditDismNCh = QLineEdit()
        self.dismission_Neur = QLabel('Dismission Neurology (dd/mm/yyyy):\t')
        self.lineEditDismNeur = QLineEdit()

        box1line1 = QHBoxLayout()
        box1line1.addWidget(self.admission_NCh)
        box1line1.addWidget(self.lineEditAdmNCh)
        box1line1.addStretch()

        box1line2 = QHBoxLayout()
        box1line2.addWidget(self.admission_Neur)
        box1line2.addWidget(self.lineEditAdmNeur)
        box1line2.addStretch()

        box1line3 = QHBoxLayout()
        box1line3.addWidget(self.dismission_NCh)
        box1line3.addWidget(self.lineEditDismNCh)
        box1line3.addStretch()

        box1line4 = QHBoxLayout()
        box1line4.addWidget(self.dismission_Neur)
        box1line4.addWidget(self.lineEditDismNeur)
        box1line4.addStretch()

        self.optionbox1Content.addLayout(box1line1)
        self.optionbox1Content.addLayout(box1line2)
        self.optionbox1Content.addLayout(box1line3)
        self.optionbox1Content.addLayout(box1line4)
        self.optionbox1.setLayout(self.optionbox1Content)

        # Optionbox upper right corner
        self.optionbox2 = QGroupBox('Surgery')
        self.optionbox2Content = QVBoxLayout(self.optionbox2)
        layout_general.addWidget(self.optionbox2, 0, 1)

        self.surgeryDate = QLabel('Surgery Date (dd/mm/yyyy):\t\t')
        self.lineEditAdmNCh = QLineEdit()

        box2line1 = QHBoxLayout()
        box2line1.addWidget(self.dismission_NCh)
        box2line1.addWidget(self.lineEditDismNCh)
        box2line1.addStretch()

        self.target = QLabel('Target:\t\t\t\t\t')
        self.targetList = QListWidget()
        self.targetList.show()
        ls = ['STN', 'GPi', 'VLp', 'Other']
        for k in ls:
            self.targetList.addItem(k)

        box2line2 = QHBoxLayout()
        box2line2.addWidget(self.target)
        box2line2.addWidget(self.targetList)
        box2line2.addStretch()

        self.optionbox2Content.addLayout(box2line1)
        self.optionbox2Content.addLayout(box2line2)
        self.optionbox2.setLayout(self.optionbox2Content)

        # Optionbox middle left
        self.optionbox3 = QGroupBox('Intraoperative')
        self.optionbox3Content = QVBoxLayout(self.optionbox3)
        layout_general.addWidget(self.optionbox3, 1, 0)

        self.ReportNeurCheck = QCheckBox()
        self.ReportNeur = QLabel('Report Neurology\t\t')
        self.AwakePatientCheck = QCheckBox()
        self.AwakePatient = QLabel('Awake Patient')

        box3line1 = QHBoxLayout()
        box3line1.addWidget(self.ReportNeurCheck)
        box3line1.addWidget(self.ReportNeur)
        box3line1.addWidget(self.AwakePatientCheck)
        box3line1.addWidget(self.AwakePatient)
        box3line1.addStretch()

        self.ReportNeurSurgCheck = QCheckBox()
        self.ReportNeurSurg = QLabel('Report Neurosurgery\t')
        self.ProtocolNeurCheck = QCheckBox()
        self.ProtocolNeur = QLabel('Protocol Neurology')

        box3line2 = QHBoxLayout()
        box3line2.addWidget(self.ReportNeurSurgCheck)
        box3line2.addWidget(self.ReportNeurSurg)
        box3line2.addWidget(self.ProtocolNeurCheck)
        box3line2.addWidget(self.ProtocolNeur)
        box3line2.addStretch()

        self.DurationSurgery = QLabel('Duration surgery (min):')
        self.lineEditDurationSurgery = QLineEdit()
        self.Trajectories = QLabel('Trajectories:')
        self.lineEditTrajectories = QLineEdit()

        box3line3 = QHBoxLayout()
        box3line3.addWidget(self.DurationSurgery)
        box3line3.addWidget(self.lineEditDurationSurgery)
        box3line3.addWidget(self.Trajectories)
        box3line3.addWidget(self.lineEditTrajectories)
        box3line3.addStretch()

        self.testingNeur = QLabel('Testing Neurologist(s):')
        self.testingNeurList = QListWidget()
        self.testingNeurList.show()
        ls = ['Oehrn/Weber', 'Pedrosa', 'Waldthaler', 'Other']
        for k in ls:
            self.testingNeurList.addItem(k)

        box3line4 = QHBoxLayout()
        box3line4.addWidget(self.testingNeur)
        box3line4.addWidget(self.testingNeurList)
        box3line4.addStretch()

        self.optionbox3Content.addLayout(box3line1)
        self.optionbox3Content.addLayout(box3line2)
        self.optionbox3Content.addLayout(box3line3)
        self.optionbox3Content.addLayout(box3line4)

        self.optionbox3.setLayout(self.optionbox3Content)

        # Optionbox middle right
        self.optionbox4 = QGroupBox('System')
        self.optionbox4Content = QVBoxLayout(self.optionbox4)
        layout_general.addWidget(self.optionbox4, 1, 1)

        self.LeadImplanted = QLabel('Lead:\t\t\t')
        self.LeadImplantedList = QListWidget()
        self.LeadImplantedList.show()
        ls = ['Medtronic 3389', 'Medtronic 3389', 'Boston Scientific 2202-30/-45',
              'St. Jude 6146/6147/6148/6149', 'Other']
        for k in ls:
            self.LeadImplantedList.addItem(k)

        box4line1 = QHBoxLayout()
        box4line1.addWidget(self.LeadImplanted)
        box4line1.addWidget(self.LeadImplantedList)
        box4line1.addStretch()

        self.IPGImplanted = QLabel('IPG:\t\t\t')
        self.IPGImplantedList = QListWidget()
        self.IPGImplantedList.show()
        ls = ['Medtronic Activa PC', 'Medtronic Activa RC', 'Medtronic Activa SC',
              'Boston Scientific Vercise', 'Boston Scientific Vercise PC']
        for k in ls:
            self.IPGImplantedList.addItem(k)

        box4line2 = QHBoxLayout()
        box4line2.addWidget(self.IPGImplanted)
        box4line2.addWidget(self.IPGImplantedList)
        box4line2.addStretch()

        self.optionbox4Content.addLayout(box4line1)
        self.optionbox4Content.addLayout(box4line2)
        self.optionbox4.setLayout(self.optionbox4Content)

        # Optionbox lower middle left
        self.optionbox5 = QGroupBox('Coordinates DBS leads')
        self.optionbox5Content = QHBoxLayout(self.optionbox5)
        layout_general.addWidget(self.optionbox5, 2, 0)

        self.grid_coordinates_left = QGridLayout()
        self.grid_coordinates_leftCheck = QLabel('Left Hemisphere')
        for i in range(0, 8):
            for j in range(0, 4):
                if j == 0:
                    self.grid_coordinates_left.addWidget(QLabel(str(i)), i, j)
                else:
                    self.grid_coordinates_left.addWidget(QLineEdit(), i, j)

        self.grid_coordinates_right = QGridLayout()
        self.grid_coordinates_rightCheck = QLabel('Right Hemisphere')
        for i in range(0, 8):
            for j in range(0, 4):
                if j != 3:
                    # self.grid_coordinates_right.addItem(QSpacerItem(5, 1, QSizePolicy.Expanding, QSizePolicy.Expanding), i, j, 1, 1)
                    hspacer = QSpacerItem(QSizePolicy.Expanding, QSizePolicy.Minimum)
                    self.grid_coordinates_right.addItem(hspacer, 0, i, -1, 1)
                    self.grid_coordinates_right.addWidget(QLineEdit(), i, j)

                else:
                    self.grid_coordinates_right.addWidget(QLabel(str(i)), i, j)

        self.optionbox5Content.addStretch()
        self.optionbox5Content.addWidget(self.grid_coordinates_leftCheck)
        self.optionbox5Content.addLayout(self.grid_coordinates_left)
        self.optionbox5Content.addStretch()
        self.optionbox5Content.addWidget(self.grid_coordinates_rightCheck)
        self.optionbox5Content.addLayout(self.grid_coordinates_right)
        self.optionbox5Content.addLayout(self.grid_coordinates_right)
        self.optionbox5Content.addStretch()

        #optionbox lower middle right
        self.optionbox6 = QGroupBox('Activation')
        self.optionbox6Content = QVBoxLayout(self.optionbox6)
        layout_general.addWidget(self.optionbox6, 2, 1)

        self.PostopCTScanCheck = QCheckBox()
        self.PostopCTScan = QLabel('Postoperative CT Scan')
        self.ImplVERCISE_DBSCheck = QCheckBox()
        self.ImplVERCISE_DBS = QLabel('Implantation VERCISE DBS')
        self.ActiveVERCISE_DBSCheck = QCheckBox()
        self.ActiveVERCISE_DBS = QLabel('Activation VERCISE DBS')
        self.InclusionQualiPaCheck = QCheckBox()
        self.InclusionQualiPa = QLabel('Inclusion QualiPa')

        box6line1 = QHBoxLayout()
        box6line1.addWidget(self.PostopCTScanCheck)
        box6line1.addWidget(self.PostopCTScan)
        box6line1.addStretch()

        box6line2 = QHBoxLayout()
        box6line2.addWidget(self.ImplVERCISE_DBSCheck)
        box6line2.addWidget(self.ImplVERCISE_DBS)
        box6line2.addStretch()

        box6line3 = QHBoxLayout()
        box6line3.addWidget(self.ActiveVERCISE_DBSCheck)
        box6line3.addWidget(self.ActiveVERCISE_DBS)
        box6line3.addStretch()

        box6line4 = QHBoxLayout()
        box6line4.addWidget(self.InclusionQualiPaCheck)
        box6line4.addWidget(self.InclusionQualiPa)
        box6line4.addStretch()

        self.optionbox6Content.addLayout(box6line1)
        self.optionbox6Content.addLayout(box6line2)
        self.optionbox6Content.addLayout(box6line3)
        self.optionbox6Content.addLayout(box6line4)

        #optionbox 3th row left
        self.optionbox7 = QGroupBox('DBS settings after dismissal')
        self.optionbox7Content = QVBoxLayout(self.optionbox7)
        layout_general.addWidget(self.optionbox7, 3, 0)

        self.DBS_settings_left = QGridLayout()
        self.DBS_settings_leftCheck = QLabel ('Left Hemisphere')
        for i in range(0, 1):
            for j in range(0, 8):
                self.DBS_settings_left.addWidget(QLineEdit(), i, j)

        self.DBS_settings_right = QGridLayout()
        self.DBS_settings_rightCheck = QLabel ('Right Hemisphere')
        for i in range(0, 1):
            for j in range(0, 8):
                self.DBS_settings_right.addWidget(QLineEdit(), i, j)

        self.optionbox7Content.addWidget(self.DBS_settings_leftCheck)
        self.optionbox7Content.addLayout(self.DBS_settings_left)
        self.optionbox7Content.addWidget(self.DBS_settings_rightCheck)
        self.optionbox7Content.addLayout(self.DBS_settings_right)

        #optionbox 3th row right

        self.optionbox8 = QGroupBox('Amplitude, Pulse and Frequency')
        self.optionbox8Content = QVBoxLayout(self.optionbox8)
        layout_general.addWidget(self.optionbox8, 3, 1)

        self.AmplitudeLeft = QLabel('Amplitude Left [in mA]:')
        self.lineEditAmplitudeLeft = QLineEdit()
        self.PulseLeft = QLabel('Pulse Width Left [in µs]:')
        self.lineEditPulseLeft = QLineEdit()
        self.FrequencyLeft = QLabel('Frequency Left [in Hz]:')
        self.lineEditFrequencyLeft = QLineEdit()

        box8line1 = QHBoxLayout()
        box8line1.addWidget(self.AmplitudeLeft)
        box8line1.addWidget(self.lineEditAmplitudeLeft)
        box8line1.addWidget(self.PulseLeft)
        box8line1.addWidget(self.lineEditPulseLeft)
        box8line1.addWidget(self.FrequencyLeft)
        box8line1.addWidget(self.lineEditFrequencyLeft)
        box8line1.addStretch()

        self.AmplitudeRight = QLabel('Amplitude Right [in mA]:')
        self.lineEditAmplitudeRight = QLineEdit()
        self.PulseRight = QLabel('Pulse Width Right [in µs]:')
        self.lineEditPulseRight = QLineEdit()
        self.FrequencyRight = QLabel('Frequency Right [in Hz]:')
        self.lineEditFrequencyRight = QLineEdit()

        box8line2 = QHBoxLayout()
        box8line2.addWidget(self.AmplitudeRight)
        box8line2.addWidget(self.lineEditAmplitudeRight)
        box8line2.addWidget(self.PulseRight)
        box8line2.addWidget(self.lineEditPulseRight)
        box8line2.addWidget(self.FrequencyRight)
        box8line2.addWidget(self.lineEditFrequencyRight)
        box8line2.addStretch()

        self.optionbox8Content.addLayout(box8line1)
        self.optionbox8Content.addLayout(box8line2)
        self.optionbox8.setLayout(self.optionbox8Content)

    # buttons

        self.button_openGUI_Medication = QPushButton('Open GUI \nMedication')
        self.button_openGUI_Medication.setText("Medication")
        self.button_openGUI_Medication.setCheckable(True)

        self.button_save = QPushButton('Save')
        self.button_save.clicked.connect(self.onClickedSaveReturn)


        hlay_bottom = QHBoxLayout()
        hlay_bottom.addStretch(2)
        hlay_bottom.addWidget(self.button_openGUI_Medication)
        hlay_bottom.addWidget(self.button_save)
        hlay_bottom.addStretch(1)

        layout_general.addLayout(hlay_bottom, 4, 0, 1,3)



    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()

    def on_click(self):
        if self.button_openGUI_Medication.isChecked():  # selects three different options available
            dialog = MedicationDialog(parent=self)
        self.hide()
        if dialog.exec():
            pass
        self.show()

    def onClickedSaveReturn(self):
        print('Done!')
        self.hide()

        #self.saveFileDialog()

    def saveFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()", "test.txt", "All Files(*)",
                                                  options=options)
        print(fileName)

    # for opening
    def open_dialog_box(self):
        option = QFileDialog.Options()
        # first parameter is self; second is the Window Title, third title is Default File Name, fourth is FileType,
        # fifth is options
        file = QFileDialog.getOpenFileName(self, "Save File Window Title", "default.txt", "All Files (*)",
                                           options=option)
        print(file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = IntraoperativeDialog()
    dlg.show()
    sys.exit(app.exec_())
