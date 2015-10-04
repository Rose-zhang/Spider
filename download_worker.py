import threading
from ParseItem import Item

__author__ = 'Jason-Zhang'


class DownloadWorker(threading.Thread):
	def __init__(self, item_info, path, progressBar):
		threading.Thread.__init__(self)
		self.item_info = item_info
		self.path = path
		self.progressBar = progressBar

	def run(self):
		i = 0
		for single_item in self.item_info:
			i += 1
			item = Item(single_item['item_url'])
			item.parse_and_save(self.path)
			self.progressBar.setValue(i)
