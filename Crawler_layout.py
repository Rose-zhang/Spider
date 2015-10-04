# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
from MainLayout import Ui_Form
import sys
import logging
import logging.config
from ParsePage import RootPage
from ParseItem import Item
import os
from download_worker import DownloadWorker

__author__ = 'Jason-Zhang'

logging.config.fileConfig("logger.config")
logger = logging.getLogger("crawler")


class Widget(QtGui.QWidget, Ui_Form):
	def __init__(self, parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.setupUi(self)
		self.exit.clicked.connect(self.close_event_for_button)
		self.craw_items.clicked.connect(self.download_link)
		self.download_item.clicked.connect(self.download_items)
		self.progressBar.hide()
		self.file_path = None
		self.item_info = []

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
		url = self.input_url.text()
		print url
		if len(url) == 0:
			message_box = QtGui.QMessageBox.information(self, u'警告', u'请输入链接地址', u'确定')
			return
		root_page = RootPage(url)
		self.item_info = root_page.get_items_link()
		if len(self.item_info) == 0:
			return
		self.display_download.setRowCount(len(self.item_info))
		for i in range(0, len(self.item_info)):
			item_url = QtGui.QTableWidgetItem(self.item_info[i]['item_url'])
			item_name = QtGui.QTableWidgetItem(self.item_info[i]['item_name'])
			self.display_download.setItem(i, 0, item_url)
			self.display_download.setItem(i, 1, item_name)

	def download_items(self):
		file_path = QtGui.QFileDialog.getSaveFileName(
			self,
			u"文件保存",
			"C:/",
			"CSV Files (*.csv)"
		)
		self.progressBar.show()
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(len(self.item_info))
		self.progressBar.setValue(0)
		self.file_path = QtCore.QString(file_path).toUtf8()
		parent_path = os.path.split(self.file_path)[0]
		file_name = os.path.split(self.file_path)[1]

		# 建立图片资源目录，目录名与CSV文件名同名
		pic_directory = file_name.split('.')[0]
		resource_dir = parent_path + '\\' + pic_directory
		if ~os.path.exists(resource_dir):
			os.mkdir(resource_dir)

		if self.file_path is not None:
			worker = DownloadWorker(self.item_info, resource_dir, self.progressBar)
			worker.start()


if __name__ == '__main__':
	app = QtGui.QApplication(sys.argv)
	widget = Widget()
	widget.show()
	sys.exit(app.exec_())
