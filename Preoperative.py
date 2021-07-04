import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QMainWindow, QApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("DBS_Patients_Preoperative.ui", self)
        self.tableWidget.setColumnWidth(0,50)
        self.tableWidget.setColumnWidth(1, 50)
        self.tableWidget.setColumnWidth(2, 270)
        self.loaddata()

    def loaddata(self):
        patients=[{"ID":"","Gender":"1","Diagnosis":"hypokinetic-rigid parkinson-syndrome(PD1)", "First_Diagnosed":"1998", "Admission":"28.08.2016", "Dismissal":"19.09.2016", "Report":"0", "Report_Preop":"", "UPDRS_On":"", "UPDRS_Off":"", "Video":"0", "Video_File":"", "MRI":"1", "fpcit_spect":"0", "NMSQ":"", "MoCa":"", "DemTect":"", "MMST":"", "PDQ8":"", "BDI2":"", "PDQ39":"", "Outpat_Contact":"", "nch":"23.09.2016", "Briefling":"0", "Briefling_Doctor":"", "DBS_Conference":"", "Decision_DBS":"0", "LEDD":"2008,5", "Levodopa/Carbidopa":"375", "Levodopa/Carbidopa CR":"200", "Entacapone":"0", "Tolcapone":"1000", "Pramipexole":"0", "Ropinirole":"16", "Rotigotine":0, "Selegiline, oral":"0", "Selegiline, sublingual":"0", "Rasagiline":"0", "Amantadine":"200", "Apomorphine": "0", "Piribedil":"0", "Safinamid": "0", "Opicapone":"0", "Other": "", "UPDRSII":"", "H&Y":"2", "HRUQ":"", "EQ5D":"", "S&E":"", "icVRCS":"0", "inexVRCS":"0", "Notes":""}]
        row=0
        self.tableWidget.setRowCount(len(patients))
        for patient in patients:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(patient["ID"]))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(patient["Gender"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(patient["Diagnosis"]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(patient["First_Diagnosed"])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(patient["Admission"])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(patient["Dismissal"])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(patient["Report"])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(patient["Report_Preop"])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(patient["UPDRS_On"])))
            self.tableWidget.setItem(row, 9, QtWidgets.QTableWidgetItem(str(patient["UPDRS_Off"])))
            self.tableWidget.setItem(row, 10, QtWidgets.QTableWidgetItem(str(patient["Video"])))
            self.tableWidget.setItem(row, 11, QtWidgets.QTableWidgetItem(str(patient["Video_File"])))
            self.tableWidget.setItem(row, 12, QtWidgets.QTableWidgetItem(str(patient["MRI"])))
            self.tableWidget.setItem(row, 13, QtWidgets.QTableWidgetItem(str(patient["fpcit_spect"])))
            self.tableWidget.setItem(row, 14, QtWidgets.QTableWidgetItem(str(patient["NMSQ"])))
            self.tableWidget.setItem(row, 15, QtWidgets.QTableWidgetItem(str(patient["MoCa"])))
            self.tableWidget.setItem(row, 16, QtWidgets.QTableWidgetItem(str(patient["DemTect"])))
            self.tableWidget.setItem(row, 17, QtWidgets.QTableWidgetItem(str(patient["MMST"])))
            self.tableWidget.setItem(row, 18, QtWidgets.QTableWidgetItem(str(patient["PDQ8"])))
            self.tableWidget.setItem(row, 19, QtWidgets.QTableWidgetItem(str(patient["BDI2"])))
            self.tableWidget.setItem(row, 20, QtWidgets.QTableWidgetItem(str(patient["PDQ39"])))
            self.tableWidget.setItem(row, 21, QtWidgets.QTableWidgetItem(str(patient["Outpat_Contact"])))
            self.tableWidget.setItem(row, 22, QtWidgets.QTableWidgetItem(str(patient["nch"])))
            self.tableWidget.setItem(row, 23, QtWidgets.QTableWidgetItem(str(patient["Briefling"])))
            self.tableWidget.setItem(row, 24, QtWidgets.QTableWidgetItem(str(patient["Briefling_Doctor"])))
            self.tableWidget.setItem(row, 25, QtWidgets.QTableWidgetItem(str(patient["DBS_Conference"])))
            self.tableWidget.setItem(row, 26, QtWidgets.QTableWidgetItem(str(patient["Decision_DBS"])))
            self.tableWidget.setItem(row, 27, QtWidgets.QTableWidgetItem(str(patient["LEDD"])))
            self.tableWidget.setItem(row, 28, QtWidgets.QTableWidgetItem(str(patient["Levodopa/Carbidopa"])))
            self.tableWidget.setItem(row, 29, QtWidgets.QTableWidgetItem(str(patient["Levodopa/Carbidopa CR"])))
            self.tableWidget.setItem(row, 30, QtWidgets.QTableWidgetItem(str(patient["Entacapone"])))
            self.tableWidget.setItem(row, 31, QtWidgets.QTableWidgetItem(str(patient["Tolcapone"])))
            self.tableWidget.setItem(row, 32, QtWidgets.QTableWidgetItem(str(patient["Pramipexole"])))
            self.tableWidget.setItem(row, 33, QtWidgets.QTableWidgetItem(str(patient["Ropinirole"])))
            self.tableWidget.setItem(row, 34, QtWidgets.QTableWidgetItem(str(patient["Rotigotine"])))
            self.tableWidget.setItem(row, 35, QtWidgets.QTableWidgetItem(str(patient["Selegiline, oral"])))
            self.tableWidget.setItem(row, 36, QtWidgets.QTableWidgetItem(str(patient["Selegiline, sublingual"])))
            self.tableWidget.setItem(row, 37, QtWidgets.QTableWidgetItem(str(patient["Rasagiline"])))
            self.tableWidget.setItem(row, 38, QtWidgets.QTableWidgetItem(str(patient["Amantadine"])))
            self.tableWidget.setItem(row, 39, QtWidgets.QTableWidgetItem(str(patient["Apomorphine"])))
            self.tableWidget.setItem(row, 40, QtWidgets.QTableWidgetItem(str(patient["Piribedil"])))
            self.tableWidget.setItem(row, 41, QtWidgets.QTableWidgetItem(str(patient["Safinamid"])))
            self.tableWidget.setItem(row, 42, QtWidgets.QTableWidgetItem(str(patient["Opicapone"])))
            self.tableWidget.setItem(row, 43, QtWidgets.QTableWidgetItem(str(patient["Other"])))
            self.tableWidget.setItem(row, 44, QtWidgets.QTableWidgetItem(str(patient["UPDRSII"])))
            self.tableWidget.setItem(row, 45, QtWidgets.QTableWidgetItem(str(patient["H&Y"])))
            self.tableWidget.setItem(row, 46, QtWidgets.QTableWidgetItem(str(patient["HRUQ"])))
            self.tableWidget.setItem(row, 47, QtWidgets.QTableWidgetItem(str(patient["EQ5D"])))
            self.tableWidget.setItem(row, 48, QtWidgets.QTableWidgetItem(str(patient["S&E"])))
            self.tableWidget.setItem(row, 49, QtWidgets.QTableWidgetItem(str(patient["icVRCS"])))
            self.tableWidget.setItem(row, 50, QtWidgets.QTableWidgetItem(str(patient["inexVRCS"])))
            self.tableWidget.setItem(row, 51, QtWidgets.QTableWidgetItem(str(patient["Notes"])))


            row=row+1

#main
app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedHeight(850)
widget.setFixedWidth(1500)
widget.show()
try:
    sys.exit(app.exec_())
except:
    print("Exiting")