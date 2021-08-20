import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QFileDialog, QWidget, QGridLayout, QLabel, QLineEdit, QComboBox, QCheckBox
from GUI.GUI_Medication import MedicationDialog


class PostoperativeDialog(QDialog):
    """Dialog to introduce all important information of postoperative patients."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        self.setWindowTitle('Postoperative Information')
        self.setGeometry(200, 100, 280, 170)
        self.move(850, 200)

        layout = QGridLayout(self)
        self.setLayout(layout)

        # Create one optionbox for the time being left
        self.optionbox1 = QGroupBox('Important Dates')
        self.optionbox1Content = QVBoxLayout(self.optionbox1)
        layout.addWidget(self.optionbox1, 0, 0)

        self.subj_Admission_Nch = QLabel('Admission Neurosurgery (dd/mm/yyyy):\t')
        self.lineEditAdmission_Nch = QLineEdit()
        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_Admission_Nch)
        lay1.addWidget(self.lineEditAdmission_Nch)
        lay1.addStretch()

        self.subj_Admission_NR = QLabel('Admission Neurology (dd/mm/yyyy):\t')
        self.lineEditAdmission_NR = QLineEdit()
        lay2 = QHBoxLayout()
        lay2.addWidget(self.subj_Admission_NR)
        lay2.addWidget(self.lineEditAdmission_NR)
        lay2.addStretch()

        self.subj_Dismission_Nch = QLabel('Dismission Neurosurgery (dd/mm/yyyy):')
        self.lineEditDismission_Nch = QLineEdit()
        lay3 = QHBoxLayout()
        lay3.addWidget(self.subj_Dismission_Nch)
        lay3.addWidget(self.lineEditDismission_Nch)
        lay3.addStretch()

        self.subj_Dismission_NR = QLabel('Dismission Neurology (dd/mm/yyyy):\t')
        self.lineEditDismission_NR = QLineEdit()
        lay4 = QHBoxLayout()
        lay4.addWidget(self.subj_Dismission_NR)
        lay4.addWidget(self.lineEditDismission_NR)
        lay4.addStretch()

        self.subj_Surgery = QLabel('Surgery Date (dd/mm/yyyy):\t\t')
        self.lineEditSurgery = QLineEdit()
        lay5 = QHBoxLayout()
        lay5.addWidget(self.subj_Surgery)
        lay5.addWidget(self.lineEditSurgery)
        lay5.addStretch()

        self.subj_Last_Revision = QLabel('Last Revision (dd/mm/yyyy):\t\t')
        self.lineEditLast_Revision = QLineEdit()
        lay6 = QHBoxLayout()
        lay6.addWidget(self.subj_Last_Revision)
        lay6.addWidget(self.lineEditLast_Revision)
        lay6.addStretch()

        self.subj_Outpatient_Contact = QLabel('Outpatient Contact (dd/mm/yyyy):\t')
        self.lineEditOutpatient_Contact = QLineEdit()
        lay7 = QHBoxLayout()
        lay7.addWidget(self.subj_Outpatient_Contact)
        lay7.addWidget(self.lineEditOutpatient_Contact)
        lay7.addStretch()

        self.optionbox1Content.addLayout(lay1)
        self.optionbox1Content.addLayout(lay2)
        self.optionbox1Content.addLayout(lay3)
        self.optionbox1Content.addLayout(lay4)
        self.optionbox1Content.addLayout(lay5)
        self.optionbox1Content.addLayout(lay6)
        self.optionbox1Content.addLayout(lay7)
        self.optionbox1.setLayout(self.optionbox1Content)

        # Create second optionbox top right
        self.optionbox2 = QGroupBox('Reason')
        self.optionbox2Content = QVBoxLayout(self.optionbox2)
        layout.addWidget(self.optionbox2, 0, 1)

        self.subj_reason = QLabel('Reason:\t\t')
        self.lineEditreason = QComboBox()
        self.lineEditreason.addItems(['3-month follow-up', '6-month follow-up', '12-month follow-up', '24-month follow-up', '36-month follow-up', 'Adverse event', 'IPG Problem', 'Lead Dislocation', 'Other'])
        self.lineEditreason.setFixedHeight(20)
        lay8 = QHBoxLayout()
        lay8.addWidget(self.subj_reason)
        lay8.addWidget(self.lineEditreason)
        lay8.addStretch()

        self.subj_Adverse_Event = QLabel('Adverse Events:\t')
        self.lineEditAdverse_Event = QLineEdit()
        self.lineEditAdverse_Event.setFixedWidth(300)
        self.lineEditAdverse_Event.setFixedHeight(50)
        lay9 = QHBoxLayout()
        lay9.addWidget(self.subj_Adverse_Event)
        lay9.addWidget(self.lineEditAdverse_Event)
        lay9.addStretch()

        self.optionbox2Content.addLayout(lay8)
        self.optionbox2Content.addLayout(lay9)
        self.optionbox2.setLayout(self.optionbox2Content)

        # Create third optionbox on the second row left
        self.optionbox3 = QGroupBox('Reports')
        self.optionbox3Content = QVBoxLayout(self.optionbox3)
        layout.addWidget(self.optionbox3, 1, 0)

        self.ReportNeurCheck = QCheckBox()
        self.ReportNeur = QLabel('Report Neurology \t\t')
        self.ReportNeurosurgeryCheck = QCheckBox()
        self.ReportNeurosurgery = QLabel('Report Neurosurgery\t')
        self.PatProgrammerCheck = QCheckBox()
        self.PatProgrammer = QLabel('Patient Programmer in use')

        box2line1 = QHBoxLayout()
        box2line1.addWidget(self.ReportNeurCheck)
        box2line1.addWidget(self.ReportNeur)
        box2line1.addWidget(self.ReportNeurosurgeryCheck)
        box2line1.addWidget(self.ReportNeurosurgery)
        box2line1.addWidget(self.PatProgrammerCheck)
        box2line1.addWidget(self.PatProgrammer)
        box2line1.addStretch()

        self.PostopCTCheck = QCheckBox()
        self.PostopCT = QLabel('Postoperative CT Scan\t')
        self.BatteryReplacementCheck = QCheckBox()
        self.BatteryReplacement = QLabel('Battery Replacement\t')
        self.PlannedVisitCheck = QCheckBox()
        self.PlannedVisit = QLabel('Planned Visit')

        box2line2 = QHBoxLayout()
        box2line2.addWidget(self.PostopCTCheck)
        box2line2.addWidget(self.PostopCT)
        box2line2.addWidget(self.BatteryReplacementCheck)
        box2line2.addWidget(self.BatteryReplacement)
        box2line2.addWidget(self.PlannedVisitCheck)
        box2line2.addWidget(self.PlannedVisit)
        box2line2.addStretch()

        self.QualiPaCheck = QCheckBox()
        self.QualiPa = QLabel('QualiPa Visit')

        box2line3 = QHBoxLayout()
        box2line3.addWidget(self.QualiPaCheck)
        box2line3.addWidget(self.QualiPa)

        self.optionbox3Content.addLayout(box2line1)
        self.optionbox3Content.addLayout(box2line2)
        self.optionbox3Content.addLayout(box2line3)
        self.optionbox3.setLayout(self.optionbox3Content)

        #optionbox 4: 2th row, right

        self.optionbox4 = QGroupBox('Tests')
        self.optionbox4Content = QVBoxLayout(self.optionbox4)
        layout.addWidget(self.optionbox4, 1, 1)

        self.UPDRSI = QLabel('UPDRS I:\t\t')
        self.lineEditUPDRSI = QLineEdit()
        self.UPDRSIV = QLabel('UPDRS IV:')
        self.lineEditUPDRSIV = QLineEdit()
        self.TSS = QLabel('TSS:\t')
        self.lineEditTSS = QLineEdit()
        self.CGICPat = QLabel('CGIC patient:\t')
        self.lineEditCGICPat = QLineEdit()
        self.CGICClinician = QLabel('CGIC clinician and cargiver:\t')
        self.lineEditCGICClinician = QLineEdit()

        box4line1 = QHBoxLayout()
        box4line1.addWidget(self.UPDRSI)
        box4line1.addWidget(self.lineEditUPDRSI)
        box4line1.addWidget(self.UPDRSIV)
        box4line1.addWidget(self.lineEditUPDRSIV)
        box4line1.addWidget(self.TSS)
        box4line1.addWidget(self.lineEditTSS)
        box4line1.addWidget(self.CGICPat)
        box4line1.addWidget(self.lineEditCGICPat)
        box4line1.addWidget(self.CGICClinician)
        box4line1.addWidget(self.lineEditCGICClinician)
        box4line1.addStretch()

        self.UPDRSON = QLabel('UPDRS On:\t')
        self.lineEditUPDRSON = QLineEdit()
        self.UPDRSII = QLabel('UPDRS II:\t\t')
        self.lineEditUPDRSII = QLineEdit()
        self.HRUQ = QLabel('HRUQ:\t')
        self.lineEditHRUQ = QLineEdit()
        self.MoCa = QLabel('MoCa:\t')
        self.lineEditMoCa = QLineEdit()
        self.MMST = QLabel('MMST:\t')
        self.lineEditMMST = QLineEdit()
        self.BDIII = QLabel('BDI-II:\t')
        self.lineEditBDIII = QLineEdit()
        self.NMSQ = QLabel('NMSQ:\t')
        self.lineEditNMSQ = QLineEdit()

        box4line2 = QHBoxLayout()
        box4line2.addWidget(self.UPDRSON)
        box4line2.addWidget(self.lineEditUPDRSON)
        box4line2.addWidget(self.UPDRSII)
        box4line2.addWidget(self.lineEditUPDRSII)
        box4line2.addWidget(self.HRUQ)
        box4line2.addWidget(self.lineEditHRUQ)
        box4line2.addWidget(self.MoCa)
        box4line2.addWidget(self.lineEditMoCa)
        box4line2.addWidget(self.MMST)
        box4line2.addWidget(self.lineEditMMST)
        box4line2.addWidget(self.BDIII)
        box4line2.addWidget(self.lineEditBDIII)
        box4line2.addWidget(self.NMSQ)
        box4line2.addWidget(self.lineEditNMSQ)
        box4line2.addStretch()

        self.UPDRSOff = QLabel('UPDRS Off:\t')
        self.lineEditUPDRSOff = QLineEdit()
        self.HY = QLabel('H&Y:\t')
        self.lineEditHY = QLineEdit()
        self.EQ5D = QLabel('EQ5D:\t')
        self.lineEditEQ5D = QLineEdit()
        self.DemTect = QLabel('DemTect:\t')
        self.lineEditDemTect = QLineEdit()
        self.PDQ8 = QLabel('PDQ8:\t')
        self.lineEditPDQ8 = QLineEdit()
        self.PDQ39 = QLabel('PDQ39:\t')
        self.lineEditPDQ39 = QLineEdit()
        self.SE = QLabel('S&E:\t')
        self.lineEditSE = QLineEdit()

        box4line3 = QHBoxLayout()
        box4line3.addWidget(self.UPDRSOff)
        box4line3.addWidget(self.lineEditUPDRSOff)
        box4line3.addWidget(self.HY)
        box4line3.addWidget(self.lineEditHY)
        box4line3.addWidget(self.EQ5D)
        box4line3.addWidget(self.lineEditEQ5D)
        box4line3.addWidget(self.DemTect)
        box4line3.addWidget(self.lineEditDemTect)
        box4line3.addWidget(self.PDQ8)
        box4line3.addWidget(self.lineEditPDQ8)
        box4line3.addWidget(self.PDQ39)
        box4line3.addWidget(self.lineEditPDQ39)
        box4line3.addWidget(self.SE)
        box4line3.addWidget(self.lineEditSE)
        box4line3.addStretch()

        self.UDDRSOn = QLabel('UDDRS On:\t')
        self.lineEditUDDRSOn = QLineEdit()
        self.TRSOn = QLabel('TRS On:\t')
        self.lineEditTRSOn = QLineEdit()

        box4line4 = QHBoxLayout()
        box4line4.addWidget(self.UDDRSOn)
        box4line4.addWidget(self.lineEditUDDRSOn)
        box4line4.addWidget(self.TRSOn)
        box4line4.addWidget(self.lineEditTRSOn)
        box4line4.addStretch()

        self.UDDRSOff = QLabel('UDDRS Off:\t')
        self.lineEditUDDRSOff = QLineEdit()
        self.TRSOff = QLabel('TRS Off:\t')
        self.lineEditTRSOff = QLineEdit()

        box4line5 = QHBoxLayout()
        box4line5.addWidget(self.UDDRSOff)
        box4line5.addWidget(self.lineEditUDDRSOff)
        box4line5.addWidget(self.TRSOff)
        box4line5.addWidget(self.lineEditTRSOff)
        box4line5.addStretch()

        self.optionbox4Content.addLayout(box4line1)
        self.optionbox4Content.addLayout(box4line2)
        self.optionbox4Content.addLayout(box4line3)
        self.optionbox4Content.addLayout(box4line4)
        self.optionbox4Content.addLayout(box4line5)
        self.optionbox4.setLayout(self.optionbox4Content)


        # optionbox 5 row 3 left

        self.optionbox5 = QGroupBox('DBS settings after dismissal')
        self.optionbox5Content = QVBoxLayout(self.optionbox5)
        layout.addWidget(self.optionbox5, 3, 0)

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

        self.optionbox5Content.addWidget(self.DBS_settings_leftCheck)
        self.optionbox5Content.addLayout(self.DBS_settings_left)
        self.optionbox5Content.addWidget(self.DBS_settings_rightCheck)
        self.optionbox5Content.addLayout(self.DBS_settings_right)

        #optionbox 6: 3rd row right

        self.optionbox6 = QGroupBox('Amplitude, Pulse and Frequency')
        self.optionbox6Content = QVBoxLayout(self.optionbox6)
        layout.addWidget(self.optionbox6, 3, 1)

        self.AmplitudeLeft = QLabel('Amplitude Left [in mA]:')
        self.lineEditAmplitudeLeft = QLineEdit()
        self.PulseLeft = QLabel('Pulse Width Left [in µs]:')
        self.lineEditPulseLeft = QLineEdit()
        self.FrequencyLeft = QLabel('Frequency Left [in Hz]:')
        self.lineEditFrequencyLeft = QLineEdit()

        box6line1 = QHBoxLayout()
        box6line1.addWidget(self.AmplitudeLeft)
        box6line1.addWidget(self.lineEditAmplitudeLeft)
        box6line1.addWidget(self.PulseLeft)
        box6line1.addWidget(self.lineEditPulseLeft)
        box6line1.addWidget(self.FrequencyLeft)
        box6line1.addWidget(self.lineEditFrequencyLeft)
        box6line1.addStretch()

        self.AmplitudeRight = QLabel('Amplitude Right [in mA]:')
        self.lineEditAmplitudeRight = QLineEdit()
        self.PulseRight = QLabel('Pulse Width Right [in µs]:')
        self.lineEditPulseRight = QLineEdit()
        self.FrequencyRight = QLabel('Frequency Right [in Hz]:')
        self.lineEditFrequencyRight = QLineEdit()

        box6line2 = QHBoxLayout()
        box6line2.addWidget(self.AmplitudeRight)
        box6line2.addWidget(self.lineEditAmplitudeRight)
        box6line2.addWidget(self.PulseRight)
        box6line2.addWidget(self.lineEditPulseRight)
        box6line2.addWidget(self.FrequencyRight)
        box6line2.addWidget(self.lineEditFrequencyRight)
        box6line2.addStretch()

        self.optionbox6Content.addLayout(box6line1)
        self.optionbox6Content.addLayout(box6line2)
        self.optionbox6.setLayout(self.optionbox6Content)

    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
    def onClickedSaveReturn(self):
        self.saveFileDialog()

    def close(self):
        self.saveFileDialog()

    def on_click(self):
        if self.button_openGUI_Medication.isChecked():  # selects three different options available
            dialog = MedicationDialog(parent=self)
        self.hide()
        if dialog.exec():
            pass
        self.show()

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
    dlg = PostoperativeDialog()
    dlg.show()
    sys.exit(app.exec_())

