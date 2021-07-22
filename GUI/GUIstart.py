import sys
import GUI_Main

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget

# Hallo David. Ich habe versucht deine Ratschläge umzusetzen. Mir fehlt allerdings noch der hintere Teil ab "Die Möglichkeit gibt
# diese zu bearbeiten (...)". Ich habe zu jeder veränderten GUI einen kleinen Text geschrieben.
# Es tut mir wirklich Leid, dass du dich sogar in deinem Urlaub, um mich kümmern musst. Ich hoffe, dass du trotzdem eine schöne
# Urlaubszeit hast.

# Ich glaube auch, dass die Abkürzungen in dem Verzeichnis sinnvoll wären. Die meisten Abkürzungen habe ich auch herausgefunden,
# aber Begriffe wie "nch" oder so sind mir noch etwas schleierhaft.
# Das größte Problem habe ich aber tatsächlich mit den Medikamenten, da ich häufig gar nicht weiß zu welcher "Kategorie" die einzelnen 
# Medikamente gehören. z.B. Ramipril, Amitriptylin etc.
# Aber das kann ich bestimmt auch in der Klinik nachfragen. Marina hat mir auch angeboten, dass ich jeder Zeit zu ihr gehen kann bei Fragen. 


# Hi! Complete und DBS/IPG ksnndt Du einfach weglassen.
#
# Also ein Paar Vorschläge für Änderungen, um die ich Dich bitten würde: 1. sollte GUIcheckPID nur die PID abfragen
# (also so sein wie GUI_ID.py nur anders heißen) und dann direkt die Datei general laden und diese vergleichen,
# damit im Falle, dass es etwas findet (also wenn die PID bei ./data/general_data.csv schon besteht) ein weiteres GUI
# öffnet, in dem alle Daten wiedergegeben werden (also etwas wue GUIstart.py, was aber auch anders heißen sollte).
# Bei dem jetzigen GUIstart.py stimmen die Schaltflächen dann auch nicht, die sollten zwei Möglichkeiten geben:
# a) Einverstanden und b) zurück. Wenn man einverstanden klickt hatte ich mir vorgestellt, dass man auf ein "GUImain.py"
# kommt in dem es drei Knöpfe gibt: i) preoperative, ii) intraoperative und iii) postoperative. Das wiederum öffnet
# jeweils eine Funktion GUI_xxx welche die vorhandenen Daten lädt (wenn gespeichert unter ./data/xxx) und die
# Möglichkeit gibt diese zu bearbeiten oder die Eingabe der Daten zulässt. Lass uns doch versuchen in den nächsten
# WOchen diese Struktur zu schaffen, verknüpfen kann man das immer noch bzw. wenn wir es schnell hinbekommen zeige ich
# Dir, wie das geht. Kannst Du mir zeigen, an welcher Stelle auf dem Wiki die Abkürungen zu finden sind? Ich denke, es
# wäre vielleicht sinnvoll hier: https://agbun.miraheze.org/wiki/List_of_available_questionnaires


# TODO: 1. Eine Funktion erstellen, die alle csv Dateien aus dem Ordner ./temp löscht beim schließen von GUIstart


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
