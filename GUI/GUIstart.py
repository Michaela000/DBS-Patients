import sys
import GUI_Main

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget


# Hallo David. 
# Ich hoffe Dein Urlaub war schön und entspannend :)
# Meine Tabelle zum Preoperative Teil ist fertig (außer Fragen etc.) aber ich wollte Bescheid sagen, 
# dass nur 6 von den 36 Patienten bei Dir in der Liste zu finden sind. Für mich war es daher sehr schwer alles richtig 
# einzutragen, was zu noch mehr Fragen und Lücken geführt hat.
# Ich arbeite gerade an der Postoperative Tabelle, daher hab ich mich noch nicht mit den Screenshots aus Deiner Email
# beschäftigt. Update: Die Tabelle ist heute morgen bis auf Fragen etc. auch fertig geworden (kein einziger Patient hat leider 
# mit deiner Liste überein gestimmt).
# Wäre es möglich einen festen Termin für die Woche festzulegen (ich kann nur am Donnerstag zwischen 9 und 12 Uhr nicht)?
# Dann könnten wir alles nochmal genauer besprechen und auch den weiteren Verlauf besser planen. 

# Ich habe noch ein paar allgemeine Fragen:
    # Wenn bei den Medikamenten "Levodopa 100/25mg" steht, muss ich dann mit 100 oder 125mg rechnen? 
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
