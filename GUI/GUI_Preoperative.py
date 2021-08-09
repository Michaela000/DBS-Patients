# Hallo David
# Ich hatte große Probleme Textfelder mit QGroupBox zu kombinieren. Ich hab eigentlich den ganzen Nachmittag versucht
# QGroupBox mit QLineEdit zu verknüpfen und zusätzlich das grid Layout zu behalten, aber es hat irgendwie nicht geklappt.
# Hab mal provisorisch die Datei "Test.py" erstellt, in der ich das ganze mit dem bisher verwendeten "QHBoxLayout" verknüpft habe.
# Das sieht aber optisch wesentlich schlechter aus. Gibt es da irgendeinen Trick?


import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QFileDialog, QWidget, QRadioButton, QGridLayout, QLineEdit, QLabel


class PreoperativeDialog(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super(PreoperativeDialog, self).__init__(parent)

        grid = QGridLayout(self)
        grid.addWidget(self.createGroup1(), 0, 0)
        grid.addWidget(self.createGroup2(), 0, 1)
        grid.addWidget(self.createGroup3(), 0, 2)
        grid.addWidget(self.createGroup4(), 1, 0)
        grid.addWidget(self.createGroup5(), 1, 1)
        grid.addWidget(self.createGroup6(), 1, 2)
        grid.addWidget(self.createGroup7(), 2, 0)
        self.setLayout(grid)

        self.setWindowTitle('Patients Information')
        self.setGeometry(200, 100, 280, 170)
        self.move(850, 200)


    # Groups
    def createGroup1(self):
        groupBox1 = QGroupBox("Basic Information")
        info1 = QRadioButton("PID")
        info2 = QRadioButton("ID")
        info3 = QRadioButton("Gender")
        info4 = QRadioButton("Diagnosis")
        info5 = QRadioButton("First Diagnosed")
        info1.setChecked(True)
        info2.setChecked(True)
        info3.setChecked(True)
        info4.setChecked(True)
        info5.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info1)
        vbox.addWidget(info2)
        vbox.addWidget(info3)
        vbox.addWidget(info4)
        vbox.addWidget(info5)
        vbox.addStretch(1)
        groupBox1.setLayout(vbox)
        return groupBox1

    def createGroup2(self):
        groupBox2 = QGroupBox("Reports")
        info6 = QRadioButton("Admission")
        info7 = QRadioButton("Dismissal")
        info8 = QRadioButton("Report")
        info9 = QRadioButton("Report Preop")
        info6.setChecked(True)
        info7.setChecked(True)
        info8.setChecked(True)
        info9.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info6)
        vbox.addWidget(info7)
        vbox.addWidget(info7)
        vbox.addWidget(info8)
        vbox.addWidget(info9)
        vbox.addStretch(1)
        groupBox2.setLayout(vbox)
        return groupBox2

    def createGroup3(self):
        groupBox3 = QGroupBox("Files/Scans")
        info10 = QRadioButton("Video")
        info11 = QRadioButton("Video File")
        info12 = QRadioButton("MRI")
        info10.setChecked(True)
        info11.setChecked(True)
        info12.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info10)
        vbox.addWidget(info11)
        vbox.addWidget(info12)
        vbox.addStretch(1)
        groupBox3.setLayout(vbox)
        return groupBox3

    def createGroup4(self):
        groupBox4 = QGroupBox("DBS-Decision")
        info13 = QRadioButton("Outpat Contact")
        info14 = QRadioButton("nch")
        info15 = QRadioButton("Briefing")
        info16 = QRadioButton("Briefing Doctor")
        info17 = QRadioButton("DBS Conference")
        info18 = QRadioButton("Decision DBS")
        info13.setChecked(True)
        info14.setChecked(True)
        info15.setChecked(True)
        info16.setChecked(True)
        info17.setChecked(True)
        info18.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info13)
        vbox.addWidget(info14)
        vbox.addWidget(info15)
        vbox.addWidget(info16)
        vbox.addWidget(info17)
        vbox.addWidget(info18)
        vbox.addStretch(1)
        groupBox4.setLayout(vbox)
        return groupBox4

    def createGroup5(self):
        groupBox5 = QGroupBox("LEDD")
        info19 = QRadioButton("LEDD")
        info19.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info19)
        vbox.addStretch(1)
        groupBox5.setLayout(vbox)
        return groupBox5


    def createGroup6(self):
        groupBox6 = QGroupBox("Tests")
        info20 = QRadioButton("BDI2")
        info21 = QRadioButton("DemTect")
        info22 = QRadioButton("EQ5D")
        info23 = QRadioButton("fpcit_spect")
        info24 = QRadioButton("HRUQ")
        info25 = QRadioButton("H&Y")
        info26 = QRadioButton("icVRCS")
        info27 = QRadioButton("inexVRCS")
        info28 = QRadioButton("MMST")
        info29 = QRadioButton("MoCa")
        info30 = QRadioButton("MMST")
        info31 = QRadioButton("NMSQ")
        info32 = QRadioButton("PDQ8")
        info33 = QRadioButton("PDQ39")
        info34 = QRadioButton("S&E")
        info35 = QRadioButton("UPDRS On")
        info36 = QRadioButton("UPDRS Off")
        info37 = QRadioButton("UPDRS II")
        info20.setChecked(True)
        info21.setChecked(True)
        info22.setChecked(True)
        info23.setChecked(True)
        info24.setChecked(True)
        info25.setChecked(True)
        info26.setChecked(True)
        info27.setChecked(True)
        info28.setChecked(True)
        info29.setChecked(True)
        info30.setChecked(True)
        info31.setChecked(True)
        info32.setChecked(True)
        info33.setChecked(True)
        info34.setChecked(True)
        info35.setChecked(True)
        info36.setChecked(True)
        info37.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info20)
        vbox.addWidget(info21)
        vbox.addWidget(info22)
        vbox.addWidget(info23)
        vbox.addWidget(info24)
        vbox.addWidget(info25)
        vbox.addWidget(info26)
        vbox.addWidget(info27)
        vbox.addWidget(info28)
        vbox.addWidget(info29)
        vbox.addWidget(info30)
        vbox.addWidget(info31)
        vbox.addWidget(info32)
        vbox.addWidget(info33)
        vbox.addWidget(info34)
        vbox.addWidget(info35)
        vbox.addWidget(info36)
        vbox.addWidget(info37)
        vbox.addStretch(1)
        groupBox6.setLayout(vbox)
        return groupBox6

    def createGroup7(self):
        groupBox7 = QGroupBox("Notes")
        info38 = QRadioButton("Notes")
        info38.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info38)
        vbox.addStretch(1)
        groupBox7.setLayout(vbox)
        return groupBox7

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_bottom = QHBoxLayout()
        self.button_save_return = QPushButton('Save settings \nand return')
        self.button_save_return.clicked.connect(self.onClickedSaveReturn)
        self.button_close = QPushButton('Save and \nclose')
        self.button_close.clicked.connect(self.close_and_return)

        layout_bottom.addStretch(1)
        layout_bottom.addWidget(self.button_save_return)
        layout_bottom.addWidget(self.button_close)

        self.layout.addWidget(self.optionbox1)
        self.layout.addLayout(layout_bottom)

    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
    def onClickedSaveReturn(self):
        self.saveFileDialog()

    def close_and_return(self):
        self.close()
        self.parent().show()
        # self.hide()
        # self.saveFileDialog()

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
    dlg = PreoperativeDialog()
    dlg.show()
    sys.exit(app.exec_())
