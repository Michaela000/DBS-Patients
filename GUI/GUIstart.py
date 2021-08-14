import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget
from GUI.GUI_Main import ChooseGUI

# Hallo David.

# Stimmt, die Verbindung mit GUIMain war noch falsch. Aber obwohl ich layout_buttons.addStretch(1) eingegeben habe, sind die beiden
# Button nicht mittig.

# Vielen Dank für die ganzen hilfreichen Antworten. Ich versuche alles in der Tabelle bzw. im Wiki Eintrag umzusetzen.

# Leider sammeln sich immer mehr Fragen bezüglich der Tabelle.
    # 1. Stimmt es, dass sowohl akinetic-rigid, hypokinetic-rigid and bradykinetic-rigid in die gleiche Diagnose "hypokinetic-rigid
    #    parkinson-syndorome (PD2) fallen? Ich war mir da sehr unsicher und hab es deshalb noch nicht eingetragen.
    ## ==> ja genau
    # 2. Bei vielen Levodopa Medikamenten steht "100/25mg". Da weiß ich jetzt, dass ich mit 100mg rechnen muss. Aber andere
    #    haben trotzdem einfach "Madopar 125T" oder "Madopar 125mg" in der Tabelle stehen. Dabei bin ich jetzt
    #    verwirrt, ob ich mit 100 oder 125mg rechnen soll.
    #== Das ist jeweils 100/25 aber ist tatsächlich sehr verwirrend
    # 3. Ich wollte auch nochmal sagen, dass manche Briefe nicht so gut kopiert wurden, wodurch oftmals ein paar Zeilen fehlen.
    # 4. Werden alle Arten von Dystonie in der Tabelle einfach nur zu "Dystonia (DT)" zusammengefasst? Hatte bei einem Patienten
    #    "Segmentale Dystonie mit Torticollis spasmodicus" und bei einem anderen "generalized dystonia" und da wollte ich nochmal
    #    kurz nachfragen, damit ich nichts falsch mache
    #==> ne, das ist alles Dystonie
    # 5. Am Anfang hieß es, dass ich "IPG" weglassen soll im General.py, aber du hattest es bei der letzten Aufgabe dazu geschrieben.
    #    Ist das jetzt doch wichtig und wenn ja, für was steht IPG?
    ##==> Das ist der Impulsgenerator und ich glaube ich wollte nur damit ausdrücken, dass die Seriennummer aufgeschrieben wird
    # 6. Bin mir bei dem Unterschied zwischen "Report" und "Report Preop" nicht sicher. Wenn ich keinen Report für Preoperative hätte, dann
    #    könnte ich theoretisch auch nicht die Tabelle machen? Also diese beiden Punkte waren bei mir immer ein großes Fragezeichen.
    ##==> Ich glaube es ging mir eher um die neurochirurgischen Briefe, also bei intraoperative

# Tut mir Leid, dass es doch so viel geworden ist.
##==> Alles gut!


class CheckForGUIMain(QDialog):
    """Very first GUI only providing a means to enter a PID (according to the ORBIS system at the
    Department of Neurology at the University Hospital of Gießen and Marburg. Several options are possible
    after entering a PID: 1. if existent -> GuiMain, 2. if inexistent enter data in general table"""

    def __init__(self, parent=None):
        """Initialize."""

        self.GuiMain = ChooseGUI()
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
        self.hide()
        self.GuiMain.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = CheckForGUIMain()
    dlg.show()
    sys.exit(app.exec_())
