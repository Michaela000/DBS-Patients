# OK, ich habe einen Vorschlag. Wir nutzen dafür mal das Wiki und erstellen eine Rubrik Abkürzungen und dort werde ich
# dann die unterschiedlichen Skalen definieren, einverstanden? Manche Dinge sind eher im Kontext zu sehen und daher nicht
# ganz einfach zu erklären/verstehen (Report heißt, ob ein Arztbrief vorliegt oder nicht). Neben den Todos aus GUIstart.py
# würde ich vorschlagen, dass Du versuchst die Tabellen fertig zu machen und am besten mit den Feldern von der Excel Datei,
# also wenn ein Feld steht ein Feld, wenn ein RadioButton vorhanden ist das, usw.

# Hallo David. Vielen Dank für Deine Hilfe heute morgen. So klappt es wesentlich besser und leichter.
# Die Idee mit dem Wiki-Eintrag finde ich klasse.
# Ich lade zusätzlich noch den csv File von Preoperative und danach auch von Postoperative hoch, aber da wird sich noch einiges an den
# Gruppen ändern, sobald ich weiß, was manche Abkürzungen eigentlich bedeuten. Aber es müssten alle Punkte sein.
# Das Einzige was ich immer gelöscht habe, war eine Spalte mit dem Namen "curr_no", weil nie etwas in dieser Spalte stand. Ist die wichtig?


import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QFileDialog, QWidget, QRadioButton, QGridLayout


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
        grid.addWidget(self.createGroup8(), 2, 1)
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
        groupBox3 = QGroupBox("Scales/Scans")
        info10 = QRadioButton("Video")
        info11 = QRadioButton("Video File")
        info12 = QRadioButton("MRI")
        info13 = QRadioButton("fpcit_spect")
        info14 = QRadioButton("NMSQ")
        info15 = QRadioButton("MoCa")
        info16 = QRadioButton("DemTect")
        info17 = QRadioButton("MMST")
        info18 = QRadioButton("PDQ8")
        info19 = QRadioButton("BDI2")
        info20 = QRadioButton("PDQ39")
        info10.setChecked(True)
        info11.setChecked(True)
        info12.setChecked(True)
        info13.setChecked(True)
        info14.setChecked(True)
        info15.setChecked(True)
        info16.setChecked(True)
        info17.setChecked(True)
        info18.setChecked(True)
        info19.setChecked(True)
        info20.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info10)
        vbox.addWidget(info11)
        vbox.addWidget(info12)
        vbox.addWidget(info13)
        vbox.addWidget(info14)
        vbox.addWidget(info15)
        vbox.addWidget(info16)
        vbox.addWidget(info17)
        vbox.addWidget(info18)
        vbox.addWidget(info19)
        vbox.addWidget(info20)
        vbox.addStretch(1)
        groupBox3.setLayout(vbox)
        return groupBox3

    def createGroup4(self):
        groupBox4 = QGroupBox("DBS")
        info21 = QRadioButton("Outpat Contact")
        info22 = QRadioButton("nch")
        info23 = QRadioButton("Briefing")
        info24 = QRadioButton("Briefing Doctor")
        info25 = QRadioButton("DBS Conference")
        info26 = QRadioButton("Decision DBS")
        info21.setChecked(True)
        info22.setChecked(True)
        info23.setChecked(True)
        info24.setChecked(True)
        info25.setChecked(True)
        info26.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info21)
        vbox.addWidget(info22)
        vbox.addWidget(info23)
        vbox.addWidget(info24)
        vbox.addWidget(info25)
        vbox.addWidget(info26)
        vbox.addStretch(1)
        groupBox4.setLayout(vbox)
        return groupBox4

    def createGroup5(self):
        groupBox5 = QGroupBox("LEDD")
        info27 = QRadioButton("LEDD")
        info27.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info27)
        vbox.addStretch(1)
        groupBox5.setLayout(vbox)
        return groupBox5

    def createGroup6(self):
        groupBox6 = QGroupBox("Medication")
        info28 = QRadioButton("Levodopa/Carbidopa")
        info29 = QRadioButton("Levodopa/Carbidopa CR")
        info30 = QRadioButton("Entacapone")
        info31 = QRadioButton("Tolcapone")
        info32 = QRadioButton("Pramipexole")
        info33 = QRadioButton("Ropinirole")
        info34 = QRadioButton("Rotigotine")
        info35 = QRadioButton("Selegiline, oral")
        info36 = QRadioButton("Selegiline, sublingual")
        info37 = QRadioButton("Rasagiline")
        info38 = QRadioButton("Amantadine")
        info39 = QRadioButton("Apomorphine")
        info40 = QRadioButton("Piribedil")
        info41 = QRadioButton("Safinamid")
        info42 = QRadioButton("Opicapone")
        info43 = QRadioButton("Other")
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
        info38.setChecked(True)
        info39.setChecked(True)
        info40.setChecked(True)
        info41.setChecked(True)
        info42.setChecked(True)
        info43.setChecked(True)
        vbox = QVBoxLayout()
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
        vbox.addWidget(info38)
        vbox.addWidget(info39)
        vbox.addWidget(info40)
        vbox.addWidget(info41)
        vbox.addWidget(info42)
        vbox.addWidget(info43)
        vbox.addStretch(1)
        groupBox6.setLayout(vbox)
        return groupBox6

    def createGroup7(self):
        groupBox7 = QGroupBox("Tests")
        info44 = QRadioButton("UPDRS On")
        info45 = QRadioButton("UPDRS Off")
        info46 = QRadioButton("UPDRS II")
        info47 = QRadioButton("H&Y")
        info48 = QRadioButton("HRUQ")
        info49 = QRadioButton("EQ5D")
        info50 = QRadioButton("S&E")
        info51 = QRadioButton("icVRCS")
        info52 = QRadioButton("inexVRCS")
        info44.setChecked(True)
        info45.setChecked(True)
        info46.setChecked(True)
        info47.setChecked(True)
        info48.setChecked(True)
        info49.setChecked(True)
        info50.setChecked(True)
        info51.setChecked(True)
        info52.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info44)
        vbox.addWidget(info45)
        vbox.addWidget(info46)
        vbox.addWidget(info47)
        vbox.addWidget(info48)
        vbox.addWidget(info49)
        vbox.addWidget(info50)
        vbox.addWidget(info51)
        vbox.addWidget(info52)
        vbox.addStretch(1)
        groupBox7.setLayout(vbox)
        return groupBox7

    def createGroup8(self):
        groupBox8 = QGroupBox("Notes")
        info53 = QRadioButton("Notes")
        info53.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info53)
        vbox.addStretch(1)
        groupBox8.setLayout(vbox)
        return groupBox8

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_bottom = QHBoxLayout()
        self.button_save_return = QPushButton('Save settings \nand return')
        self.button_save_return.clicked.connect(self.onClickedSaveReturn)
        self.button_close = QPushButton('Save and \nclose')
        self.button_close.clicked.connect(self.close)  

        layout_bottom.addStretch(1)
        layout_bottom.addWidget(self.button_save_return)
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
