# Hi David. Ich hab tatsächlich das Problem, dass nicht alle Punkte auf den Bildschirm passen.

import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel, QFileDialog, QWidget


class Dialog(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Subject Information')
        self.setGeometry(200, 100, 280, 170)
        self.move(850, 200)

        self.layout = QVBoxLayout(self)
        self.optionbox1 = QGroupBox('Preoperative')
        self.settings_list = QVBoxLayout(self.optionbox1)

        # ====================    Create Content for First Option box on Top left      ====================
        self.subj_ID = QLabel('ID:\t\t')
        self.lineEditFilename = QLineEdit()
        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_ID)
        lay1.addWidget(self.lineEditFilename)
        lay1.addStretch()

        self.subj_Gender = QLabel('Gender:\t\t')
        self.lineEditFilename = QLineEdit()
        lay2 = QHBoxLayout()
        lay2.addWidget(self.subj_Gender)
        lay2.addWidget(self.lineEditFilename)
        lay2.addStretch()

        self.subj_Diagnosis = QLabel('Diagnosis:\t\t')
        self.lineEditFilename = QLineEdit()
        lay3 = QHBoxLayout()
        lay3.addWidget(self.subj_Diagnosis)
        lay3.addWidget(self.lineEditFilename)
        lay3.addStretch()

        self.subj_First_Diagnosed = QLabel('First_Diagnosed:\t\t')
        self.lineEditFilename = QLineEdit()
        lay4 = QHBoxLayout()
        lay4.addWidget(self.subj_First_Diagnosed)
        lay4.addWidget(self.lineEditFilename)
        lay4.addStretch()

        self.subj_Admission = QLabel('Admission:\t\t')
        self.lineEditFilename = QLineEdit()
        lay5 = QHBoxLayout()
        lay5.addWidget(self.subj_Admission)
        lay5.addWidget(self.lineEditFilename)
        lay5.addStretch()

        self.subj_Dismissal = QLabel('Dismissal:\t\t')
        self.lineEditFilename = QLineEdit()
        lay6 = QHBoxLayout()
        lay6.addWidget(self.subj_Dismissal)
        lay6.addWidget(self.lineEditFilename)
        lay6.addStretch()

        self.subj_Report = QLabel('Report:\t\t')
        self.lineEditFilename = QLineEdit()
        lay7 = QHBoxLayout()
        lay7.addWidget(self.subj_Report)
        lay7.addWidget(self.lineEditFilename)
        lay7.addStretch()

        self.subj_Report_Preop = QLabel('Report_Preop:\t\t')
        self.lineEditFilename = QLineEdit()
        lay8 = QHBoxLayout()
        lay8.addWidget(self.subj_Report_Preop)
        lay8.addWidget(self.lineEditFilename)
        lay8.addStretch()

        self.subj_UPDRS_On = QLabel('UPDRS_On:\t\t')
        self.lineEditFilename = QLineEdit()
        lay9 = QHBoxLayout()
        lay9.addWidget(self.subj_UPDRS_On)
        lay9.addWidget(self.lineEditFilename)
        lay9.addStretch()

        self.subj_UPDRS_Off = QLabel('UPDRS_Off:\t\t')
        self.lineEditFilename = QLineEdit()
        lay10 = QHBoxLayout()
        lay10.addWidget(self.subj_UPDRS_Off)
        lay10.addWidget(self.lineEditFilename)
        lay10.addStretch()

        self.subj_Video = QLabel('Video:\t\t')
        self.lineEditFilename = QLineEdit()
        lay11 = QHBoxLayout()
        lay11.addWidget(self.subj_Video)
        lay11.addWidget(self.lineEditFilename)
        lay11.addStretch()

        self.subj_Video_File = QLabel('Video_File:\t\t')
        self.lineEditFilename = QLineEdit()
        lay12 = QHBoxLayout()
        lay12.addWidget(self.subj_Video_File)
        lay12.addWidget(self.lineEditFilename)
        lay12.addStretch()

        self.subj_MRI = QLabel('MRI:\t\t')
        self.lineEditFilename = QLineEdit()
        lay13 = QHBoxLayout()
        lay13.addWidget(self.subj_MRI)
        lay13.addWidget(self.lineEditFilename)
        lay13.addStretch()

        self.subj_fpcit_spect = QLabel('fpcit_spect:\t\t')
        self.lineEditFilename = QLineEdit()
        lay14 = QHBoxLayout()
        lay14.addWidget(self.subj_fpcit_spect)
        lay14.addWidget(self.lineEditFilename)
        lay14.addStretch()

        self.subj_NMSQ = QLabel('NMSQ:\t\t')
        self.lineEditFilename = QLineEdit()
        lay15 = QHBoxLayout()
        lay15.addWidget(self.subj_NMSQ)
        lay15.addWidget(self.lineEditFilename)
        lay15.addStretch()

        self.subj_MoCa = QLabel('MoCa:\t\t')
        self.lineEditFilename = QLineEdit()
        lay16 = QHBoxLayout()
        lay16.addWidget(self.subj_MoCa)
        lay16.addWidget(self.lineEditFilename)
        lay16.addStretch()

        self.subj_DemTect = QLabel('DemTect:\t\t')
        self.lineEditFilename = QLineEdit()
        lay17 = QHBoxLayout()
        lay17.addWidget(self.subj_DemTect)
        lay17.addWidget(self.lineEditFilename)
        lay17.addStretch()

        self.subj_MMST = QLabel('MMST:\t\t')
        self.lineEditFilename = QLineEdit()
        lay18 = QHBoxLayout()
        lay18.addWidget(self.subj_MMST)
        lay18.addWidget(self.lineEditFilename)
        lay18.addStretch()

        self.subj_PDQ8 = QLabel('PDQ8:\t\t')
        self.lineEditFilename = QLineEdit()
        lay19 = QHBoxLayout()
        lay19.addWidget(self.subj_PDQ8)
        lay19.addWidget(self.lineEditFilename)
        lay19.addStretch()

        self.subj_BDI2 = QLabel('BDI2:\t\t')
        self.lineEditFilename = QLineEdit()
        lay20 = QHBoxLayout()
        lay20.addWidget(self.subj_BDI2)
        lay20.addWidget(self.lineEditFilename)
        lay20.addStretch()

        self.subj_PDQ39 = QLabel('PDQ39:\t\t')
        self.lineEditFilename = QLineEdit()
        lay21 = QHBoxLayout()
        lay21.addWidget(self.subj_PDQ39)
        lay21.addWidget(self.lineEditFilename)
        lay21.addStretch()

        self.subj_Outpat_Contact = QLabel('Outpat_Contact:\t\t')
        self.lineEditFilename = QLineEdit()
        lay22 = QHBoxLayout()
        lay22.addWidget(self.subj_Outpat_Contact)
        lay22.addWidget(self.lineEditFilename)
        lay22.addStretch()

        self.subj_nch = QLabel('nch:\t\t')
        self.lineEditFilename = QLineEdit()
        lay23 = QHBoxLayout()
        lay23.addWidget(self.subj_nch)
        lay23.addWidget(self.lineEditFilename)
        lay23.addStretch()

        self.subj_Briefing = QLabel('Briefing:\t\t')
        self.lineEditFilename = QLineEdit()
        lay24 = QHBoxLayout()
        lay24.addWidget(self.subj_Briefing)
        lay24.addWidget(self.lineEditFilename)
        lay24.addStretch()

        self.subj_Briefing_Doctor = QLabel('Briefing_Doctor:\t\t')
        self.lineEditFilename = QLineEdit()
        lay25 = QHBoxLayout()
        lay25.addWidget(self.subj_Briefing_Doctor)
        lay25.addWidget(self.lineEditFilename)
        lay25.addStretch()

        self.subj_DBS_Conference = QLabel('DBS_Conference:\t\t')
        self.lineEditFilename = QLineEdit()
        lay26 = QHBoxLayout()
        lay26.addWidget(self.subj_DBS_Conference)
        lay26.addWidget(self.lineEditFilename)
        lay26.addStretch()

        self.subj_Decision_DBS = QLabel('Decision_DBS:\t\t')
        self.lineEditFilename = QLineEdit()
        lay27 = QHBoxLayout()
        lay27.addWidget(self.subj_Decision_DBS)
        lay27.addWidget(self.lineEditFilename)
        lay27.addStretch()

        self.subj_LEDD = QLabel('LEDD:\t\t')
        self.lineEditFilename = QLineEdit()
        lay28 = QHBoxLayout()
        lay28.addWidget(self.subj_LEDD)
        lay28.addWidget(self.lineEditFilename)
        lay28.addStretch()

        self.subj_Levodopa_Carbidopa = QLabel('Levodopa/Carbidopa:\t\t')
        self.lineEditFilename = QLineEdit()
        lay29 = QHBoxLayout()
        lay29.addWidget(self.subj_Levodopa_Carbidopa)
        lay29.addWidget(self.lineEditFilename)
        lay29.addStretch()

        self.subj_Levodopa_Carbidopa_CR = QLabel('Levodopa/Carbidopa CR:\t\t')
        self.lineEditFilename = QLineEdit()
        lay30 = QHBoxLayout()
        lay30.addWidget(self.subj_Levodopa_Carbidopa_CR)
        lay30.addWidget(self.lineEditFilename)
        lay30.addStretch()

        self.subj_Entacapone = QLabel('Entacapone:\t\t')
        self.lineEditFilename = QLineEdit()
        lay31 = QHBoxLayout()
        lay31.addWidget(self.subj_Entacapone)
        lay31.addWidget(self.lineEditFilename)
        lay31.addStretch()

        self.subj_Tolcapone = QLabel('Tolcapone:\t\t')
        self.lineEditFilename = QLineEdit()
        lay32 = QHBoxLayout()
        lay32.addWidget(self.subj_Tolcapone)
        lay32.addWidget(self.lineEditFilename)
        lay32.addStretch()

        self.subj_Pramipexole = QLabel('Pramipexole:\t\t')
        self.lineEditFilename = QLineEdit()
        lay33 = QHBoxLayout()
        lay33.addWidget(self.subj_Pramipexole)
        lay33.addWidget(self.lineEditFilename)
        lay33.addStretch()

        self.subj_Ropinirole = QLabel('Ropinirole:\t\t')
        self.lineEditFilename = QLineEdit()
        lay34 = QHBoxLayout()
        lay34.addWidget(self.subj_Ropinirole)
        lay34.addWidget(self.lineEditFilename)
        lay34.addStretch()

        self.subj_Rotigotine = QLabel('Rotigotine:\t\t')
        self.lineEditFilename = QLineEdit()
        lay35 = QHBoxLayout()
        lay35.addWidget(self.subj_Rotigotine)
        lay35.addWidget(self.lineEditFilename)
        lay35.addStretch()

        self.subj_Selegiline_oral = QLabel('Selegiline oral:\t\t')
        self.lineEditFilename = QLineEdit()
        lay36 = QHBoxLayout()
        lay36.addWidget(self.subj_Selegiline_oral)
        lay36.addWidget(self.lineEditFilename)
        lay36.addStretch()

        self.subj_Selegiline_sublingual = QLabel('Selegiline sublingual:\t\t')
        self.lineEditFilename = QLineEdit()
        lay37 = QHBoxLayout()
        lay37.addWidget(self.subj_Selegiline_sublingual)
        lay37.addWidget(self.lineEditFilename)
        lay37.addStretch()

        self.subj_Rasagiline = QLabel('Rasagiline:\t\t')
        self.lineEditFilename = QLineEdit()
        lay38 = QHBoxLayout()
        lay38.addWidget(self.subj_Rasagiline)
        lay38.addWidget(self.lineEditFilename)
        lay38.addStretch()

        self.subj_Amantadine = QLabel('Amantadine:\t\t')
        self.lineEditFilename = QLineEdit()
        lay39 = QHBoxLayout()
        lay39.addWidget(self.subj_Amantadine)
        lay39.addWidget(self.lineEditFilename)
        lay39.addStretch()

        self.subj_Apomorphine = QLabel('Apomorphine:\t\t')
        self.lineEditFilename = QLineEdit()
        lay40 = QHBoxLayout()
        lay40.addWidget(self.subj_Apomorphine)
        lay40.addWidget(self.lineEditFilename)
        lay40.addStretch()

        self.subj_Piribedil = QLabel('Piribedil:\t\t')
        self.lineEditFilename = QLineEdit()
        lay41 = QHBoxLayout()
        lay41.addWidget(self.subj_Piribedil)
        lay41.addWidget(self.lineEditFilename)
        lay41.addStretch()

        self.subj_Safinamid = QLabel('Safinamid:\t\t')
        self.lineEditFilename = QLineEdit()
        lay42 = QHBoxLayout()
        lay42.addWidget(self.subj_Safinamid)
        lay42.addWidget(self.lineEditFilename)
        lay42.addStretch()

        self.subj_Opicapone = QLabel('Opicapone:\t\t')
        self.lineEditFilename = QLineEdit()
        lay43 = QHBoxLayout()
        lay43.addWidget(self.subj_Opicapone)
        lay43.addWidget(self.lineEditFilename)
        lay43.addStretch()

        self.subj_Ongentys = QLabel('Ongentys:\t\t')
        self.lineEditFilename = QLineEdit()
        lay44 = QHBoxLayout()
        lay44.addWidget(self.subj_Ongentys)
        lay44.addWidget(self.lineEditFilename)
        lay44.addStretch()

        self.subj_Other = QLabel('Other:\t\t')
        self.lineEditFilename = QLineEdit()
        lay45 = QHBoxLayout()
        lay45.addWidget(self.subj_Other)
        lay45.addWidget(self.lineEditFilename)
        lay45.addStretch()

        self.subj_UPDRSII = QLabel('UPDRSII:\t\t')
        self.lineEditFilename = QLineEdit()
        lay46 = QHBoxLayout()
        lay46.addWidget(self.subj_UPDRSII)
        lay46.addWidget(self.lineEditFilename)
        lay46.addStretch()

        self.subj_H_Y = QLabel('H&Y:\t\t')
        self.lineEditFilename = QLineEdit()
        lay47 = QHBoxLayout()
        lay47.addWidget(self.subj_H_Y)
        lay47.addWidget(self.lineEditFilename)
        lay47.addStretch()

        self.subj_HRUQ = QLabel('HRUQ:\t\t')
        self.lineEditFilename = QLineEdit()
        lay48 = QHBoxLayout()
        lay48.addWidget(self.subj_HRUQ)
        lay48.addWidget(self.lineEditFilename)
        lay48.addStretch()

        self.subj_EQ5D = QLabel('EQ5D:\t\t')
        self.lineEditFilename = QLineEdit()
        lay49 = QHBoxLayout()
        lay49.addWidget(self.subj_EQ5D)
        lay49.addWidget(self.lineEditFilename)
        lay49.addStretch()

        self.subj_S_E = QLabel('S&E:\t\t')  #Ist Lay15 und 16 das gleiche?
        self.lineEditFilename = QLineEdit()
        lay50 = QHBoxLayout()
        lay50.addWidget(self.subj_S_E)
        lay50.addWidget(self.lineEditFilename)
        lay50.addStretch()

        self.subj_icVRCS = QLabel('icVRCS:\t\t')
        self.lineEditFilename = QLineEdit()
        lay51 = QHBoxLayout()
        lay51.addWidget(self.subj_icVRCS)
        lay51.addWidget(self.lineEditFilename)
        lay51.addStretch()

        self.subj_inexVRCS = QLabel('inexVRCS:\t\t')
        self.lineEditFilename = QLineEdit()
        lay52 = QHBoxLayout()
        lay52.addWidget(self.subj_inexVRCS)
        lay52.addWidget(self.lineEditFilename)
        lay52.addStretch()

        self.subj_Notes = QLabel('Notes:\t\t')
        self.lineEditFilename = QLineEdit()
        lay53 = QHBoxLayout()
        lay53.addWidget(self.subj_Notes)
        lay53.addWidget(self.lineEditFilename)
        lay53.addStretch()

        self.settings_list.addLayout(lay1)
        self.settings_list.addLayout(lay2)
        self.settings_list.addLayout(lay3)
        self.settings_list.addLayout(lay4)
        self.settings_list.addLayout(lay5)
        self.settings_list.addLayout(lay6)
        self.settings_list.addLayout(lay7)
        self.settings_list.addLayout(lay8)
        self.settings_list.addLayout(lay9)
        self.settings_list.addLayout(lay10)
        self.settings_list.addLayout(lay11)
        self.settings_list.addLayout(lay12)
        self.settings_list.addLayout(lay13)
        self.settings_list.addLayout(lay14)
        self.settings_list.addLayout(lay15)
        self.settings_list.addLayout(lay16)
        self.settings_list.addLayout(lay17)
        self.settings_list.addLayout(lay18)
        self.settings_list.addLayout(lay19)
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
        self.settings_list.addLayout(lay38)
        self.settings_list.addLayout(lay39)
        self.settings_list.addLayout(lay40)
        self.settings_list.addLayout(lay41)
        self.settings_list.addLayout(lay42)
        self.settings_list.addLayout(lay43)
        self.settings_list.addLayout(lay44)
        self.settings_list.addLayout(lay45)
        self.settings_list.addLayout(lay46)
        self.settings_list.addLayout(lay47)
        self.settings_list.addLayout(lay48)
        self.settings_list.addLayout(lay49)
        self.settings_list.addLayout(lay50)
        self.settings_list.addLayout(lay51)
        self.settings_list.addLayout(lay52)
        self.settings_list.addLayout(lay53)

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_bottom = QHBoxLayout()
        self.button_savereturn = QPushButton('Save settings \nand return')
        self.button_savereturn.clicked.connect(self.onClickedSaveReturn)
        self.button_close = QPushButton('Save and \nclose')
        self.button_close.clicked.connect(self.close)  # TODO: define function to save things before closing

        layout_bottom.addStretch(1)
        layout_bottom.addWidget(self.button_savereturn)
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
        # first parameter is self; second is the Window Title, third title is Default File Name, fourth is FileType, fifth is options
        file = QFileDialog.getOpenFileName(self, "Save File Window Title", "default.txt", "All Files (*)", options=option)
        print(file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
