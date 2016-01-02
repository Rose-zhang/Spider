# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainLayout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.download_item = QtGui.QPushButton(Form)
        self.download_item.setGeometry(QtCore.QRect(20, 560, 75, 23))
        self.download_item.setObjectName(_fromUtf8("download_item"))
        self.input_url = QtGui.QLineEdit(Form)
        self.input_url.setGeometry(QtCore.QRect(20, 10, 661, 20))
        self.input_url.setObjectName(_fromUtf8("input_url"))
        self.exit = QtGui.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(710, 560, 75, 23))
        self.exit.setObjectName(_fromUtf8("exit"))
        self.craw_items = QtGui.QPushButton(Form)
        self.craw_items.setGeometry(QtCore.QRect(710, 10, 75, 23))
        self.craw_items.setObjectName(_fromUtf8("craw_items"))
        self.progressBar = QtGui.QProgressBar(Form)
        self.progressBar.setGeometry(QtCore.QRect(290, 560, 241, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.display_download = QtGui.QTableWidget(Form)
        self.display_download.setGeometry(QtCore.QRect(20, 50, 761, 481))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.display_download.sizePolicy().hasHeightForWidth())
        self.display_download.setSizePolicy(sizePolicy)
        self.display_download.setAutoScroll(True)
        self.display_download.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.display_download.setShowGrid(True)
        self.display_download.setGridStyle(QtCore.Qt.NoPen)
        self.display_download.setObjectName(_fromUtf8("display_download"))
        self.display_download.setColumnCount(2)
        self.display_download.setRowCount(15)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(7, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(8, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(9, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(10, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(11, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(12, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(13, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setVerticalHeaderItem(14, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.display_download.setHorizontalHeaderItem(1, item)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "宝贝助手", None))
        self.download_item.setText(_translate("Form", "下载宝贝", None))
        self.input_url.setToolTip(_translate("Form", "请在此输入链接", None))
        self.exit.setText(_translate("Form", "退出", None))
        self.craw_items.setText(_translate("Form", "抓取链接", None))
        item = self.display_download.verticalHeaderItem(0)
        item.setText(_translate("Form", "1", None))
        item = self.display_download.verticalHeaderItem(1)
        item.setText(_translate("Form", "2", None))
        item = self.display_download.verticalHeaderItem(2)
        item.setText(_translate("Form", "3", None))
        item = self.display_download.verticalHeaderItem(3)
        item.setText(_translate("Form", "4", None))
        item = self.display_download.verticalHeaderItem(4)
        item.setText(_translate("Form", "5", None))
        item = self.display_download.verticalHeaderItem(5)
        item.setText(_translate("Form", "6", None))
        item = self.display_download.verticalHeaderItem(6)
        item.setText(_translate("Form", "7", None))
        item = self.display_download.verticalHeaderItem(7)
        item.setText(_translate("Form", "8", None))
        item = self.display_download.verticalHeaderItem(8)
        item.setText(_translate("Form", "9", None))
        item = self.display_download.verticalHeaderItem(9)
        item.setText(_translate("Form", "10", None))
        item = self.display_download.verticalHeaderItem(10)
        item.setText(_translate("Form", "11", None))
        item = self.display_download.verticalHeaderItem(11)
        item.setText(_translate("Form", "12", None))
        item = self.display_download.verticalHeaderItem(12)
        item.setText(_translate("Form", "13", None))
        item = self.display_download.verticalHeaderItem(13)
        item.setText(_translate("Form", "14", None))
        item = self.display_download.verticalHeaderItem(14)
        item.setText(_translate("Form", "15", None))
        item = self.display_download.horizontalHeaderItem(0)
        item.setText(_translate("Form", "宝贝URL", None))
        item = self.display_download.horizontalHeaderItem(1)
        item.setText(_translate("Form", "宝贝名称", None))

