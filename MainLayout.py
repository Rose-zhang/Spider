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


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        # resize is forbidden for now
        Form.setFixedSize(800, 600)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)

        # table
        self.tableView = QtGui.QTableView(Form)
        self.tableView.setGeometry(QtCore.QRect(20, 50, 761, 491))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        self.tableView.sethorizo(['hello']);

        # button for downloading links
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 560, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))

        # textArea for imputing url
        self.lineEdit = QtGui.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(20, 10, 661, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))

        # button for downloading items
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(710, 560, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        # button for exiting application
        self.pushButton_3 = QtGui.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(710, 10, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "宝贝助手", None))
        self.pushButton.setText(_translate("Form", "下载宝贝", None))
        self.pushButton_2.setText(_translate("Form", "退出", None))
        self.pushButton_3.setText(_translate("Form", "抓取链接", None))

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    form = QtGui.QWidget()
    ui = Ui_Form()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec_())