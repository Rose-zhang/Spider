# -*- coding: utf-8 -*-
import sys
import logging
import logging.config
import os
import Queue

from PyQt4 import QtGui, QtCore

from MainLayout import Ui_Form

from download_boss import DownloadBoss
from download_item_link import DownloadLink

__author__ = 'Jason-Zhang'

logging.config.fileConfig("logger.config")
logger = logging.getLogger("crawler")


class Widget(QtGui.QMainWindow, Ui_Form):
	# signal_increment_bar = QtCore.pyqtSignal()

	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.exit.clicked.connect(self.close_event_for_button)
		self.craw_items.clicked.connect(self.download_link)
		self.download_item.clicked.connect(self.download_items)
		# self.signal_increment_bar.connect(self.increase_progressbar)
		self.progressBar.hide()
		self.file_path = None
		self.item_info = []
		self.job = None
		self.download_link_job = None

		self.overlay = None

	# logger.debug('haha')

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
			sys.exit(0)

	def download_link(self):
		try:
			url = self.input_url.text()
			# print url
			if len(url) == 0:
				raise Exception(u'请输入链接地址')
			self.download_link_job = DownloadLink(url)
			self.download_link_job.signal_job_completed.connect(self.fulfill_table)
			self.download_link_job.start()

			# self.overlay = Overlay(self.centralWidget())
			# self.overlay.show()

			self.init_progressbar(0)

		except Exception, e:
			QtGui.QMessageBox.information(self, u'警告', e.message, u'确定')

	def fulfill_table(self, item_info):
		self.progressBar.hide()
		self.item_info = item_info
		try:

			if len(self.item_info) == 0:
				raise Exception(u'请输入合法链接地址')

			self.display_download.setRowCount(len(self.item_info))

			for i in range(0, len(self.item_info)):
				item_url = QtGui.QTableWidgetItem(self.item_info[i]['item_url'])
				item_name = QtGui.QTableWidgetItem(self.item_info[i]['item_name'])
				self.display_download.setItem(i, 0, item_url)
				self.display_download.setItem(i, 1, item_name)
			# QtGui.QMessageBox.information(self, u'系统消息', u'链接抓取完成', u'确定')
			self.job_completed_notify(u'系统消息', u'链接抓取完成')

		except Exception, e:
			QtGui.QMessageBox.information(self, u'警告', e.message, u'确定')

	def download_items(self):
		file_path = QtGui.QFileDialog.getSaveFileName(
				self,
				u"文件保存",
				"C:/",
				"CSV Files (*.csv)"
		)

		self.file_path = QtCore.QString(file_path).toUtf8()
		parent_path = os.path.split(self.file_path)[0]
		file_name = os.path.split(self.file_path)[1]
		if len(parent_path) == 0 or len(file_name) == 0:
			return

		self.init_progressbar(len(self.item_info))
		# 建立图片资源目录，目录名与CSV文件名同名
		pic_directory = file_name.split('.')[0]
		resource_dir = parent_path + '\\' + pic_directory
		if not os.path.exists(resource_dir):
			os.mkdir(resource_dir)

		if self.file_path is not None:
			queue = self.generate_queue()
			self.job = DownloadBoss(self, queue, resource_dir, file_path, 4)
			self.job.signal_job_completed.connect(self.job_completed_notify)
			self.job.start()

	def init_progressbar(self, maximum):
		self.progressBar.show()
		self.progressBar.setMinimum(0)
		self.progressBar.setMaximum(maximum)
		self.progressBar.setValue(0)

	def increase_progressbar(self, num):
		self.progressBar.setValue(self.progressBar.value() + num)

	def generate_queue(self):
		queue = Queue.Queue(0)
		for item in self.item_info:
			queue.put(item)
		return queue

	def job_completed_notify(self, message_type, message):
		QtGui.QMessageBox.information(self, message_type, message, u'确定')


if __name__ == '__main__':
	reload(sys)
	sys.setdefaultencoding('utf8')
	app = QtGui.QApplication(sys.argv)
	widget = Widget()
	widget.show()
	sys.exit(app.exec_())
