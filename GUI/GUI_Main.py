import sys
from GUI. GUI_Preoperative import PreoperativeDialog
from GUI. GUI_Intraoperative import IntraoperativeDialog
from GUI. GUI_Postoperative import PostoperativeDialog

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget


class ChooseGUI(QDialog):
    """Describes GUIMain. This GUI is responsible to open further GUI'S:
    1. Preoperative 2. Intraoperative 3. Postoperative"""

    def __init__(self, parent=None):
        """Initialize."""

        super().__init__(parent)

        # Initialize the GUIs that may be used
        self.GUIPreoperative = PreoperativeDialog(self)
        self.GUIIntraoperative = IntraoperativeDialog(self)
        self.GUIPostoperative = PostoperativeDialog(self)

        # General settings for 'own' GUI
        self.setWindowTitle('Choose GUI')
        self.setGeometry(400, 100, 500, 300)  # left, right, width, height
        self.move(850, 425)

        self.layout = QVBoxLayout(self)  # entire layout for GUI
        self.content_box = QVBoxLayout(self)  # content of the box

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_buttons = QHBoxLayout()
        self.button_openGUI_Preoperative = QPushButton('Open GUI \nPreoperative')
        self.button_openGUI_Preoperative.clicked.connect(self.onClicked_run_preoperative)
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
        layout_buttons.addStretch(1)

        # ====================    Add boxes and buttons to self.entire_layout      ====================
        self.layout.addLayout(self.content_box)
        self.layout.addLayout(layout_buttons)

    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
    def onClicked_run_preoperative(self):
        """Opens the GUI for the preoperative data """
        self.GUIPreoperative.show()
        self.hide()

    def onClicked_openGUI_Intraoperative(self):
        print('adapt according to onClicked_run_preoperative')
        self.GUIIntraoperative.show()
        self.hide()

    def onClicked_openGUI_Postoperative(self):
        print('adapt according to onClicked_run_preoperative')
        self.GUIPostoperative.show()
        self.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = ChooseGUI()
    dlg.show()
    sys.exit(app.exec_())
