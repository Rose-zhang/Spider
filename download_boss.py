# -*- coding: utf-8 -*-
import codecs

from PyQt4 import QtCore

from download_worker import DownloadWorker
from constants import *

__author__ = 'Jason-Zhang'


class DownloadBoss(QtCore.QThread):
	signal_job_completed = QtCore.pyqtSignal()

	def __init__(self, widget, queue, path, file_path, thread_num, parent=None):
		super(DownloadBoss, self).__init__(parent)
		self.queue = queue
		self.path = path
		self.file_path = file_path
		self.thread_num = thread_num
		self.widget = widget

	def run(self):
		threads = []
		# csv_file = self.__init_csv_file(self.file_path)
		self.__init_csv_file(self.file_path)
		for i in range(self.thread_num):
			worker = DownloadWorker(self.queue, self.path, self.file_path)
			worker.start()
			worker.signal_increment_bar.connect(self.widget.increase_progressbar)
			threads.append(worker)

		for t in threads:
			t.wait()
		self.signal_job_completed.emit()

	@staticmethod
	def __init_csv_file(path):
		# 创建CSV文件
		f = None
		try:
			f = codecs.open(path, 'w', 'utf-8')
			f.write(version)
			f.write('\n')
			for key in keys_en:
				f.write(key)
				f.write(',')
			f.write('\n')

			for key in keys_cn:
				f.write(key)
				f.write(',')
		finally:
			f.close()
