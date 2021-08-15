# Hallo David.
# Ich habe mich die letzten zwei Tage nochmal ausführlich mit den Tabellen von Pre und Postoperative beschäftigt
# (bei Intraoperative habe ich leider keine Patienten)
# Insgesamt sind es viele kleine Unstimmigkeiten, die ich mit Dir besprechen müsste z.B. Unterschiede zu Deiner Tabelle oder
# allgemeine Fragen (z.B. Du wolltest mir die Liste mit Programmen vom IPG zeigen)
# Ich glaube allerdings schon, dass das Ganze etwas Zeit in Anspruch nehmen wird und deswegen wollte ich es schon einmal angesprochen haben.
# Könnten wir dafür vielleicht noch einmal einen Termin vereinbaren? Ich denke das sollte sowohl telefnonischt als auch persönlich gut machbar sein.
# Ich würde mich da nach Dir richten. Zeitlich bin ich sehr offen, auch wenn es sehr früh oder spät wäre.

# Ein paar allgemeine Fragen hätte ich aber noch:
# Wenn bei Levodopa LT bzw RT steht, gehört das dann zu "Levodopa/Carbidopa" oder zu "Levodopa/Carbidopa CR"?
# Wenn da steht "Nacom 200mg" sind das dann wirklich 200 oder aus irgendeinem Grund auch nur 100mg?
# Es gibt auch so kryptische Medikamente wo steht: "Stalevo 50/12,5/200mg" oder "Levocomp ret. 200mg/50mg"


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
