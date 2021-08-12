# Hallo David
# Ich habe mit dieser Test Datei versucht GUI_Preoperative so zu schreiben, dass man Textfelder hat zum Eintragen der
# Daten. Ich habe keinen einfacheren Weg gefunden die Daten mit "grid Layout" anzuordnen. Gibt es da irgendeinen Trick,
# sodass man QGroupBox und QLineEdit miteinander verknüpfen kann?
# Der Trick ist dass Du \t (Tab) nutzt, da Du hierdurch immer den gleichen Abstand hast und dann das manuell machst.
# Das ist die pragmatische Lösung, denn der Rest ist sehr aufwändig. Ich habe es mal hier angepasst.

import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QFileDialog, QWidget, QRadioButton, QGridLayout, QLineEdit, QLabel, QComboBox


textfield_width = 450


class MedicationDialog(QDialog):
    """Dialog to introduce the medication at a specific date. All unrelated """

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)

        self.setWindowTitle('Preoperative Information')
        self.setGeometry(200, 100, 280, 170)
        self.move(850, 200)

        self.layout = QVBoxLayout(self)
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


        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_bottom = QHBoxLayout()
        self.button_save_return = QPushButton('Save settings \nand return')
        self.button_save_return.clicked.connect(self.onClickedSaveReturn)

        layout_bottom.addStretch(1)
        layout_bottom.addWidget(self.button_save_return)

        self.layout.addWidget(self.optionbox1)
        self.layout.addWidget(self.optionbox2)
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
    dlg = MedicationDialog()
    dlg.show()
    sys.exit(app.exec_())
