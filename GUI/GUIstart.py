# Hallo David.

##==> Was hältst Du davon, dass wir uns einfach auf die GUIs konzentrieren. Dann ist Deine Arbeit das Programmieren der
# Abläufe (plus natürlich das was Du schon hast). Wäre das für Dich ok? Die IPG LIste habe ich Dir eben geschickt!

### -> Tut mir leid, dass ich die Email heute morgen verpasst habe.
###    Können wir aber gerne so machen. Ich würde mich dann heute trotzdem noch um den IPG und um die Berechnung von LEDD kümmern und diese eintragen.
###    Danach wäre ich aber dann "fertig" mit den Tabellen (bis auf die Fragen). Natürlich arbeite ich parallel dazu auch noch weiter am Code. 


# Ein paar allgemeine Fragen hätte ich aber noch:
# 1. Wenn bei Levodopa LT bzw RT steht, gehört das dann zu "Levodopa/Carbidopa" oder zu "Levodopa/Carbidopa CR"?
##==> Glaube das ist ein Tippfehler, RT gibt es nicht
# 2. Wenn da steht "Nacom 200mg" sind das dann wirklich 200 oder aus irgendeinem Grund auch nur 100mg?
##==> Nacom sind tatsächlich 200mg Levodopa
# 3. Es gibt auch so kryptische Medikamente wo steht: "Stalevo 50/12,5/200mg" oder "Levocomp ret. 200mg/50mg": wie muss ich die berechnen?
##==> STalevo ist ein KOmbi Präparat, das aus LEvodopa, Carbidopa (nicht wichtig) und Entacapon besteht.
#==> Kannst Du bitte nochmal die Bilder bei 'temp' hochladen, dass ich mal schauen kann, wie das aussieht? Ich finde das nicht mehrt


import sys

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget
from GUI.GUI_Main import ChooseGUI


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
