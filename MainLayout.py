# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainLayout.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
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


class Ui_Form(QtGui.QWidget):
	def setupUi(self):
		self.setObjectName(_fromUtf8("Form"))
		# resize is forbidden for now
		self.setFixedSize(800, 600)
		sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
		sizePolicy.setHorizontalStretch(0)
		sizePolicy.setVerticalStretch(0)
		sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
		self.setSizePolicy(sizePolicy)

		# table
		self.tableView = QtGui.QTableView(self)
		self.tableView.setGeometry(QtCore.QRect(20, 50, 761, 491))
		self.tableView.setObjectName(_fromUtf8("tableView"))

		# button for downloading items
		self.pushButton = QtGui.QPushButton(self)
		self.pushButton.setGeometry(QtCore.QRect(20, 560, 75, 23))
		self.pushButton.setObjectName(_fromUtf8("pushButton"))

		# textArea for imputing url
		self.lineEdit = QtGui.QLineEdit(self)
		self.lineEdit.setGeometry(QtCore.QRect(20, 10, 661, 20))
		self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

		# button for exiting application
		self.pushButton_2 = QtGui.QPushButton(self)
		self.pushButton_2.setGeometry(QtCore.QRect(710, 560, 75, 23))
		self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
		self.pushButton_2.clicked.connect(self.close_event_for_button)

		# button for downloading links
		self.pushButton_3 = QtGui.QPushButton(self)
		self.pushButton_3.setGeometry(QtCore.QRect(710, 10, 75, 23))
		self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

		self.retranslateUi()
		QtCore.QMetaObject.connectSlotsByName(self)

	# close window

	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(
			self, _translate('Form', '系统消息', None),
			_translate('Form', '确定退出?', None), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No
		)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def close_event_for_button(self):
		reply = QtGui.QMessageBox.question(
			self, _translate('Form', '系统消息', None),
			_translate('Form', '确定退出?', None), QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No
		)
		if reply == QtGui.QMessageBox.Yes:
			exit(0)

	def retranslateUi(self):
		self.setWindowTitle(_translate("Form", "宝贝助手", None))
		self.pushButton.setText(_translate("Form", "下载宝贝", None))
		self.pushButton_2.setText(_translate("Form", "退出", None))
		self.pushButton_3.setText(_translate("Form", "抓取链接", None))
		self.lineEdit.setToolTip(_translate("Form", "请在此输入链接", None))


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	ui = Ui_Form()
	ui.setupUi()
	ui.show()
	sys.exit(app.exec_())
