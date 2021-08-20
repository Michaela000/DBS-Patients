import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QLabel, QFileDialog, QWidget, QGridLayout


class MedicationDialog(QDialog):
    """Dialog to introduce the medication at a specific date. All unrelated """

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Parkinson Medication')
        self.setGeometry(200, 100, 280, 170)
        self.move(700, 250)


        layout_general = QGridLayout(self)
        self.setLayout(layout_general)

        # Optionbox upper left corner
        self.optionbox1 = QGroupBox('Patient Medication')
        self.optionbox1Content = QVBoxLayout(self.optionbox1)
        layout_general.addWidget(self.optionbox1, 0, 0)

        self.subj_Levodopa_Carbidopa = QLabel('Levodopa/Carbidopa (mg):\t')
        self.lineEditLevodopaCarbidopa = QLineEdit()
        self.subj_Selegiline_sublingual = QLabel('Selegiline sublingual (mg):\t')
        self.lineEditSelegiline_sublingual = QLineEdit()
        self.subj_Levodopa_Carbidopa_CR = QLabel('Levodopa/Carbidopa CR (mg):')
        self.lineEditLevodopaCarbidopaCR = QLineEdit()
        self.subj_Rasagiline = QLabel('Rasagiline (mg):\t\t')
        self.lineEditRasagiline = QLineEdit()
        self.subj_Entacapone = QLabel('Entacapone (mg):\t\t')
        self.lineEditEntacapone = QLineEdit()
        self.subj_Amantadine = QLabel('Amantadine (mg):\t\t')
        self.lineEditAmantadine = QLineEdit()
        self.subj_Tolcapone = QLabel('Tolcapone (mg):\t\t')
        self.lineEditTolcapone = QLineEdit()
        self.subj_Apomorphine = QLabel('Apomorphine (mg):\t\t')
        self.lineEditApomorphine = QLineEdit()
        self.subj_Pramipexole = QLabel('Pramipexole (mg):\t\t')
        self.lineEditPramipexole = QLineEdit()
        self.lineEditPramipexole.setFixedWidth(103)
        self.subj_Piribedil = QLabel('Piribedil (mg):\t\t')
        self.lineEditPiribedil = QLineEdit()
        self.lineEditPiribedil.setFixedWidth(103)
        self.subj_Ropinirole = QLabel('Ropinirole (mg):\t\t')
        self.lineEditRopinirole = QLineEdit()
        self.subj_Safinamid = QLabel('Safinamid (mg):\t\t')
        self.lineEditSafinamid = QLineEdit()
        self.subj_Rotigotine = QLabel('Rotigotine (mg):\t\t')
        self.lineEditRotigotine = QLineEdit()
        self.subj_Opicapone = QLabel('Opicapone (mg):\t\t')
        self.lineEditOpicapone = QLineEdit()
        self.subj_Selegiline_oral = QLabel('Selegiline oral (mg):\t\t')
        self.lineEditSelegiline_oral = QLineEdit()
        self.lineEditSelegiline_oral.setFixedWidth(103)
        self.subj_Other = QLabel('Other:\t\t\t')
        self.lineEditOther = QLineEdit()
        self.lineEditOther.setFixedHeight(50)
        self.lineEditOther.setFixedWidth(300)

        box1line1 = QHBoxLayout()
        box1line1.addWidget(self.subj_Levodopa_Carbidopa)
        box1line1.addWidget(self.lineEditLevodopaCarbidopa)
        box1line1.addWidget(self.subj_Selegiline_sublingual)
        box1line1.addWidget(self.lineEditSelegiline_sublingual)
        box1line1.addStretch()

        box1line2 = QHBoxLayout()
        box1line2.addWidget(self.subj_Levodopa_Carbidopa_CR)
        box1line2.addWidget(self.lineEditLevodopaCarbidopaCR)
        box1line2.addWidget(self.subj_Rasagiline)
        box1line2.addWidget(self.lineEditRasagiline)
        box1line2.addStretch()

        box1line3 = QHBoxLayout()
        box1line3.addWidget(self.subj_Entacapone)
        box1line3.addWidget(self.lineEditEntacapone)
        box1line3.addWidget(self.subj_Amantadine)
        box1line3.addWidget(self.lineEditAmantadine)
        box1line3.addStretch()

        box1line4 = QHBoxLayout()
        box1line4.addWidget(self.subj_Tolcapone)
        box1line4.addWidget(self.lineEditTolcapone)
        box1line4.addWidget(self.subj_Apomorphine)
        box1line4.addWidget(self.lineEditApomorphine)
        box1line4.addStretch()

        box1line5 = QHBoxLayout()
        box1line5.addWidget(self.subj_Pramipexole)
        box1line5.addWidget(self.lineEditPramipexole)
        box1line5.addWidget(self.subj_Piribedil)
        box1line5.addWidget(self.lineEditPiribedil)
        box1line5.addStretch()

        box1line6 = QHBoxLayout()
        box1line6.addWidget(self.subj_Ropinirole)
        box1line6.addWidget(self.lineEditRopinirole)
        box1line6.addWidget(self.subj_Safinamid)
        box1line6.addWidget(self.lineEditSafinamid)
        box1line6.addStretch()

        box1line7 = QHBoxLayout()
        box1line7.addWidget(self.subj_Rotigotine)
        box1line7.addWidget(self.lineEditRotigotine)
        box1line7.addWidget(self.subj_Opicapone)
        box1line7.addWidget(self.lineEditOpicapone)
        box1line7.addStretch()

        box1line8 = QHBoxLayout()
        box1line8.addWidget(self.subj_Selegiline_oral)
        box1line8.addWidget(self.lineEditSelegiline_oral)
        box1line8.addStretch()

        box1line9 = QHBoxLayout()
        box1line9.addWidget(self.subj_Other)
        box1line9.addWidget(self.lineEditOther)
        box1line9.addStretch()

        self.optionbox1Content.addLayout(box1line1)
        self.optionbox1Content.addLayout(box1line2)
        self.optionbox1Content.addLayout(box1line3)
        self.optionbox1Content.addLayout(box1line4)
        self.optionbox1Content.addLayout(box1line5)
        self.optionbox1Content.addLayout(box1line6)
        self.optionbox1Content.addLayout(box1line7)
        self.optionbox1Content.addLayout(box1line8)
        self.optionbox1Content.addLayout(box1line9)
        self.optionbox1.setLayout(self.optionbox1Content)



        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_bottom = QHBoxLayout()
        self.button_save_return = QPushButton('Save settings \nand return')
        self.button_save_return.clicked.connect(self.onClickedSaveReturn)

        layout_bottom.addStretch(1)
        layout_bottom.addWidget(self.button_save_return)

        hlay_bottom = QHBoxLayout()
        hlay_bottom.addStretch(2)
        hlay_bottom.addWidget(self.button_save_return)
        hlay_bottom.addStretch(1)

        layout_general.addLayout(hlay_bottom, 4, 0, 1,3)


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
