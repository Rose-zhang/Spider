import threading
from ParseItem import Item
import logging

__author__ = 'Jason-Zhang'

mutex = threading.Lock()
logger = logging.getLogger("crawler")


class DownloadWorker(threading.Thread):
	def __init__(self, queue, path, progressbar):
		threading.Thread.__init__(self)
		self.queue = queue
		self.path = path
		self.progressBar = progressbar

	def run(self):
		while not self.queue.empty():
			logger.debug(self.queue.qsize())
			logger.debug(self.queue.qsize())
			item = Item(self.queue.get()['item_url'])
			item.parse_and_save(self.path)
			mutex.acquire()
			self.progressBar.setValue(self.progressBar.value() + 1)
			mutex.release()
