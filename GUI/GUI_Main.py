import sys
from GUI. GUI_Preoperative import PreoperativeDialog

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, \
    QWidget

# Hallo David.
# Ich habe versucht mal GUI_Main zu erstellen.
# Dazu habe ich aber noch zwei kleine Fragen.
# 1. Er öffnet mir nicht die unterschiedlichen GUI's nach Knopfdruck also scheint mir noch irgendetwas essentielles
# zu fehlen ==> ich habe das mal beispielhaft für GUI_Preoperative geschrieben. Es ist etwas kompliziert, Du musst als
# 'parent' das andere GUi angeben, das bedeutet kleiner Änderungen im Code
# super(PreoperativeDialog, self).__init__(parent) statt super(PreoperativeDialog, self).__init__()
# Das Ganze kehrt noch nicht zurück, weil es keinen Knopf gibt. Er ist zwar angelegt, aber leider nicht eingebunden in
# das LAyout. Kannst Du mal schauen, dass Du das hinbekommst, dann binden wir das ein.
# 2. Gibt es eine Möglichkeit, die Knöpfe irgendwie in die Mitte zu verschieben?
# Klar! DU fügst am Ende ein layout_buttons.addStretch(1) ein, dann ist es symmetrisch.
# Es ist eigentlich gar nicht mehr viel, wenn das LAyout steht. Dann programmieren wir noch, dass es die Daten aus den
# CSV-Dateien holt und wir können mit der Dateneingabe und Auswertung weiter machen.


class ChooseGUI(QDialog):
    """Describes GUIMain. This GUI is responsible to open further GUI'S:
    1. Preoperative 2. Intraoperative 3. Postoperative"""

    def __init__(self, parent=None):
        """Initialize."""

        super().__init__(parent)

        # Initialize the GUIs that may be used
        self.GUIPreoperative = PreoperativeDialog(self)

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
        # open(GUI_Intraoperative)

    def onClicked_openGUI_Postoperative(self):
        print('adapt according to onClicked_run_preoperative')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = ChooseGUI()
    dlg.show()
    sys.exit(app.exec_())
