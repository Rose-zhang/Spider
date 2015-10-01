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

		# button for downloading items
		self.download_item = QtGui.QPushButton(Form)
		self.download_item.setGeometry(QtCore.QRect(20, 560, 75, 23))
		self.download_item.setObjectName(_fromUtf8("download_item"))

		# textArea for entering url
		self.input_url = QtGui.QLineEdit(Form)
		self.input_url.setGeometry(QtCore.QRect(20, 10, 661, 20))
		self.input_url.setObjectName(_fromUtf8("input_url"))

		# button for exiting application
		self.exit = QtGui.QPushButton(Form)
		self.exit.setGeometry(QtCore.QRect(710, 560, 75, 23))
		self.exit.setObjectName(_fromUtf8("exit"))

		# button for downloading links
		self.craw_items = QtGui.QPushButton(Form)
		self.craw_items.setGeometry(QtCore.QRect(710, 10, 75, 23))
		self.craw_items.setObjectName(_fromUtf8("craw_items"))

		# progressBar to show the progress of downloading items
		self.progressBar = QtGui.QProgressBar(Form)
		self.progressBar.setGeometry(QtCore.QRect(290, 560, 241, 23))
		self.progressBar.setProperty("value", 24)
		self.progressBar.setObjectName(_fromUtf8("progressBar"))

		# table view to show all items and the progress of downloading
		self.display_download = QtGui.QTableView(Form)
		self.display_download.setGeometry(QtCore.QRect(30, 50, 741, 481))
		self.display_download.setAutoFillBackground(False)
		self.display_download.setSortingEnabled(False)
		self.display_download.setObjectName(_fromUtf8("display_download"))

		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		Form.setWindowTitle(_translate("Form", "宝贝助手", None))
		self.download_item.setText(_translate("Form", "下载宝贝", None))
		self.input_url.setToolTip(_translate("Form", "请在此输入链接", None))
		self.exit.setText(_translate("Form", "退出", None))
		self.craw_items.setText(_translate("Form", "抓取链接", None))
