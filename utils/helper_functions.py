#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rstr
import csv
import os
import pandas as pds
from dependencies import ROOTDIR, FILEDIR
from PyQt5.QtWidgets import QMessageBox, QFileDialog


class General:
    def __init__(self, _debug=False):
        pass

    @staticmethod
    def generate_code(size_array):
        """generates a code consisting of a random combination of letters, numbers and special characters; ';' and ','
        are omitted to avoid confusion in 'csv-files' """
        re_expression = '[a-zA-Z0-9_!#%$§]{}'.format('{%s}' % str(size_array))

        return rstr.xeger(re_expression)

    @staticmethod
    def import_dataframe(filename, separator_csv=';'):
        """returns pandas dataframe from csv ()"""

        filename_total = os.path.join(FILEDIR, filename)
        if not os.path.isfile(filename_total):
            print('\t Filename: {} not found. Please double-check!'.format(filename_total))

        df = pds.read_csv(filename_total, sep=separator_csv)

        return df

    @staticmethod
    def write_csv_temp(df, idx, default_filename='current_subj.csv'):
        """this function is intended to write a file in which the metadata of the subject being processed is saved"""

        header = ['code', 'idx']
        data = [int(df["PID_ORBIS"][idx[0]]), idx[0]]

        with open(os.path.join(ROOTDIR, 'temp', default_filename), 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerow(data)


class Output:
    def __init__(self, _debug=False):
        pass

    @staticmethod
    def msg_box(text='Unknown text', title='unknown title', flag='Information'):
        """helper intended to provide some sort of message box with a text and a title"""
        msgBox = QMessageBox()
        if flag == 'Information':
            msgBox.setIcon(QMessageBox.Information)
        elif flag == 'Warning':
            msgBox.setIcon(QMessageBox.Warning)
        else:
            msgBox.setIcon(QMessageBox.Critical)

        msgBox.setText(text)
        msgBox.setWindowTitle(title)
        msgBox.setStandardButtons(QMessageBox.Ok)
        msgBox.exec()

