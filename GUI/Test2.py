# Hallo David. Ich habe mal versucht jedem self.settings_list = QVBoxLayout(self.optionbox1) nur ein Objekt zuzuweisen.
# Ich bin mir nicht sicher, ob ich den Auftrag komplett verstanden habe, aber so wie es jetzt ist, gefällt es mir optisch nicht so gut.
# Ich fand es eigentlich sehr schön, als die verschiedenen Information gruppiert waren in einzelnen Boxen.
# Kann man das vielleicht irgendwie kombinieren?

##==> Du erstellst zuviele Gruppen und deswegen wirkt es sehr unsortiert. Ich habe mal versucht das Ganze zu
# vereinfachen. Die Idee ist folgende: Erstelle erst einmal ein Gerüst mit den Boxen die Du brauchst (das kann man
# später noch sortieren) und füge jeweils nur einen Wert ein. Ich habe das mal optionbox(x) genannt und den Inhalt
# jeweils optionbox(x)Content. Das hat jeweils die Möglichkeit INhalte horizontal (QHBoxLayout) oder vertikal
# auszurichten (QHBoxLayout). Die Ausrichtung im Gui geschieht mittels GridLayout, was sehr variabel ist. Dann fügst Du
# die Box hinzu (layout.addWidget) und später den INhalt (nochmals als horizontale Gruppe, siehe zum Beispiel lay1).
# Die Bezeichnungen sind etwas gewöhnungsbedürftig, gebe ich zu, aber so kannst Du relativ flexibel Dinge eintragen
# und auch später ergänzen. Magst Du mal schauen, wie das so klappt?


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

        layout = QGridLayout(self)
        self.setLayout(layout)

        # Create one optionbox for the time being left
        self.optionbox1 = QGroupBox('General data')
        self.optionbox1Content = QVBoxLayout(self.optionbox1)
        layout.addWidget(self.optionbox1, 0, 0)

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

        self.optionbox1Content.addLayout(lay1)
        self.optionbox1Content.addLayout(lay2)
        self.optionbox1.setLayout(self.optionbox1Content)

        # Create one optionbox for the time being right
        self.optionbox2 = QGroupBox('DBS data')
        self.optionbox2Content = QVBoxLayout(self.optionbox2)
        layout.addWidget(self.optionbox2, 0, 1)

        self.subj_PID = QLabel('PID:\t\t')
        self.lineEditPID = QLineEdit()
        lay3 = QHBoxLayout()
        lay3.addWidget(self.subj_PID)
        lay3.addWidget(self.lineEditPID)
        lay3.addStretch()

        self.subj_ID = QLabel('ID:\t\t')
        self.lineEditID = QLineEdit()
        lay4 = QHBoxLayout()
        lay4.addWidget(self.subj_ID)
        lay4.addWidget(self.lineEditID)
        lay4.addStretch()

        self.optionbox2Content.addLayout(lay3)
        self.optionbox2Content.addLayout(lay4)
        self.optionbox2.setLayout(self.optionbox2Content)



        # # ====================    Create Content for First Option box on Top left      ====================
        # self.subj_PID = QLabel('PID:\t\t')
        # self.lineEditPID = QLineEdit()
        # lay1 = QHBoxLayout()
        # lay1.addWidget(self.subj_PID)
        # lay1.addWidget(self.lineEditPID)
        # lay1.addStretch()
        #
        # self.optionbox2 = QGroupBox('ID')
        # self.settings_list = QVBoxLayout(self.optionbox2)
        #
        # self.subj_ID = QLabel('ID:\t\t')
        # self.lineEditID = QLineEdit()
        # lay2 = QHBoxLayout()
        # lay2.addWidget(self.subj_ID)
        # lay2.addWidget(self.lineEditID)
        # lay2.addStretch()
        #
        # self.optionbox3 = QGroupBox('Gender')
        # self.settings_list = QVBoxLayout(self.optionbox3)
        #
        # self.subj_gender = QLabel('Gender:\t\t')
        # self.lineEditGender = QComboBox()
        # self.lineEditGender.addItems(['female', 'male', 'diverse'])
        # self.lineEditGender.setFixedHeight(50)
        # lay3 = QHBoxLayout()
        # lay3.addWidget(self.subj_gender)
        # lay3.addWidget(self.lineEditGender)
        # lay3.addStretch()
        #
        # self.optionbox4 = QGroupBox('Diagnosis')
        # self.settings_list = QVBoxLayout(self.optionbox4)
        #
        # self.subj_diagnosis = QLabel('Diagnosis:\t')
        # self.lineEditDiagnosis = QComboBox()
        # self.lineEditDiagnosis.addItems(['Hypokinetic-rigid parkinson-syndrome (PD1)',
        #                                  'Tremordominant parkinson-syndrome(PD2)',
        #                                  'Mixed-type parkinson-syndrome (PD3)',
        #                                  'Dystonia (DT)',
        #                                  'Essential tremor (ET)',
        #                                  'Other'])
        #
        # self.lineEditDiagnosis.setFixedWidth(textfield_width)
        # self.lineEditDiagnosis.setFixedHeight(50)
        # lay4 = QHBoxLayout()
        # lay4.addWidget(self.subj_diagnosis)
        # lay4.addWidget(self.lineEditDiagnosis)
        # lay4.addStretch()
        #
        # self.optionbox5 = QGroupBox('First Diagnosed')
        # self.settings_list = QVBoxLayout(self.optionbox5)
        #
        # self.subj_firstDiagnosed = QLabel('First Diagnosed:\t')
        # self.lineEditfirstDiagnosed = QLineEdit()
        # lay5 = QHBoxLayout()
        # lay5.addWidget(self.subj_firstDiagnosed)
        # lay5.addWidget(self.lineEditfirstDiagnosed)
        # lay5.addStretch()
        #
        # self.optionbox6 = QGroupBox('Admission')
        # self.settings_list = QVBoxLayout(self.optionbox6)
        #
        # self.subj_Admission = QLabel('Admission:\t')
        # self.lineEditAdmission = QLineEdit()
        # lay6 = QHBoxLayout()
        # lay6.addWidget(self.subj_Admission)
        # lay6.addWidget(self.lineEditAdmission)
        # lay6.addStretch()
        #
        # self.optionbox7 = QGroupBox('Dismissal')
        # self.settings_list = QVBoxLayout(self.optionbox7)
        #
        # self.subj_Dismissal = QLabel('Dismissal:\t')
        # self.lineEditDismissal = QLineEdit()
        # lay7 = QHBoxLayout()
        # lay7.addWidget(self.subj_Dismissal)
        # lay7.addWidget(self.lineEditDismissal)
        # lay7.addStretch()
        #
        # self.optionbox8 = QGroupBox('Report')
        # self.settings_list = QVBoxLayout(self.optionbox8)
        #
        # self.subj_Report = QLabel('Report:\t\t')
        # self.lineEditReport = QLineEdit()
        # lay8 = QHBoxLayout()
        # lay8.addWidget(self.subj_Report)
        # lay8.addWidget(self.lineEditReport)
        # lay8.addStretch()
        #
        # self.optionbox9 = QGroupBox('Report Preop')
        # self.settings_list = QVBoxLayout(self.optionbox9)
        #
        # self.subj_ReportPreop = QLabel('Report Preop:\t')
        # self.lineEditReportPreop = QLineEdit()
        # lay9 = QHBoxLayout()
        # lay9.addWidget(self.subj_ReportPreop)
        # lay9.addWidget(self.lineEditReportPreop)
        # lay9.addStretch()
        #
        # self.settings_list.addLayout(lay1)
        # self.settings_list.addLayout(lay2)
        # self.settings_list.addLayout(lay3)
        # self.settings_list.addLayout(lay4)
        # self.settings_list.addLayout(lay5)
        # self.settings_list.addLayout(lay6)
        # self.settings_list.addLayout(lay7)
        # self.settings_list.addLayout(lay8)
        # self.settings_list.addLayout(lay9)
        #
        # # ====================    Create Content for Buttons at the Bottom      ====================
        #
        # layout_bottom = QHBoxLayout()
        # self.button_save_return = QPushButton('Save settings \nand return')
        # self.button_save_return.clicked.connect(self.onClickedSaveReturn)
        #
        # layout_bottom.addStretch(1)
        # layout_bottom.addWidget(self.button_save_return)
        #
        # self.layout.addWidget(self.optionbox1)
        # self.layout.addWidget(self.optionbox2)
        # self.layout.addWidget(self.optionbox3)
        # self.layout.addWidget(self.optionbox4)
        # self.layout.addWidget(self.optionbox5)
        # self.layout.addWidget(self.optionbox6)
        # self.layout.addWidget(self.optionbox7)
        # self.layout.addWidget(self.optionbox8)
        # self.layout.addWidget(self.optionbox9)
        # self.layout.addLayout(layout_bottom)
        #
        # grid = QGridLayout(self)
        # grid.addWidget(self.optionbox1, 0, 0)
        # grid.addWidget(self.optionbox2, 0, 1)
        # grid.addWidget(self.optionbox3, 0, 2)
        # grid.addWidget(self.optionbox4, 1, 0)
        # grid.addWidget(self.optionbox5, 1, 1)
        # grid.addWidget(self.optionbox6, 1, 2)
        # grid.addWidget(self.optionbox7, 2, 0)
        # grid.addWidget(self.optionbox8, 2, 1)
        # grid.addWidget(self.optionbox9, 2, 1)
        # self.setLayout(grid)


    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
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
    dlg = PreoperativeDialog()
    dlg.show()
    sys.exit(app.exec_())
