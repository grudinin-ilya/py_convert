# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(620, 655)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(620, 655))
        MainWindow.setMaximumSize(QtCore.QSize(620, 655))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.SaudiArabia))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 90, 620, 530))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QtCore.QSize(620, 530))
        self.textEdit.setMaximumSize(QtCore.QSize(620, 530))
        self.textEdit.setObjectName("textEdit")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 620, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(620, 40))
        self.frame_2.setMaximumSize(QtCore.QSize(620, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit_page = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_page.setEnabled(True)
        self.lineEdit_page.setGeometry(QtCore.QRect(530, 5, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_page.sizePolicy().hasHeightForWidth())
        self.lineEdit_page.setSizePolicy(sizePolicy)
        self.lineEdit_page.setMinimumSize(QtCore.QSize(80, 30))
        self.lineEdit_page.setMaximumSize(QtCore.QSize(80, 30))
        self.lineEdit_page.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lineEdit_page.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lineEdit_page.setDragEnabled(False)
        self.lineEdit_page.setClearButtonEnabled(False)
        self.lineEdit_page.setObjectName("lineEdit_page")
        self.radioButton_pdf_to_txt = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_pdf_to_txt.setGeometry(QtCore.QRect(380, 10, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_pdf_to_txt.sizePolicy().hasHeightForWidth())
        self.radioButton_pdf_to_txt.setSizePolicy(sizePolicy)
        self.radioButton_pdf_to_txt.setMinimumSize(QtCore.QSize(140, 20))
        self.radioButton_pdf_to_txt.setMaximumSize(QtCore.QSize(140, 20))
        self.radioButton_pdf_to_txt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_pdf_to_txt.setObjectName("radioButton_pdf_to_txt")
        self.buttonGroup = QtWidgets.QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName("buttonGroup")
        self.buttonGroup.addButton(self.radioButton_pdf_to_txt)
        self.radioButton_txt_to_speech = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_txt_to_speech.setGeometry(QtCore.QRect(200, 10, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_txt_to_speech.sizePolicy().hasHeightForWidth())
        self.radioButton_txt_to_speech.setSizePolicy(sizePolicy)
        self.radioButton_txt_to_speech.setMinimumSize(QtCore.QSize(140, 20))
        self.radioButton_txt_to_speech.setMaximumSize(QtCore.QSize(140, 20))
        self.radioButton_txt_to_speech.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_txt_to_speech.setObjectName("radioButton_txt_to_speech")
        self.buttonGroup.addButton(self.radioButton_txt_to_speech)
        self.radioButton_speech_to_txt = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_speech_to_txt.setGeometry(QtCore.QRect(10, 10, 140, 20))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton_speech_to_txt.sizePolicy().hasHeightForWidth())
        self.radioButton_speech_to_txt.setSizePolicy(sizePolicy)
        self.radioButton_speech_to_txt.setMinimumSize(QtCore.QSize(140, 20))
        self.radioButton_speech_to_txt.setMaximumSize(QtCore.QSize(140, 20))
        self.radioButton_speech_to_txt.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.radioButton_speech_to_txt.setObjectName("radioButton_speech_to_txt")
        self.buttonGroup.addButton(self.radioButton_speech_to_txt)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(0, 40, 440, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setMinimumSize(QtCore.QSize(440, 40))
        self.frame_4.setMaximumSize(QtCore.QSize(440, 40))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.toolButton_browse = QtWidgets.QToolButton(self.frame_4)
        self.toolButton_browse.setGeometry(QtCore.QRect(400, 5, 30, 30))
        self.toolButton_browse.setMinimumSize(QtCore.QSize(30, 30))
        self.toolButton_browse.setMaximumSize(QtCore.QSize(30, 30))
        self.toolButton_browse.setObjectName("toolButton_browse")
        self.pushButton_save_doc = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_save_doc.setGeometry(QtCore.QRect(10, 5, 75, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_save_doc.sizePolicy().hasHeightForWidth())
        self.pushButton_save_doc.setSizePolicy(sizePolicy)
        self.pushButton_save_doc.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_save_doc.setMaximumSize(QtCore.QSize(75, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(False)
        font.setWeight(50)
        self.pushButton_save_doc.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("imgs/save-file.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_save_doc.setIcon(icon)
        self.pushButton_save_doc.setIconSize(QtCore.QSize(21, 21))
        self.pushButton_save_doc.setObjectName("pushButton_save_doc")
        self.lineEdit_path = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_path.setGeometry(QtCore.QRect(190, 5, 200, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit_path.sizePolicy().hasHeightForWidth())
        self.lineEdit_path.setSizePolicy(sizePolicy)
        self.lineEdit_path.setMinimumSize(QtCore.QSize(200, 30))
        self.lineEdit_path.setMaximumSize(QtCore.QSize(200, 30))
        self.lineEdit_path.setObjectName("lineEdit_path")
        self.pushButton_convert = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_convert.setGeometry(QtCore.QRect(100, 5, 75, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_convert.sizePolicy().hasHeightForWidth())
        self.pushButton_convert.setSizePolicy(sizePolicy)
        self.pushButton_convert.setMinimumSize(QtCore.QSize(75, 30))
        self.pushButton_convert.setMaximumSize(QtCore.QSize(75, 30))
        self.pushButton_convert.setLayoutDirection(QtCore.Qt.LeftToRight)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("imgs/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_convert.setIcon(icon1)
        self.pushButton_convert.setIconSize(QtCore.QSize(21, 21))
        self.pushButton_convert.setObjectName("pushButton_convert")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(440, 40, 180, 40))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(180, 40))
        self.frame_3.setMaximumSize(QtCore.QSize(180, 40))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_chenge_lang = QtWidgets.QLabel(self.frame_3)
        self.label_chenge_lang.setGeometry(QtCore.QRect(90, 5, 80, 30))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_chenge_lang.sizePolicy().hasHeightForWidth())
        self.label_chenge_lang.setSizePolicy(sizePolicy)
        self.label_chenge_lang.setMinimumSize(QtCore.QSize(80, 30))
        self.label_chenge_lang.setMaximumSize(QtCore.QSize(80, 30))
        self.label_chenge_lang.setObjectName("label_chenge_lang")
        self.comboBox_lang = QtWidgets.QComboBox(self.frame_3)
        self.comboBox_lang.setGeometry(QtCore.QRect(10, 5, 80, 30))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.comboBox_lang.setFont(font)
        self.comboBox_lang.setObjectName("comboBox_lang")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "       MU3EEN"))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Times New Roman\'; font-size:14pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Dubai Light\';\"><br /></p></body></html>"))
        self.lineEdit_page.setStatusTip(_translate("MainWindow", "اكتب رقم الصفحة أو الصفحات"))
        self.lineEdit_page.setPlaceholderText(_translate("MainWindow", "مثلا: 3-5"))
        self.radioButton_pdf_to_txt.setStatusTip(_translate("MainWindow", "تحويل ملف بي دي أف أو صورة إلى نص"))
        self.radioButton_pdf_to_txt.setText(_translate("MainWindow", "pdf/jpg to text"))
        self.radioButton_txt_to_speech.setStatusTip(_translate("MainWindow", "تحويل نص إلى ملف صوتي"))
        self.radioButton_txt_to_speech.setText(_translate("MainWindow", "text to speech"))
        self.radioButton_speech_to_txt.setStatusTip(_translate("MainWindow", "تحويل ملف صوتي إلى نص"))
        self.radioButton_speech_to_txt.setText(_translate("MainWindow", "speech to text"))
        self.toolButton_browse.setStatusTip(_translate("MainWindow", "اختر طريق إلى ملف"))
        self.toolButton_browse.setText(_translate("MainWindow", "..."))
        self.pushButton_save_doc.setStatusTip(_translate("MainWindow", "حفظ "))
        self.pushButton_save_doc.setText(_translate("MainWindow", "حفظ"))
        self.pushButton_convert.setStatusTip(_translate("MainWindow", "تحويل ملف"))
        self.pushButton_convert.setText(_translate("MainWindow", "تحويل"))
        self.label_chenge_lang.setText(_translate("MainWindow", "اختر اللغة"))
        self.comboBox_lang.setStatusTip(_translate("MainWindow", "احتر اللغة"))
