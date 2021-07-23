# Hi :) Also ich erhalte keine Fehlermeldung sondern nur die Antwort "Filename:
# C:\Users\Anwender\PycharmProjects\DBS_Patients\data\General.csv not found. Please double-check!". Aber eigentlich
# macht dieser Pfad auch keinen Sinn, weil es keinen Ordner "data" in DBS_Patients gibt. Die Datei liegt bei mir
# direkt im DBS_Patients Ordner also müsste ich thereotisch nur eine directory nach hinten gehen. Ich weiß aber einfach
# nicht woher er diesen Pfad nimmt bzw. wo ich diesen verändern kann.
# Alles andere funktioniert.

# Hi! Versuch die Fehler unten zu lesen, das hilft Dir meistens weiter zu kommen und dann die Debug Funktion nutzen
# (oben der grüne Käfer) bis zu der Linie mit dem Fehler. Das Skript ging bei mir auch nicht, weil der Dateiname
# als General.csv bei Zeile 76 definiert war. Habe das mal geändert, jetzt geht es (zumindest bei mir).
# Jetzt sollte es aber gehen und auch das tun, was wir gerne hätten. Das heißt , wenn wir die gleiche Struktur der
# Daten haben. Erstelle bitte einen Ordner ./data in dem VErzeichnis DBS_patients. Das hat zwei Vorteile: i)
# haben wir den gleichen AUfbau und ii) ist dieser Ordner per Definition Teil von dem, was er ignoriert beim HOchladen
# (siehe .gitignore). Dann werden auch keine Daten versehentlich hochgeladen.
# Bevor wir uns GUImain widmen, bitte noch dasTODO weiter unten beachten und das zuerst machen.
# Außerdem noch zwei allgemeine Bitten: 1. Mach Dich schon einmal dran, die Startseite von GitHub (also die Readme)
# Datei zu verändern. Das Repository und Deine Arbeit daran wird am Ende auch Teil der Arbeit werden und dazu gehört auch
# die Form. 2. Kannst Du bitte eine allgemeine Anleitung erstellen, wie man ein Projekt bei GitHub startet und das ins
# Wiki setzen?

#  Den Rest bekommen wir auch noch hin ; )



import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, \
    QWidget, QLabel, QFileDialog
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
            General.write_csv_temp(df, idx_PID)  # writes data to temporary file, so that it may be used later
            # TODO: here a GUI is required which shows some of the main data similar to GUIgeneral_data.py and enables
            #  to continue to GUImain.py
            self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = CheckPID()
    dlg.show()
    sys.exit(app.exec_())
