# Filename: test_pyqt5.py

# Hi David. Das war schwieriger als ich gedacht habe. Ich habe eigentlich den ganzen Tag damit verbracht diese Datei zu speichern. Trotzdem klappt das ganze noch nicht
# 100%, da er zwar das Fenster öffnet zum abspeichern aber nichts abspeichert. 
# Ich habe noch eine Frage zum Inhalt. Ich dachte, ich darf den Namen und das Alter nicht veröffentlichen aber Du meintest, ich sollte schon einmal die Inhalte einfügen.
# Tut mir Leid, dass ich im Moment nicht so schnell voran komme. Ich glaube aber, sobald ich eine Box fertig habe, wird das ganze viel schneller gehen. 

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


# Hi Michaela, ich habe das mal vom Aufbau geändert. Das GUI wirkt in seiner Form zwar etwas komplexer, aber ist in
# seiner Logik viel stimmiger alles in allem. Kurze Erklärung: self.layout ist das gesamte Layout und ist vertikal
# aufgebaut, dann haben wir die erste Box (optionbox1) die allgemeine Daten beinhaltet und es gibt (bisher) eine Leiste
# mit Knöpfen, die man auch erweitern kann. Darf ich vorschlagen, dass Du versuchst das nachzuvollziehen und erst einmal
# alles an Inhalten einfügst. Wenn Du soweit bist, kannst Du gerne versuchen eine zweite Box auf der rechten Seite
# einzufügen (Du kannst Dir vielleicht noch Zeile 292f bei
# https://github.com/dpedrosac/cDBS/blob/master/utils/settingsNIFTIprocAnts.py anschauen ; ) Die FUnktion greetings
# lassen wir einfach weg, die brauchen wir nicht)


def greeting():
    """Function."""
    if QDialogButtonBox.Cancel:
        print('Close')
    else:
        print('Thank You!')


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
