# -*- coding: utf-8 -*-
import logging
from ParsePage import RootPage

from PyQt4 import QtCore

__author__ = 'Jason-Zhang'

logger = logging.getLogger("crawler")


class DownloadLink(QtCore.QThread):
	signal_job_completed = QtCore.pyqtSignal(list)

	def __init__(self, url, parent=None):
		super(DownloadLink, self).__init__(parent)
		self.url = url

	def run(self):
		root_page = RootPage(self.url)
		item_info = root_page.get_items_link()
		self.signal_job_completed.emit(item_info)
