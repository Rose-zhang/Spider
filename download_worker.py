import threading
import logging

from PyQt4 import QtCore

from ParseItem import Item

__author__ = 'Jason-Zhang'

mutex = threading.Lock()
logger = logging.getLogger("crawler")


class DownloadWorker(QtCore.QThread):
	signal_increment_bar = QtCore.pyqtSignal(int)

	def __init__(self, queue, path, file_path, parent=None):
		super(DownloadWorker, self).__init__(parent)
		self.queue = queue
		self.path = path
		self.file_path = file_path

	def run(self):
		while True:
			mutex.acquire()
			logger.debug(self.queue.qsize())
			if self.queue.empty():
				mutex.release()
				break
			item = Item(self.queue.get()['item_url'])
			mutex.release()
			try:
				item.parse_and_save(self.path, self.file_path)
			except Exception, e:
				logger.error(e)
			finally:
				self.signal_increment_bar.emit(1)
