# Hallo David.

# 1. Wenn bei Levodopa LT bzw RT steht, gehört das dann zu "Levodopa/Carbidopa" oder zu "Levodopa/Carbidopa CR"?
##==> Glaube das ist ein Tippfehler, RT gibt es nicht
### --> und wozu gehört dann LT?
#### -> Das ist nur die Formuluierung (lösliche Tablette), die besonder schnell aufgenommen wird

# 3. Es gibt auch so kryptische Medikamente wo steht: "Stalevo 50/12,5/200mg" oder "Levocomp ret. 200mg/50mg": wie muss ich die berechnen?
##==> Stalevo ist ein Kombi Präparat, das aus Levodopa, Carbidopa (nicht wichtig) und Entacapon besteht.
#==> Kannst Du bitte nochmal die Bilder bei 'temp' hochladen, dass ich mal schauen kann, wie das aussieht? Ich finde das nicht mehrt
    ### --> welche Bilder? Die Tabellen habe ich noch nicht hochgeladen, da sie nicht im csv Format sind. Oder meinst du etwas anderes?
    #       Soll ich dann noch einen Ordner auf GitHub mit dem Namen "temp" erstellen? Also ich habe einen Ordner temp auf meinem PC, aber
    #       dazu hast du keinen direkten Zugriff oder?
    #       Die Angaben von Stalevo etc. steht in den Briefen (da ist bisher einfach eine markierte Lücke in der Tabelle).


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
