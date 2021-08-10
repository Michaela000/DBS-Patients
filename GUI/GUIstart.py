import sys
import GUI_Main

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget

# Hallo David.

# Ich habe gerade mit Marina telefoniert. Scheinbar muss ich gar nichts vorbereiten, sondern einfach nur im Oktober vorbei kommen und mein Praktikum starten.
# Alles weitere zum Thema Masterarbeit wird dann erst in einem halben Jahr geregelt.
# Wenn es für dich passt, würde ich vorschlagen, dass ich einfach regulär zum Semesterstart anfangen könnte? Die Vorlesungszeiten sind zwischen dem 18.10.2021 und dem 18.02.2022.

# Ich habe noch ein paar allgemeine Fragen:
    # Wenn vorne im Brief einfach nur H&Y Stadium II steht, bezieht sich das auf das OFF oder das ON? Das gleiche steht
        # manchmal auch bei UPDRS ("UPDRS Teil III x Punkte")
    # Bei einigen Patienten steht einfach nur UPDRS OFF/On: xx/xx. Bezieht sich das auf UPDRS III oder II?
    # Ist EQ-VAS das gleiche wie EQ5D?
    # Wenn ich bei postoperative mehrere Programme auf dem Brief habe, welches Programm soll ich in die Tabelle eintragen, 
        # wenn keine Beschreibung vorhanden ist, welche hauptsächlich verwendet wird? Soll ich einfach irgendein Programm wählen
        # oder gibt es da eine bestimmte Regel?
# Und ich habe noch eine wichtige Frage bezüglich des Wiki-Eintrags. Soll ich den Text so formulieren, dass man sich
    # angesprochen fühlt z.B. "If you want to add another collaborator you need to press (...)" oder als eine Stichpunktliste:
    # z.B. Add another collaborator
    #      - Press (...)
    #      - Then (...)
    # Oder ganz anders? 

class CheckForGUIMain(QDialog):
    """Very first GUI only providing a means to enter a PID (according to the ORBIS system at the
    Department of Neurology at the University Hospital of Gießen and Marburg. Several options are possible
    after entering a PID: 1. if existent -> GuiMain, 2. if inexistent enter data in general table"""

    def __init__(self, parent=None):
        """Initialize."""

        super().__init__(parent)
        self.setWindowTitle('Choose GUI')
        self.setGeometry(400, 100, 500, 300)  # left, right, width, height
        self.move(850, 425)

        self.layout = QVBoxLayout(self)  # entire layout for GUI
        self.content_box = QVBoxLayout(self)  # content of the box

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_buttons = QHBoxLayout()
        self.button_openGUImain = QPushButton('Open GUI \nMain')
        self.button_openGUImain.clicked.connect(self.onClicked_open_GUI_main)
        self.button_close = QPushButton('Close GUI')
        self.button_close.clicked.connect(self.close)

        layout_buttons.addStretch(1)
        layout_buttons.addWidget(self.button_openGUImain)
        layout_buttons.addWidget(self.button_close)

        # ====================    Add boxes and buttons to self.entire_layout      ====================
        self.layout.addLayout(self.content_box)
        self.layout.addLayout(layout_buttons)

    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
    def onClicked_open_GUI_main(self):
        """when button is pressed, a series of checks are performed in order to retrieve data/to set the following
        GUI """

        open(GUI_Main)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = CheckForGUIMain()
    dlg.show()
    sys.exit(app.exec_())
