# Hi David. Ich hab mal versucht Gruppen zu erstellen und das hat schlussendlich sogar funktioniert. Mein einziges Problem ist, dass ich bei manchen Abkürzungen nicht weiß was genau das 
# eigentlich ist (z.B. H&Y) und daher hab ich sie einfach zu irgendeiner Gruppe hinzugefügt. Gibt es vielleicht irgendwo eine Liste mit den Abkürzungen? Ich würde mir dann da auch durchlesen wollen, was genau
# mit "Report" oder so gemeint ist.
# Ich habe Dir per Email auch die beiden Tabellen geschickt, mir ist aber erst nach dem Abschicken aufgefallen, dass die "ID" in der Tabelle nicht die PID, sondern eine
# zufällig generierte Nummer ist. Soll ich nochmal eine neue Tabelle erstellen, in denen ich das genau zuordnen kann? Auf Grund der knappen Zeit, habe ich die Daten aus
# Deiner Tablle fürs Erste verwendet. 
# Ich fange heute an eine eigene Tabelle aufzusetzen.

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
        info2 = QRadioButton("Gender")
        info3 = QRadioButton("Diagnosis")
        info4 = QRadioButton("First Diagnosed")
        info5 = QRadioButton("Admission")
        info6 = QRadioButton("Dismissal")
        info1.setChecked(True)
        info2.setChecked(True)
        info3.setChecked(True)
        info4.setChecked(True)
        info5.setChecked(True)
        info6.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info1)
        vbox.addWidget(info2)
        vbox.addWidget(info3)
        vbox.addWidget(info4)
        vbox.addWidget(info5)
        vbox.addWidget(info6)
        vbox.addStretch(1)
        groupBox1.setLayout(vbox)
        return groupBox1

    def createGroup2(self):
        groupBox2 = QGroupBox("Reports")
        info7 = QRadioButton("Report")
        info8 = QRadioButton("Report Preop")
        info7.setChecked(True)
        info8.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info7)
        vbox.addWidget(info8)
        vbox.addStretch(1)
        groupBox2.setLayout(vbox)
        return groupBox2

    def createGroup3(self):
        groupBox3 = QGroupBox("Scales/Scans")
        info9 = QRadioButton("UPDRS On")
        info10 = QRadioButton("UPDRS Off")
        info11 = QRadioButton("Video")
        info12 = QRadioButton("Video File")
        info13 = QRadioButton("MRI")
        info14 = QRadioButton("fpcit_spect")
        info15 = QRadioButton("NMSQ")
        info16 = QRadioButton("MoCa")
        info17 = QRadioButton("DemTect")
        info18 = QRadioButton("MMST")
        info19 = QRadioButton("PDQ8")
        info20 = QRadioButton("BDI2")
        info21 = QRadioButton("PDQ39")
        info9.setChecked(True)
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
        info21.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info9)
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
        vbox.addWidget(info21)
        vbox.addStretch(1)
        groupBox3.setLayout(vbox)
        return groupBox3

    def createGroup4(self):
        groupBox4 = QGroupBox("DBS")
        info22 = QRadioButton("Outpat Contact")
        info23 = QRadioButton("nch")
        info24 = QRadioButton("Briefing")
        info25 = QRadioButton("Briefing Doctor")
        info26 = QRadioButton("DBS Conference")
        info27 = QRadioButton("Decision DBS")
        info22.setChecked(True)
        info23.setChecked(True)
        info24.setChecked(True)
        info25.setChecked(True)
        info26.setChecked(True)
        info27.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info22)
        vbox.addWidget(info23)
        vbox.addWidget(info24)
        vbox.addWidget(info25)
        vbox.addWidget(info26)
        vbox.addWidget(info27)
        vbox.addStretch(1)
        groupBox4.setLayout(vbox)
        return groupBox4

    def createGroup5(self):
        groupBox5 = QGroupBox("LEDD")
        info28 = QRadioButton("LEDD")
        info28.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info28)
        vbox.addStretch(1)
        groupBox5.setLayout(vbox)
        return groupBox5

    def createGroup6(self):
        groupBox6 = QGroupBox("Medication")
        info29 = QRadioButton("Levodopa/Carbidopa")
        info30 = QRadioButton("Levodopa/Carbidopa CR")
        info31 = QRadioButton("Entacapone")
        info32 = QRadioButton("Tolcapone")
        info33 = QRadioButton("Pramipexole")
        info34 = QRadioButton("Ropinirole")
        info35 = QRadioButton("Rotigotine")
        info36 = QRadioButton("Selegiline, oral")
        info37 = QRadioButton("Selegiline, sublingual")
        info38 = QRadioButton("Rasagiline")
        info39 = QRadioButton("Amantadine")
        info40 = QRadioButton("Apomorphine")
        info41 = QRadioButton("Piribedil")
        info42 = QRadioButton("Safinamid")
        info43 = QRadioButton("Opicapone")
        info44 = QRadioButton("Other")
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
        info44.setChecked(True)
        vbox = QVBoxLayout()
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
        vbox.addWidget(info44)
        vbox.addStretch(1)
        groupBox6.setLayout(vbox)
        return groupBox6

    def createGroup7(self):
        groupBox7 = QGroupBox("Tests")
        info45 = QRadioButton("UPDRS II")
        info46 = QRadioButton("H&Y")
        info47 = QRadioButton("HRUQ")
        info48 = QRadioButton("EQ5D")
        info49 = QRadioButton("S&E")
        info50 = QRadioButton("icVRCS")
        info51 = QRadioButton("inexVRCS")
        info45.setChecked(True)
        info46.setChecked(True)
        info47.setChecked(True)
        info48.setChecked(True)
        info49.setChecked(True)
        info50.setChecked(True)
        info51.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info45)
        vbox.addWidget(info46)
        vbox.addWidget(info47)
        vbox.addWidget(info48)
        vbox.addWidget(info49)
        vbox.addWidget(info50)
        vbox.addWidget(info51)
        vbox.addStretch(1)
        groupBox7.setLayout(vbox)
        return groupBox7

    def createGroup8(self):
        groupBox8 = QGroupBox("Notes")
        info52 = QRadioButton("Notes")
        info52.setChecked(True)
        vbox = QVBoxLayout()
        vbox.addWidget(info52)
        vbox.addStretch(1)
        groupBox8.setLayout(vbox)
        return groupBox8

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_bottom = QHBoxLayout()
        self.button_savereturn = QPushButton('Save settings \nand return')
        self.button_savereturn.clicked.connect(self.onClickedSaveReturn)
        self.button_close = QPushButton('Save and \nclose')
        self.button_close.clicked.connect(self.close)  

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
