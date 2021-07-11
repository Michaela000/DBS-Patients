# Filename: GUIcheckPID.py

"""Dialog-Style application."""

import sys
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, \
    QFileDialog, QWidget, QLabel


# Hey, also alles gut! Ehrlicherweise hast Du viel mehr gemacht, als was ich wollte. Es ging mir eigentlich nur
# darum, dass Du mal ein wenig mit dem Code spielst und versuchst Inhalt einzufügen. Das mit dem Speichern und
# Löschen, das bekommen wir alles noch später hin. Ich habe den Eindruck,  es würde Dir mehr bringen, wenn wir erst noch
# ein Paar Zwischenschritte einfügen, bevor wir mit "decorator" starten (trotzdem mega
# gut, dass Du das hinbekommen hast). Meine Bitte für die nächsten Tage wäre also, dass Du ein GUI erstellst wie das
# aus dem Makro der Excel Datei (preoperative) ein GUI für die Medikation (also alle Parkinson Medikamente die es gibt)
# und ein GUI für die Eingabe der Daten (also der PID), sodass man prüfen kann, ob es den Menschen gibt oder nicht.
# Zum jetzigen Zeitpunkt noch keine Funktionen und keine Verknüpfungen, reines Aussehen des GUI. Den Rest machen wir
# noch. Das speicherst Du unter einem Ordner GUI im Hauptverzeichnis.

# Habe ein wenig den Code aufgeräumt und ein Paar kleinere Extras ergänzt, die später klarer werden ; )


class CheckPID(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle('Check for information related so far to the entered PID')
        self.setGeometry(400, 100, 750, 900)  # left, right, height, width
        self.move(850, 425)

        self.entire_layout = QVBoxLayout(self)
        self.content_boxes = QHBoxLayout(self)
        self.optionbox1 = QGroupBox('Is the information related to PID correct?')
        self.settings_optionsbox1 = QVBoxLayout(self.optionbox1)

        # ====================    Create Content for First Option box on Top left      ====================
        self.subj_name = QLabel('Name:\t\t')
        self.lineEditFilename = QLineEdit()

        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_name)
        lay1.addWidget(self.lineEditFilename)
        lay1.addStretch()

        self.subj_code = QLabel('Code:\t\t')
        self.lineEditFilename = QLineEdit()

        lay2 = QHBoxLayout()
        lay2.addWidget(self.subj_code)
        lay2.addWidget(self.lineEditFilename)
        lay2.addStretch()

        self.settings_optionsbox1.addLayout(lay1)
        self.settings_optionsbox1.addLayout(lay2)

        # ====================    Merge boxes      ====================
        self.content_boxes.addWidget(self.optionbox1)

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_bottom = QHBoxLayout()
        self.button_savereturn = QPushButton('Yes. \nContinue')
        self.button_savereturn.clicked.connect(self.onClickedSaveReturn)
        self.button_close = QPushButton('No. \nReturn')
        self.button_close.clicked.connect(self.close)

        layout_bottom.addStretch(1)
        layout_bottom.addWidget(self.button_savereturn)
        layout_bottom.addWidget(self.button_close)

        # ====================    Add boxes and buttons to self.entire_layout      ====================
        self.entire_layout.addLayout(self.content_boxes)
        self.entire_layout.addLayout(layout_bottom)

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
    dlg = CheckPID()
    dlg.show()
    sys.exit(app.exec_())
