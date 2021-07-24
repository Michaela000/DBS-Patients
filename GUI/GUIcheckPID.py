# Hallo David. Ich hab versucht alles umzusetzen. Ich werde mich die nächsten Tage auch um die Readme und die Wiki Einträge kümmern.
# Ich bin mir aber nicht genau sicher, ob ich das Todo komplett richtig verstanden habe. Ich habe jetzt eine weitere GUI mit den
# wichtigsten Details aus general_data erstellt und sie nur etwas umbenannt. Ich weiß allerdings nicht wie ich diese Datei löschen soll,
# beim Schließen der GUI.


# Bevor wir uns GUImain widmen, bitte noch dasTODO weiter unten beachten und das zuerst machen.
# Außerdem noch zwei allgemeine Bitten: 1. Mach Dich schon einmal dran, die Startseite von GitHub (also die Readme)
# Datei zu verändern. Das Repository und Deine Arbeit daran wird am Ende auch Teil der Arbeit werden und dazu gehört auch
# die Form. 2. Kannst Du bitte eine allgemeine Anleitung erstellen, wie man ein Projekt bei GitHub startet und das ins
# Wiki setzen?


import sys
import GUI_Temp
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, \
    QWidget, QLabel
from utils.helper_functions import General, Output
from GUI.GUIgeneral_data import CheckForGeneralData


class CheckPID(QDialog):
    """Dialog."""

    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.EnterNewDataPID = CheckForGeneralData()

        self.setWindowTitle('Check for existence of subject in database')
        self.setGeometry(400, 100, 500, 300)  # left, right, width, height
        self.move(850, 425)

        self.layout = QVBoxLayout(self)  # entire layout for GUI
        self.content_box = QVBoxLayout(self)  # content of the box

        # ====================    Create Content for First Option box on Top left      ====================
        self.optionbox_guistart = QGroupBox('Please enter the PID_Orbis')
        self.settings_optionsbox1 = QVBoxLayout(self.optionbox_guistart)

        self.subj_PID = QLabel('PID-ORBIS:\t\t')
        self.lineEditPID = QLineEdit()

        self.lineEditPID.setFixedWidth(150)
        self.lineEditPID.setFixedHeight(50)

        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_PID)
        lay1.addWidget(self.lineEditPID)
        lay1.addStretch()

        self.settings_optionsbox1.addLayout(lay1)
        self.content_box.addWidget(self.optionbox_guistart)

        # ====================    Create Content for Buttons at the Bottom      ====================
        layout_buttons = QHBoxLayout()
        self.button_checkPID = QPushButton('Check for \nexistence')
        self.button_checkPID.clicked.connect(self.onClickedCheckPID)
        self.button_close = QPushButton('Close GUI')
        self.button_close.clicked.connect(self.close)

        layout_buttons.addStretch(1)
        layout_buttons.addWidget(self.button_checkPID)
        layout_buttons.addWidget(self.button_close)

        # ====================    Add boxes and buttons to self.entire_layout      ====================
        self.layout.addLayout(self.content_box)
        self.layout.addLayout(layout_buttons)

    # In the next lines, actions are defined when Buttons are pressed
    @QtCore.pyqtSlot()
    def onClickedCheckPID(self):
        """when button is pressed, a series of checks are performed in order to retrieve data/to set the following
        GUI """

        if not self.lineEditPID.text():
            Output.msg_box(text='Missing input for the PID, please enter a number', title='Missing input')
            return

        if self.lineEditPID.text():
            filename = 'general_data.csv'  # 'General.csv'
            df = General.import_dataframe(filename)
            PID2lookfor = self.lineEditPID.text().lstrip('0')  # string that is searched for in metadata file
            idx_PID = df.index[df['PID_ORBIS'] == int(PID2lookfor)].to_list()

        if not idx_PID:
            Output.msg_box(text='No corresponding subject found, please create new entry', title='Missing PID')
            self.EnterNewDataPID.show()
            self.hide()
        elif len(idx_PID) > 1:
            Output.msg_box(text='Too many entries, please double check file: {}'.format(filename),
                           title='Too many PID entries')
            return
        else:
            # writes data to temporary file, so that it may be used later
            """when button is pressed, data is added to temporary file """
            # TODO: here a GUI is required which shows some of the main data similar to GUIgeneral_data.py and enables
            #  to continue to GUImain.py

            General.write_csv_temp(df, idx_PID)
            open(GUI_Temp)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = CheckPID()
    dlg.show()
    sys.exit(app.exec_())
