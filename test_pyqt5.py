# Filename: test_pyqt5.py

"""Dialog-Style application."""

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
from PyQt5.QtWidgets import QLabel, QFileDialog, QWidget, QMainWindow

# Hey, also alles gut! Ehrlicherweise hast Du viel mehr gemacht, als was ich wollte. Es ging mir eigentlich nur
# darum, dass Du mal ein wenig mit dem Code spielst und versuchst Inhalt einzufügen. Das mit dem Speichern und
# Löschen, das bekommen wir alles noch später hin. Ich habe den Eindruck,  es würde Dir mehr bringen, wenn wir erst noch
# ein Paar Zwischenschritte einfügen, bevor wir mit "decorator" starten (trotzdem mega
# gut, dass Du das hinbekommen hast). Meine Bitte für die nächsten Tage wäre also, dass Du ein GUI erstellst wie das
# aus dem Makro der Excel Datei (preoperative) ein GUI für die Medikation (also alle Parkinson Medikamente die es gibt)
# und ein GUI für die Eingabe der Daten (also der PID), sodass man prüfen kann, ob es den Menschen gibt oder nicht.
# Zum jetzigen Zeitpunkt noch keine Funktionen und keine Verknüpfungen, reines Aussehen des GUI. Den Rest machen wir
# noch. Das speicherst Du unter einem Ordner GUI im Hauptverzeichnis.

# P.S.: Du hast natürlich Recht, kein personenbezogener Inhalt, das war verwirrend von mir. Sorry! Mir ist
# nichts besseres eingefallen.


class Dialog(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Dialog_Test')
        self.setGeometry(200, 100, 280, 170)
        self.move(850, 425)

        self.layout = QVBoxLayout(self)
        self.optionbox1 = QGroupBox('Personal data')
        self.settings_list = QVBoxLayout(self.optionbox1)

        # ====================    Create Content for First Option box on Top left      ====================
        self.subj_name = QLabel('Name:\t\t')
        self.lineEditFilename = QLineEdit()

        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_name)
        lay1.addWidget(self.lineEditFilename)
        lay1.addStretch()

        self.subj_age = QLabel('Age:\t\t')
        self.lineEditFilename = QLineEdit()

        lay2 = QHBoxLayout()
        lay2.addWidget(self.subj_age)
        lay2.addWidget(self.lineEditFilename)
        lay2.addStretch()

        self.settings_list.addLayout(lay1)
        self.settings_list.addLayout(lay2)

        # ====================    Create Content for Second Option box on Top right      ====================
        # TODO: rechte Seite

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
    def open_dialog_box(self):
        option = QFileDialog.Options()
        # first parameter is self; second is the Window Title, third title is Default File Name, fourth is FileType,
        # fifth is options
        file = QFileDialog.getOpenFileName(self, "Save File Window Title", "default.txt", "All Files (*)", options=option)
        print(file)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = Dialog()
    dlg.show()
    sys.exit(app.exec_())
