import sys
import GUI_Preoperative
import GUI_Intraoperative
import GUI_Postoperative

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget

# Hallo David.
# Ich habe versucht mal GUI_Main zu erstellen.
# Dazu habe ich aber noch zwei kleine Fragen.
# 1. Er öffnet mir nicht die unterschiedlichen GUI's nach Knopfdruck also scheint mir noch irgendetwas essentielles zu fehlen
# 2. Gibt es eine Möglichkeit, die Knöpfe irgendwie in die Mitte zu verschieben?

class ChooseGUI(QDialog):
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
        self.button_openGUI_Preoperative = QPushButton('Open GUI \nPreoperative')
        self.button_openGUI_Preoperative.clicked.connect(self.onClicked_openGUI_Preoperative)
        self.button_openGUI_Intraoperative = QPushButton('Open GUI \nIntraoperative')
        self.button_openGUI_Intraoperative.clicked.connect(self.onClicked_openGUI_Intraoperative)
        self.button_openGUI_Postoperative = QPushButton('Open GUI \nPostoperative')
        self.button_openGUI_Postoperative.clicked.connect(self.onClicked_openGUI_Postoperative)
        self.button_close = QPushButton('Close GUI')
        self.button_close.clicked.connect(self.close)

        layout_buttons.addStretch(1)
        layout_buttons.addWidget(self.button_openGUI_Preoperative)
        layout_buttons.addWidget(self.button_openGUI_Intraoperative)
        layout_buttons.addWidget(self.button_openGUI_Postoperative)
        layout_buttons.addWidget(self.button_close)

        # ====================    Add boxes and buttons to self.entire_layout      ====================
        self.layout.addLayout(self.content_box)
        self.layout.addLayout(layout_buttons)

    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
    def onClicked_openGUI_Preoperative(self):
        """when button is pressed, a series of checks are performed in order to retrieve data/to set the following
        GUI """

        open(GUI_Preoperative)

    def onClicked_openGUI_Intraoperative(self):
        open(GUI_Intraoperative)

    def onClicked_openGUI_Postoperative(self):
        open(GUI_Postoperative)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = ChooseGUI()
    dlg.show()
    sys.exit(app.exec_())
