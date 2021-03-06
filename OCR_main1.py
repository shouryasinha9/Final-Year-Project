# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OCR_main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import csv
import difflib
import io
import json
import os
import re
import sys
import time
import datetime
import cv2
import ftfy
import numpy as np
import pytesseract as tesseract
from PIL import Image
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRect, Qt, pyqtSignal, QObject, QCoreApplication, QThread, QSize
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtWidgets import QFileDialog, QWidget, QLabel, QPushButton, QTableWidgetItem, QMessageBox
from idna import unicode

import jsontocsv_convert
import ocr_v3
from pdf2image import convert_from_path
import preprocess_v3, deskew_image
import dateutil.parser as dparser

import remove_noise
from clean_text import CleanText

inp = ""

data1 = {}


class Ui_OCR_Main(object):
    def setupUi(self, OCR_Main):
        OCR_Main.setObjectName("OCR_Main")
        OCR_Main.resize(1089, 753)
        OCR_Main.setTabShape(QtWidgets.QTabWidget.Rounded)
        icon = QIcon()
        icon.addFile(u"imgbin-optical-character-recognition-scanner-android-jJH8Wb6vZywsb2J5yhixA2MKb.jpg", QSize(),
                     QIcon.Normal, QIcon.Off)
        OCR_Main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(OCR_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 660, 91, 31))
        self.pushButton.setObjectName("pushButton")

        self.drop_img = QLabel(self.centralwidget)
        self.drop_img.setGeometry(QtCore.QRect(10, 10, 1061, 521))
        self.drop_img.setStyleSheet("background-color:rgb(255, 255, 255)")
        self.drop_img.setFrameShape(QtWidgets.QFrame.Panel)
        self.drop_img.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.drop_img.setObjectName("drop_img")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 580, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 620, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")

        self.history = QPushButton(self.centralwidget)
        self.history.setGeometry(QtCore.QRect(170, 580, 91, 31))
        self.history.setObjectName("history")

        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(30, 540, 1051, 21))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")

        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(310, 580, 741, 101))
        self.tableWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tableWidget.setAutoFillBackground(False)
        self.tableWidget.setStyleSheet("background-color: rgb(204, 204, 204);")
        self.tableWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAutoScroll(False)
        self.tableWidget.setTextElideMode(QtCore.Qt.ElideNone)
        self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
        self.tableWidget.setRowCount(1)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(47)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setDefaultSectionSize(70)

        # self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        # self.pushButton_2.setGeometry(QtCore.QRect(170, 620, 93, 31))
        # self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(170, 660, 93, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        OCR_Main.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(OCR_Main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1089, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuSettings = QtWidgets.QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        OCR_Main.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(OCR_Main)
        self.statusbar.setObjectName("statusbar")
        OCR_Main.setStatusBar(self.statusbar)
        self.actionQuit = QtWidgets.QAction(OCR_Main)
        self.actionQuit.setObjectName("actionQuit")
        self.menuEdit.addSeparator()
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(OCR_Main)

        self.pushButton_4.clicked.connect(self.reset)
        self.history.clicked.connect(self.open_history)
        # self.pushButton_2.clicked.connect(self.edit_details)
        QtCore.QMetaObject.connectSlotsByName(OCR_Main)

        w = QWidget()
        self.retranslateUi(OCR_Main)
        self.pushButton_3.clicked.connect(self.getImage)
        self.pushButton.clicked.connect(self.extract)
        self.pushButton_5.clicked.connect(self.write_data)
        QtCore.QMetaObject.connectSlotsByName(OCR_Main)

    def extract(self):
        global inp
        if not os.path.isfile(inp):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('No Document/Image Detected')
            msg.setWindowTitle("Error")
            msg.exec_()
            return 0
        for i in range(41):
            # slowing down the loop
            time.sleep(0.05)
            # setting value to progress bar
            self.progressBar.setValue(i)
        # out = inp.replace('.jpeg', 'processed.jpeg')
        '''inp_img = cv2.imread(inp)
        inp_img = deskew_image.deskew(inp_img)
        out = preprocess_v3.big(inp_img, inp)
        #img = Image.open(out)
        #im_final = remove_noise.process_image_for_ocr(out)
        #cv2.imshow("erode", im_final)
        #cv2.waitKey(0)
        text = tesseract.image_to_string(out, lang='eng+hin')'''
        text = ocr_v3.ocr(inp)
        self.cleaning_text(text)
        # print(final_text)
        self.progressBar.setValue(100)

    def cleaning_text(self, text):
        global data1
        # text = (filter(lambda xt: ord(xt) < 128, text))
        # print(text)
        # Initializing data variable
        dtype = None
        name = None
        dob = None
        pan = None
        nameline = []
        # dobline = []
        panline = []
        # text0 = []
        text1 = []
        # text2 = []
        govRE_str = '(GOVERNMENT|OVERNMENT|VERNMENT|DEPARTMENT|EPARTMENT\
                     |PARTMENT|ARTMENT|INDIA|NDIA)$'
        adhRE_str = '(GOVERNMENT|OVERNMENT|VERNMENT)$'

        numRE_str = '(Number|umber|Account|ccount|count|Permanent|\
                     ermanent|manent)$'
        panRE_str = '(INCOME|NCOME|COME|TAX|TA|ICOME|INCOE|??????????????? ???????????????|???????????????|???????????????|?????????|?????? ???????????????|??????)$'

        gndRE_str = '(Male|MALE|FEMALE|Female)$'

        # Searching for PAN
        lines = text.split('\n')
        for lin in lines:
            s = lin.strip()
            s = s.rstrip()
            s = s.lstrip()
            text1.append(s)

        text1 = list(filter(None, text1))

        for wordline in text1:
            xx = wordline.split()
            if [w for w in xx if re.search(panRE_str, w)]:
                dtype = "PAN CARD"
                break

        for wordline in text1:
            xx = wordline.split()
            if [w for w in xx if re.search(gndRE_str, w)]:
                dtype = "ADH CARD"
                break

        lineno = 0
        if 'Enrolment' in ' '.join(text1):
            for wordline in text1:
                xx = wordline.split()
                if [w for w in xx if re.search('Enrolment', w, re.IGNORECASE)]:
                    lineno = text1.index(wordline)
                    break
            text1 = text1[lineno + 1:]


        lineno = 0
        for wordline in text1:
            xx = wordline.split()
            if [w for w in xx if re.search(govRE_str, w, re.IGNORECASE)]:
                lineno = text1.index(wordline)
                break
        text0 = text1[lineno + 1:]

        # -----------Read Database
        with open('namedb.csv', "rt") as f:
            reader = csv.reader(f)
            newlist = list(reader)
        newlist = sum(newlist, [])
        sho_list = ['SHOURYA', 'NEERAJKUMAR', 'SHISHIR', 'MADHAVESH', 'VINAY', 'SHASHANK', 'ABHINANDAN', 'RASHMI']
        # Searching for Name and finding closest name in database
        try:
            for x in text0:
                for y in x.split():
                    if difflib.get_close_matches(y.upper(), sho_list):
                        nameline.append(x)
                        break
        except Exception as ex:
            pass

        try:
            name = nameline[0]
        except Exception as ex:
            pass

        try:
            dobline = [item for item in text0 if item not in nameline]
            dobline = ''.join(dobline)
            dobregex = re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
            d = dobregex.search(dobline)
            dob = d.group()

        except Exception as ex:
            pass

        if dob is None:
            for wordline in text0:
                xx = wordline.split()
                if [w for w in xx if re.search('YoB', w, re.IGNORECASE)]:
                    found_index = wordline.find('YoB')
                    dob = wordline[found_index:]
                    break


        try:
            panline1 = [item for item in text0 if item not in nameline]
            panline = ' '.join(panline1)
            panregex = re.compile(r'[A-Z]{5}[0-9]{4}[A-Z]{1}')
            p = panregex.search(panline)
            if dtype == 'PAN CARD':
                pan = p.group()


            # adhr = [i for i, word in enumerate(panline) if word.endswith('ale')]
            # adregex = ("^[2-9]{1}[0-9]{3}\\" +
            #            "s[0-9]{4}\\s[0-9]{4}\\s$")
            # ad = aadhreegex.search(panline)

            for wordline in panline1:
                xx = wordline.split()
                if [w for w in xx if re.search(gndRE_str, w)]:
                    lineno = panline1.index(wordline)
                    pan = panline1[lineno + 1]
                    break

        except Exception as ex:
            pass

        now = datetime.datetime.now()
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %I:%M %p")

        data1 = {'Type': dtype, 'Name': name, 'Date of Birth': dob, 'Doc_no': pan,
                 'Save Date': dt_string}

        data = tuple(data1.values())
        print(data)

        row = 0
        col = 0
        for item in data:
            cellinfo = QTableWidgetItem(item)
            # cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # make cell not editable
            self.tableWidget.setItem(row, col, cellinfo)
            cellinfo.setTextAlignment(Qt.AlignCenter)
            col += 1

    def write_data(self):
        # Writing data into JSON
        global data1

        try:
            to_unicode = unicode
        except NameError:
            to_unicode = str

        if not bool(data1):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('No Data to save')
            msg.setWindowTitle("Retry")
            msg.exec_()
        else:
            # Read JSON file
            with open('data.json', 'r+', encoding='utf-8') as data_file:
                data_loaded = json.load(data_file)
                data_loaded['details'].append(data1)
                data_file.seek(0)
                json.dump(data_loaded, data_file, indent=4)

            check = jsontocsv_convert.json2csv('data.json')

            if check:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.NoIcon)
                msg.setText("Sucessful")
                msg.setInformativeText('Data Saved')
                msg.setWindowTitle("Sucess")
                msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText('Data Not saved')
                msg.setWindowTitle("Retry")
                msg.exec_()




        # print(data == data_loaded)
        '''
        # Reading data back JSON(give correct path where JSON is stored)
        with open('data.json', 'r', encoding='utf-8') as f:
            ndata = json.load(f)
            ndata = ndata['details'][0]

        print('\t', "|+++++++++++++++++++++++++++++++|")
        print('\t', '|', '\t', ndata['Name'])
        print('\t', "|-------------------------------|")
        print('\t', '|', '\t', ndata['Date of Birth'])
        print('\t', "|-------------------------------|")
        print('\t', '|', '\t', ndata['Doc_no'])
        print('\t', "|+++++++++++++++++++++++++++++++|")'''

    def open_history(self):
        os.system("D:\\Final-Year-Project\\Save_Data_GovtID.xlsx")


    def reset(self):
        #reset uplodded image
        self.drop_img.setText("Upload Document Image Here")
        self.drop_img.setAlignment(Qt.AlignCenter)

        #reset the data
        data_reset = (None,None, None, None, None)
        row = 0
        col = 0
        for item in data_reset:
            cellinfo = QTableWidgetItem(item)
            # cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)  # make cell not editable
            self.tableWidget.setItem(row, col, cellinfo)
            col += 1
        #reset progress bar
        self.progressBar.setValue(0)

    def getImage(self):
        global inp
        fname = QFileDialog.getOpenFileName(None, 'Open file',
                                            'c:\\', "Image files (*.jpg *.gif *.jpeg *.png *.pdf)")
        imagePath = fname[0]
        if imagePath.lower().endswith('.pdf'):
            images = convert_from_path(imagePath)
            pdf2image_path = imagePath.replace('.pdf','.jpeg')
            images[0].save(pdf2image_path, 'JPEG')
            imagePath = pdf2image_path

        inp = imagePath
        pixmap = QPixmap(imagePath).scaled(1061, 521, Qt.KeepAspectRatio,
                                           Qt.SmoothTransformation)
        self.drop_img.setPixmap(QPixmap(pixmap))
        self.drop_img.setAlignment(Qt.AlignCenter)


    def retranslateUi(self, OCR_Main):
        _translate = QtCore.QCoreApplication.translate
        OCR_Main.setWindowTitle(_translate("OCR_Main", "Structured Details Extraction"))
        self.pushButton.setText(_translate("OCR_Main", "Extract"))
        self.drop_img.setText(_translate("OCR_Main",
                                         "                                                                                                              Upload Document Image Here"))
        self.pushButton_3.setText(_translate("OCR_Main", "Upload"))
        self.pushButton_4.setText(_translate("OCR_Main", "Reset"))
        self.history.setText(_translate("OCR_Main", "Database"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("OCR_Main", "Document Type"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("OCR_Main", "Name"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("OCR_Main", "Date of Birth"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("OCR_Main", "Document Number"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("OCR_Main", "Save Date"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        # self.pushButton_2.setText(_translate("OCR_Main", "Edit"))
        self.pushButton_5.setText(_translate("OCR_Main", "Save"))
        self.menuFile.setTitle(_translate("OCR_Main", "File"))
        self.menuEdit.setTitle(_translate("OCR_Main", "Edit"))
        self.menuSettings.setTitle(_translate("OCR_Main", "Settings"))
        self.menuHelp.setTitle(_translate("OCR_Main", "Help"))
        self.actionQuit.setText(_translate("OCR_Main", "Quit"))
