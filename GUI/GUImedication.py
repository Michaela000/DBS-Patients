import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, \
    QHBoxLayout, QLabel, QFileDialog, QWidget


class MedicationDialog(QDialog):
    """Dialog to introduce the medication at a specific date. All unrelated """

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Parkinson Medication')
        self.setGeometry(200, 100, 280, 170)
        self.move(850, 200)

        self.layout = QVBoxLayout(self)
        self.optionbox1 = QGroupBox('Subject Medication')
        self.settings_list = QVBoxLayout(self.optionbox1)

        # ====================    Create Content for First Option box on Top left      ====================
        self.subj_Levodopa_Carbidopa = QLabel('Levodopa/Carbidopa:\t')
        self.lineEditFilename = QLineEdit()
        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_Levodopa_Carbidopa)
        lay1.addWidget(self.lineEditFilename)
        lay1.addStretch()

        self.subj_Levodopa_Carbidopa_CR = QLabel('Levodopa/Carbidopa CR:\t')
        self.lineEditFilename = QLineEdit()
        lay2 = QHBoxLayout()
        lay2.addWidget(self.subj_Levodopa_Carbidopa_CR)
        lay2.addWidget(self.lineEditFilename)
        lay2.addStretch()

        self.subj_Entacapone = QLabel('Entacapone:\t\t')
        self.lineEditFilename = QLineEdit()
        lay3 = QHBoxLayout()
        lay3.addWidget(self.subj_Entacapone)
        lay3.addWidget(self.lineEditFilename)
        lay3.addStretch()

        self.subj_Tolcapone = QLabel('Tolcapone:\t\t')
        self.lineEditFilename = QLineEdit()
        lay4 = QHBoxLayout()
        lay4.addWidget(self.subj_Tolcapone)
        lay4.addWidget(self.lineEditFilename)
        lay4.addStretch()

        self.subj_Pramipexole = QLabel('Pramipexole:\t\t')
        self.lineEditFilename = QLineEdit()
        lay5 = QHBoxLayout()
        lay5.addWidget(self.subj_Pramipexole)
        lay5.addWidget(self.lineEditFilename)
        lay5.addStretch()

        self.subj_Ropinirole = QLabel('Ropinirole:\t\t')
        self.lineEditFilename = QLineEdit()
        lay6 = QHBoxLayout()
        lay6.addWidget(self.subj_Ropinirole)
        lay6.addWidget(self.lineEditFilename)
        lay6.addStretch()

        self.subj_Rotigotine = QLabel('Rotigotine:\t\t')
        self.lineEditFilename = QLineEdit()
        lay7 = QHBoxLayout()
        lay7.addWidget(self.subj_Rotigotine)
        lay7.addWidget(self.lineEditFilename)
        lay7.addStretch()

        self.subj_Selegiline_oral = QLabel('Selegiline oral:\t\t')
        self.lineEditFilename = QLineEdit()
        lay8 = QHBoxLayout()
        lay8.addWidget(self.subj_Selegiline_oral)
        lay8.addWidget(self.lineEditFilename)
        lay8.addStretch()

        self.subj_Selegiline_sublingual = QLabel('Selegiline sublingual:\t')
        self.lineEditFilename = QLineEdit()
        lay9 = QHBoxLayout()
        lay9.addWidget(self.subj_Selegiline_sublingual)
        lay9.addWidget(self.lineEditFilename)
        lay9.addStretch()

        self.subj_Rasagiline = QLabel('Rasagiline:\t\t')
        self.lineEditFilename = QLineEdit()
        lay10 = QHBoxLayout()
        lay10.addWidget(self.subj_Rasagiline)
        lay10.addWidget(self.lineEditFilename)
        lay10.addStretch()

        self.subj_Amantadine = QLabel('Amantadine:\t\t')
        self.lineEditFilename = QLineEdit()
        lay11 = QHBoxLayout()
        lay11.addWidget(self.subj_Amantadine)
        lay11.addWidget(self.lineEditFilename)
        lay11.addStretch()

        self.subj_Apomorphine = QLabel('Apomorphine:\t\t')
        self.lineEditFilename = QLineEdit()
        lay12 = QHBoxLayout()
        lay12.addWidget(self.subj_Apomorphine)
        lay12.addWidget(self.lineEditFilename)
        lay12.addStretch()

        self.subj_Piribedil = QLabel('Piribedil:\t\t\t')
        self.lineEditFilename = QLineEdit()
        lay13 = QHBoxLayout()
        lay13.addWidget(self.subj_Piribedil)
        lay13.addWidget(self.lineEditFilename)
        lay13.addStretch()

        self.subj_Safinamid = QLabel('Safinamid:\t\t')
        self.lineEditFilename = QLineEdit()
        lay14 = QHBoxLayout()
        lay14.addWidget(self.subj_Safinamid)
        lay14.addWidget(self.lineEditFilename)
        lay14.addStretch()

        self.subj_Opicapone = QLabel('Opicapone:\t\t')
        self.lineEditFilename = QLineEdit()
        lay15 = QHBoxLayout()
        lay15.addWidget(self.subj_Opicapone)
        lay15.addWidget(self.lineEditFilename)
        lay15.addStretch()

        self.subj_Other = QLabel('Other:\t\t\t')
        self.lineEditFilename = QLineEdit()
        lay16 = QHBoxLayout()
        lay16.addWidget(self.subj_Other)
        lay16.addWidget(self.lineEditFilename)
        lay16.addStretch()

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

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_bottom = QHBoxLayout()
        self.button_savereturn = QPushButton('Save settings \nand return')
        self.button_savereturn.clicked.connect(self.onClickedSaveReturn)

        layout_bottom.addStretch(1)
        layout_bottom.addWidget(self.button_savereturn)

        self.layout.addWidget(self.optionbox1)
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
