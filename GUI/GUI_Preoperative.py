# Hallo David
# Super danke für die Hilfe. Der Schritt hat schon einmal geklappt aber ich schaffe es immer noch nicht
# das Ganze mit dem grid.layout zu verknüpfen. Wenn ich es so lassen würde, dann könnte man nicht alle Punkte auf dem
# Bildschirm sehen. Ich fand es vorher eigentlich sehr schön mit dem QGridLayout. Dabei erhalte ich allerdings die
# Fehlermeldung, dass er optionbox 1-7 nicht findet. Habe versucht das Debug-Tool zu benutzen, aber ich bin mir nicht so
# sicher, ob ich das so genau bisher verstanden habe.

# Sobald Preoperative.py steht werde ich das gleiche für Postoperative und Intraoperative machen.
# Bei Preoperative bin ich mir bei einigen Begriffen immer noch nicht sicher: Outpat_Contact; nch (habe ich diese zu der
# richtigen Gruppe geordnet?
# und sind fpcit_spect, icVRCS und inexVRCS Tests? Hab sie derzeit in diese Kategorie einsortiert.

import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QFileDialog, QWidget, QRadioButton, QGridLayout, QLineEdit, QLabel, QComboBox


textfield_width = 450


class PreoperativeDialog(QDialog):
    """Dialog to introduce the medication at a specific date. All unrelated """

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)


        self.setWindowTitle('Preoperative Information')
        self.setGeometry(200, 100, 280, 170)
        self.move(850, 200)

        self.layout = QVBoxLayout(self)


        grid = QGridLayout(self)
        grid.addWidget(self.optionbox1(), 0, 0)
        grid.addWidget(self.optionbox2(), 0, 1)
        grid.addWidget(self.optionbox3(), 0, 2)
        grid.addWidget(self.optionbox4(), 1, 0)
        grid.addWidget(self.optionbox5(), 1, 1)
        grid.addWidget(self.optionbox6(), 1, 2)
        grid.addWidget(self.optionbox7(), 2, 0)
        self.setLayout(grid)


        self.optionbox1 = QGroupBox('General data')
        self.settings_list = QVBoxLayout(self.optionbox1)


        # ====================    Create Content for First Option box on Top left      ====================
        self.subj_PID = QLabel('PID:\t\t')
        self.lineEditPID = QLineEdit()
        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_PID)
        lay1.addWidget(self.lineEditPID)
        lay1.addStretch()

        self.subj_ID = QLabel('ID:\t\t')
        self.lineEditID = QLineEdit()
        lay2 = QHBoxLayout()
        lay2.addWidget(self.subj_ID)
        lay2.addWidget(self.lineEditID)
        lay2.addStretch()

        self.subj_gender = QLabel('Gender:\t\t')
        self.lineEditGender = QComboBox()
        self.lineEditGender.addItems(['female', 'male', 'diverse'])
        self.lineEditGender.setFixedHeight(50)
        lay3 = QHBoxLayout()
        lay3.addWidget(self.subj_gender)
        lay3.addWidget(self.lineEditGender)
        lay3.addStretch()

        self.subj_diagnosis = QLabel('Diagnosis:\t')
        self.lineEditDiagnosis = QComboBox()
        self.lineEditDiagnosis.addItems(['Hypokinetic-rigid parkinson-syndrome (PD1)',
                                         'Tremordominant parkinson-syndrome(PD2)',
                                         'Mixed-type parkinson-syndrome (PD3)',
                                         'Dystonia (DT)',
                                         'Essential tremor (ET)',
                                         'Other'])

        self.lineEditDiagnosis.setFixedWidth(textfield_width)
        self.lineEditDiagnosis.setFixedHeight(50)
        lay4 = QHBoxLayout()
        lay4.addWidget(self.subj_diagnosis)
        lay4.addWidget(self.lineEditDiagnosis)
        lay4.addStretch()

        self.subj_firstDiagnosed = QLabel('First Diagnosed:\t')
        self.lineEditfirstDiagnosed = QLineEdit()
        lay5 = QHBoxLayout()
        lay5.addWidget(self.subj_firstDiagnosed)
        lay5.addWidget(self.lineEditfirstDiagnosed)
        lay5.addStretch()

        self.settings_list.addLayout(lay1)
        self.settings_list.addLayout(lay2)
        self.settings_list.addLayout(lay3)
        self.settings_list.addLayout(lay4)
        self.settings_list.addLayout(lay5)


        self.optionbox2 = QGroupBox('Reports')
        self.settings_list = QVBoxLayout(self.optionbox2)

        # ====================    Create Content for Second Option box on Top Right     ====================
        self.subj_Admission = QLabel('Admission:\t')
        self.lineEditAdmission = QLineEdit()
        lay6 = QHBoxLayout()
        lay6.addWidget(self.subj_Admission)
        lay6.addWidget(self.lineEditAdmission)
        lay6.addStretch()

        self.subj_Dismissal = QLabel('Dismissal:\t')
        self.lineEditDismissal = QLineEdit()
        lay7 = QHBoxLayout()
        lay7.addWidget(self.subj_Dismissal)
        lay7.addWidget(self.lineEditDismissal)
        lay7.addStretch()

        self.subj_Report = QLabel('Report:\t\t')
        self.lineEditReport = QLineEdit()
        lay8 = QHBoxLayout()
        lay8.addWidget(self.subj_Report)
        lay8.addWidget(self.lineEditReport)
        lay8.addStretch()

        self.subj_ReportPreop = QLabel('Report Preop:\t')
        self.lineEditReportPreop = QLineEdit()
        lay9 = QHBoxLayout()
        lay9.addWidget(self.subj_ReportPreop)
        lay9.addWidget(self.lineEditReportPreop)
        lay9.addStretch()

        self.settings_list.addLayout(lay6)
        self.settings_list.addLayout(lay7)
        self.settings_list.addLayout(lay8)
        self.settings_list.addLayout(lay9)

        self.optionbox3 = QGroupBox('Files/Scans')
        self.settings_list = QVBoxLayout(self.optionbox3)

        # ====================    Create Content for Third Option box on Top Right     ====================
        self.subj_Video = QLabel('Video:\t')
        self.lineEditVideo = QLineEdit()
        lay10 = QHBoxLayout()
        lay10.addWidget(self.subj_Video)
        lay10.addWidget(self.lineEditVideo)
        lay10.addStretch()

        self.subj_VideoFile = QLabel('Video File:\t')
        self.lineEditVideoFile = QLineEdit()
        lay11 = QHBoxLayout()
        lay11.addWidget(self.subj_VideoFile)
        lay11.addWidget(self.lineEditVideoFile)
        lay11.addStretch()

        self.subj_MRT = QLabel('MRT:\t\t')
        self.lineEditMRT = QLineEdit()
        lay12 = QHBoxLayout()
        lay12.addWidget(self.subj_MRT)
        lay12.addWidget(self.lineEditMRT)
        lay12.addStretch()

        self.settings_list.addLayout(lay10)
        self.settings_list.addLayout(lay11)
        self.settings_list.addLayout(lay12)

        self.optionbox4 = QGroupBox('DBS Decision')
        self.settings_list = QVBoxLayout(self.optionbox4)

        # ====================    Create Content for Fourth Option box on Top Right     ====================
        self.subj_OutpatContact = QLabel('Outpat Contact:\t')
        self.lineEditOutpatContact = QLineEdit()
        lay13 = QHBoxLayout()
        lay13.addWidget(self.subj_OutpatContact)
        lay13.addWidget(self.lineEditOutpatContact)
        lay13.addStretch()

        self.subj_nch = QLabel('nch:\t')
        self.lineEditnch = QLineEdit()
        lay14 = QHBoxLayout()
        lay14.addWidget(self.subj_nch)
        lay14.addWidget(self.lineEditnch)
        lay14.addStretch()

        self.subj_Briefing = QLabel('Briefing:\t\t')
        self.lineEditBriefing = QLineEdit()
        lay15 = QHBoxLayout()
        lay15.addWidget(self.subj_Briefing)
        lay15.addWidget(self.lineEditBriefing)
        lay15.addStretch()

        self.subj_BriefingDoctor = QLabel('Briefing Doctor:\t')
        self.lineEditBriefingDoctor = QLineEdit()
        lay16 = QHBoxLayout()
        lay16.addWidget(self.subj_BriefingDoctor)
        lay16.addWidget(self.lineEditBriefingDoctor)
        lay16.addStretch()

        self.subj_DBSConference = QLabel('DBS Conference:\t')
        self.lineEditDBSConference = QLineEdit()
        lay17 = QHBoxLayout()
        lay17.addWidget(self.subj_DBSConference)
        lay17.addWidget(self.lineEditDBSConference)
        lay17.addStretch()

        self.subj_DecisionDBS = QLabel('Decision DBS:\t\t')
        self.lineEditDecisionDBS = QLineEdit()
        lay18 = QHBoxLayout()
        lay18.addWidget(self.subj_DecisionDBS)
        lay18.addWidget(self.lineEditDecisionDBS)
        lay18.addStretch()

        self.settings_list.addLayout(lay13)
        self.settings_list.addLayout(lay14)
        self.settings_list.addLayout(lay15)
        self.settings_list.addLayout(lay16)
        self.settings_list.addLayout(lay17)
        self.settings_list.addLayout(lay18)


        self.optionbox5 = QGroupBox('LEDD')
        self.settings_list = QVBoxLayout(self.optionbox5)

        # ====================    Create Content for Fifth Option box on Top Right     ====================
        self.subj_LEDD = QLabel('LEDD:\t')
        self.lineEditLEDD = QLineEdit()
        lay19 = QHBoxLayout()
        lay19.addWidget(self.subj_LEDD)
        lay19.addWidget(self.lineEditLEDD)
        lay19.addStretch()

        self.settings_list.addLayout(lay19)

        self.optionbox6 = QGroupBox('Tests')
        self.settings_list = QVBoxLayout(self.optionbox6)

        # ====================    Create Content for Sixth Option box on Top Right     ====================
        self.subj_BDI2 = QLabel('BDI2:\t')
        self.lineEditBDI2 = QLineEdit()
        lay20 = QHBoxLayout()
        lay20.addWidget(self.subj_BDI2)
        lay20.addWidget(self.lineEditBDI2)
        lay20.addStretch()

        self.subj_DemTect = QLabel('DemTect:\t')
        self.lineEditDemTect = QLineEdit()
        lay21 = QHBoxLayout()
        lay21.addWidget(self.subj_DemTect)
        lay21.addWidget(self.lineEditDemTect)
        lay21.addStretch()

        self.subj_EQ5D = QLabel('EQ5D:\t\t')
        self.lineEditEQ5D = QLineEdit()
        lay22 = QHBoxLayout()
        lay22.addWidget(self.subj_EQ5D)
        lay22.addWidget(self.lineEditEQ5D)
        lay22.addStretch()

        self.subj_fpcit_spect = QLabel('fpcit_spect:\t')
        self.lineEditfpcit_spect = QLineEdit()
        lay23 = QHBoxLayout()
        lay23.addWidget(self.subj_fpcit_spect)
        lay23.addWidget(self.lineEditfpcit_spect)
        lay23.addStretch()

        self.subj_HRUQ = QLabel('HRUQ:\t')
        self.lineEditHRUQ = QLineEdit()
        lay24 = QHBoxLayout()
        lay24.addWidget(self.subj_HRUQ)
        lay24.addWidget(self.lineEditHRUQ)
        lay24.addStretch()

        self.subj_HYOn = QLabel('H&Y On:\t\t')
        self.lineEditHYOn = QLineEdit()
        lay25 = QHBoxLayout()
        lay25.addWidget(self.subj_HYOn)
        lay25.addWidget(self.lineEditHYOn)
        lay25.addStretch()

        self.subj_HYOff = QLabel('H&Y Off:\t\t')
        self.lineEditHYOff= QLineEdit()
        lay26 = QHBoxLayout()
        lay26.addWidget(self.subj_HYOff)
        lay26.addWidget(self.lineEditHYOff)
        lay26.addStretch()

        self.subj_icVRCS = QLabel('icVRCS:\t')
        self.lineEditicVRCS = QLineEdit()
        lay27 = QHBoxLayout()
        lay27.addWidget(self.subj_icVRCS)
        lay27.addWidget(self.lineEditicVRCS)
        lay27.addStretch()

        self.subj_inexVRCS = QLabel('inexVRCS:\t')
        self.lineEditinexVRCS = QLineEdit()
        lay28 = QHBoxLayout()
        lay28.addWidget(self.subj_inexVRCS)
        lay28.addWidget(self.lineEditinexVRCS)
        lay28.addStretch()

        self.subj_MMST = QLabel('MMST:\t\t')
        self.lineEditMMST = QLineEdit()
        lay29 = QHBoxLayout()
        lay29.addWidget(self.subj_MMST)
        lay29.addWidget(self.lineEditMMST)
        lay29.addStretch()

        self.subj_MoCa = QLabel('MoCa:\t')
        self.lineEditMoCa = QLineEdit()
        lay30 = QHBoxLayout()
        lay30.addWidget(self.subj_MoCa)
        lay30.addWidget(self.lineEditMoCa)
        lay30.addStretch()

        self.subj_NMSQ = QLabel('NMSQ:\t')
        self.lineEditNMSQ = QLineEdit()
        lay31 = QHBoxLayout()
        lay31.addWidget(self.subj_NMSQ)
        lay31.addWidget(self.lineEditNMSQ)
        lay31.addStretch()

        self.subj_PDQ8 = QLabel('PDQ8:\t\t')
        self.lineEditPDQ8 = QLineEdit()
        lay32 = QHBoxLayout()
        lay32.addWidget(self.subj_PDQ8)
        lay32.addWidget(self.lineEditPDQ8)
        lay32.addStretch()

        self.subj_PDQ39 = QLabel('PDQ39:\t')
        self.lineEditPDQ39 = QLineEdit()
        lay33 = QHBoxLayout()
        lay33.addWidget(self.subj_PDQ39)
        lay33.addWidget(self.lineEditPDQ39)
        lay33.addStretch()

        self.subj_SE = QLabel('S&E:\t\t')
        self.lineEditSE = QLineEdit()
        lay34 = QHBoxLayout()
        lay34.addWidget(self.subj_SE)
        lay34.addWidget(self.lineEditSE)
        lay34.addStretch()

        self.subj_UPDRSII = QLabel('UPDRS II:\t')
        self.lineEditUPDRSII = QLineEdit()
        lay35 = QHBoxLayout()
        lay35.addWidget(self.subj_UPDRSII)
        lay35.addWidget(self.lineEditUPDRSII)
        lay35.addStretch()

        self.subj_UPDRSIIIOn = QLabel('UPDRS III On:\t')
        self.lineEditUPDRSIIIOn = QLineEdit()
        lay36 = QHBoxLayout()
        lay36.addWidget(self.subj_UPDRSIIIOn)
        lay36.addWidget(self.lineEditUPDRSIIIOn)
        lay36.addStretch()

        self.subj_UPDRSIIIOff = QLabel('UPDRS III Off:\t\t')
        self.lineEditUPDRSIIIOff = QLineEdit()
        lay37 = QHBoxLayout()
        lay37.addWidget(self.subj_UPDRSIIIOff)
        lay37.addWidget(self.lineEditUPDRSIIIOff)
        lay37.addStretch()

        self.settings_list.addLayout(lay20)
        self.settings_list.addLayout(lay21)
        self.settings_list.addLayout(lay22)
        self.settings_list.addLayout(lay23)
        self.settings_list.addLayout(lay24)
        self.settings_list.addLayout(lay25)
        self.settings_list.addLayout(lay26)
        self.settings_list.addLayout(lay27)
        self.settings_list.addLayout(lay28)
        self.settings_list.addLayout(lay29)
        self.settings_list.addLayout(lay30)
        self.settings_list.addLayout(lay31)
        self.settings_list.addLayout(lay32)
        self.settings_list.addLayout(lay33)
        self.settings_list.addLayout(lay34)
        self.settings_list.addLayout(lay35)
        self.settings_list.addLayout(lay36)
        self.settings_list.addLayout(lay37)


        self.optionbox7 = QGroupBox('Notes')
        self.settings_list = QVBoxLayout(self.optionbox7)

        # ====================    Create Content for Seventh Option box on Top Right     ====================
        self.subj_Notes = QLabel('Notes:\t')
        self.lineEditNotes = QLineEdit()
        lay38 = QHBoxLayout()
        lay38.addWidget(self.subj_Notes)
        lay38.addWidget(self.lineEditNotes)
        lay38.addStretch()

        self.settings_list.addLayout(lay38)

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_bottom = QHBoxLayout()
        self.button_save_return = QPushButton('Save settings \nand return')
        self.button_save_return.clicked.connect(self.onClickedSaveReturn)

        layout_bottom.addStretch(1)
        layout_bottom.addWidget(self.button_save_return)

        self.layout.addWidget(self.optionbox1)
        self.layout.addWidget(self.optionbox2)
        self.layout.addWidget(self.optionbox3)
        self.layout.addWidget(self.optionbox4)
        self.layout.addWidget(self.optionbox5)
        self.layout.addWidget(self.optionbox6)
        self.layout.addWidget(self.optionbox7)
        self.layout.addLayout(layout_bottom)


        # In the next lines, actions are defined when Buttons are pressed

    @QtCore.pyqtSlot()
    def onClickedSaveReturn(self):
        self.saveFileDialog()

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
    dlg = PreoperativeDialog()
    dlg.show()
    sys.exit(app.exec_())
