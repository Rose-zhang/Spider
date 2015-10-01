# -*- coding: utf-8 -*-
from PyQt4 import QtGui
from MainLayout import Ui_Form
import sys
import logging
import logging.config
from ParsePage import RootPage

__author__ = 'Jason-Zhang'

logging.config.fileConfig("logger.config")
logger = logging.getLogger("crawler")


class Widget(QtGui.QWidget, Ui_Form):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.exit.clicked.connect(self.close_event_for_button)
		self.craw_items.clicked.connect(self.download_link)

	def closeEvent(self, event):
		reply = QtGui.QMessageBox.question(
			self, u'系统消息',
			u'确定退出', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No
		)
		if reply == QtGui.QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()

	def close_event_for_button(self):
		reply = QtGui.QMessageBox.question(
			self, u'系统消息',
			u'确定退出', QtGui.QMessageBox.Yes | QtGui.QMessageBox.No, QtGui.QMessageBox.No
		)
		if reply == QtGui.QMessageBox.Yes:
			exit(0)

	def download_link(self):
		logger.debug(self.input_url.text())


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	widget = Widget()
	widget.show()
	sys.exit(app.exec_())
