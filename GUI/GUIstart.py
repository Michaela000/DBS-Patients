import csv
import os
import GUI_Preoperative

from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QLineEdit, QVBoxLayout, QGroupBox, QHBoxLayout, \
    QWidget, QLabel

from GUI.GUIcheckPID import CheckPID
from utils.helper_functions import General, Output
from dependencies import ROOTDIR

# Hallo David. Ich habe versucht die Änderungen durchzuführen. Aber habe ich das richtig verstande, das in dieser csv Datei die persönlichen Daten stehen?
# Also darf ich diese Textdatei nicht auf github hochladen?
# Da ich mir bei dem ganzen Thema etwas unsicher bin, habe ich als Probe einfach nur meinen Namen (ist sowieso auf github) und eine Fake-PID (ABCDE) eingegeben.
# Ich hätte noch eine Frage bezüglich der Informationen die in general stehen sollen: Ich hab jetzt erst einmal alle Spalten von deiner Liste übernommen,
# aber benötigt man da nochmal die Diagnose, Side Dominance oder DBS/IPG? Und was genau ist mit "Complete" gemeint? Das alle Angaben vorhanden sind?

# Ich habe leider hier das gleiche Problem wie auch mit YAML, dass ich das Package "GUI." ... nicht
# installieren kann, daher konnte ich den Code leider nicht ausprobieren und war mir dementsprechend bei Todo 2 und 3 sehr unsicher.
# Fehlermeldung:
# ERROR: Could not find a version that satisfies the requirement GUI (from versions: none)
# ERROR: No matching distribution found for GUI
# auch .helper_functions ist die ganze Zeit rot unterstrichen, obwohl ich das Package korrekt geladen habe.


# TODO: 1. GUIcheckPID erweitern, sodass alle Daten von df drin vorkommen,
# TODO: 2. weitere Verknüfungen erstellen.
# TODO: 3. Eine Funktion erstellen, die alle csv Dateien aus dem Ordner ./temp löscht beim schließen von GUIstart


class CheckForGeneralData(QDialog):
    """Very first GUI only providing a means to enter a PID (according to the ORBIS system at the
    Department of Neurology at the University Hospital of Gießen and Marburg. Several options are possible
    after entering a PID: 1. if existent -> GuiMain, 2. if inexistent enter data in general table"""

    def __init__(self, parent=None):
        """Initialize."""

        super().__init__(parent)
        self.setWindowTitle('Check for existence of subject in database')
        self.setGeometry(400, 100, 500, 300)  # left, right, width, height
        self.move(850, 425)

        self.layout = QVBoxLayout(self)  # entire layout for GUI
        self.content_box = QVBoxLayout(self)  # content of the box

        # ====================    Create Content for First Option box on Top left      ====================
        self.optionbox_guistart = QGroupBox('Please enter general data')
        self.settings_optionsbox1 = QVBoxLayout(self.optionbox_guistart)

        self.subj_surname = QLabel('Surname:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay1 = QHBoxLayout()
        lay1.addWidget(self.subj_surname)
        lay1.addWidget(self.lineEditFilename)
        lay1.addStretch()

        self.subj_name = QLabel('Name:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay2 = QHBoxLayout()
        lay2.addWidget(self.subj_name)
        lay2.addWidget(self.lineEditFilename)
        lay2.addStretch()

        self.subj_birthdate = QLabel('Birthdate:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay3 = QHBoxLayout()
        lay3.addWidget(self.subj_birthdate)
        lay3.addWidget(self.lineEditFilename)
        lay3.addStretch()

        self.subj_PID = QLabel('PID-ORBIS:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay4 = QHBoxLayout()
        lay4.addWidget(self.subj_PID)
        lay4.addWidget(self.lineEditFilename)
        lay4.addStretch()

        self.subj_ID = QLabel('ID:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay5 = QHBoxLayout()
        lay5.addWidget(self.subj_ID)
        lay5.addWidget(self.lineEditFilename)
        lay5.addStretch()

        self.subj_gender = QLabel('Gender:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay6 = QHBoxLayout()
        lay6.addWidget(self.subj_gender)
        lay6.addWidget(self.lineEditFilename)
        lay6.addStretch()

        self.subj_diagnosis = QLabel('Diagnosis:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay7 = QHBoxLayout()
        lay7.addWidget(self.subj_diagnosis)
        lay7.addWidget(self.lineEditFilename)
        lay7.addStretch()

        self.subj_side = QLabel('Side Dominance:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay8 = QHBoxLayout()
        lay8.addWidget(self.subj_side)
        lay8.addWidget(self.lineEditFilename)
        lay8.addStretch()

        self.subj_complete = QLabel('Complete:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay9 = QHBoxLayout()
        lay9.addWidget(self.subj_complete)
        lay9.addWidget(self.lineEditFilename)
        lay9.addStretch()

        self.subj_IPG = QLabel('IPG:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay10 = QHBoxLayout()
        lay10.addWidget(self.subj_IPG)
        lay10.addWidget(self.lineEditFilename)
        lay10.addStretch()

        self.subj_DBS = QLabel('DBS:\t\t')
        self.lineEditFilename = QLineEdit()

        self.lineEditFilename.setFixedWidth(150)
        self.lineEditFilename.setFixedHeight(50)

        lay11 = QHBoxLayout()
        lay11.addWidget(self.subj_DBS)
        lay11.addWidget(self.lineEditFilename)
        lay11.addStretch()

        self.settings_optionsbox1.addLayout(lay1)
        self.settings_optionsbox1.addLayout(lay2)
        self.settings_optionsbox1.addLayout(lay3)
        self.settings_optionsbox1.addLayout(lay4)
        self.settings_optionsbox1.addLayout(lay5)
        self.settings_optionsbox1.addLayout(lay6)
        self.settings_optionsbox1.addLayout(lay7)
        self.settings_optionsbox1.addLayout(lay8)
        self.settings_optionsbox1.addLayout(lay9)
        self.settings_optionsbox1.addLayout(lay10)
        self.settings_optionsbox1.addLayout(lay11)
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
        """when button is pressed, a series of checks are performed in order to retrieve data/to set the following GUI"""

        if not self.lineEditFilename.text():
            Output.msg_box(text='Missing input for the PID, please enter a number', title='Missing input')
            return

        filename = 'general_data.csv'
        df = General.import_dataframe(filename)
        PID2lookfor = self.lineEditFilename.text().lstrip('0') # string that is searched for in metadata file
        idx_PID = df.index[df['PID_ORBIS'] == int(PID2lookfor)].to_list()

        if not idx_PID:
            Output.msg_box(text='No corresponding subject found, please create new entry', title='Missing PID')
        elif len(idx_PID)>1:
            Output.msg_box(text='Too many entries, please double check file: {}'.format(filename),
                           title='Too many PID entries')
            return
        else:
            General.write_csv_temp(df, idx_PID) # writes data to temporary file, so that it may be used later
            self.checkPID = CheckPID()
            self.checkPID.show()

        # TODO 2: Ich glaube das ist nicht richtg, aber ich habe auch nicht ganz verstanden warum es self.checkPID heißt. Die Klasse hieß vor meiner Umbenennung "CheckforPID". Müsste es dann nicht
        # self.checkPID = CheckforPID sein? Bei diesem Teil des Codes war ich mir wirklich sehr unsicher.

        if idx_PID:
            self.GUI_Preoperative = GUI_Preoperative()
            self.GUI_Preoperative.show()
            self.GUI_Postoperative = GUI_Postoperative()
            self.GUI_Postoperative.show()

    # TODO 3: Heute waren die Todo's wirklich schwer. An sich weiß ich, dass ich theoretisch nur den richtigen Pfad angeben muss, aber dann ist das nicht universell auf jedem Rechner zu finden.
    # An sich weiß ich wie es aussehen muss, aber es fällt mir sehr schwer das Ganze in die Tat umzusetzen. Online finde ich leider nur bedingt etwas dazu.

    def close(self):
        dir = '/temp'
        for f in os.listdir(dir):
            os.remove(os.path.join(dir, f))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QWidget
    dlg = CheckForGeneralData()
    dlg.show()
    sys.exit(app.exec_())
