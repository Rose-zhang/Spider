import re
import requests
from bs4 import BeautifulSoup

__author__ = 'think'


# this module is for dealing with the rootURL and get a bunch of the links to each item
protocol = "http:"


class RootPage:
	def __init__(self, url):
		self.url = url

	def get_items_link(self):
		item_info = []
		s = requests.session()
		r = s.post(self.url)
		soup = BeautifulSoup(r.text, "html.parser")
		line_pool = soup.find_all("div", "item4line1")
		for line in line_pool:
			item_info.append(self.get_items_from_line(line))

	def get_items_from_line(self, line):
		item_info = []
		details = line.find_all("dd", "detail")
		for detail in details:
			item_url = detail.a.attrs['href']
			item_name = detail.a.contents
			print item_url
			print item_name

if __name__ == '__main__':
	page_url = protocol + "//chengxinshudian88.taobao.com/search.htm?orderType=coefp_desc&viewType=grid&keyword=%CA%B5%D1%E9%B0%E0&lowPrice=&highPrice="
	# page_url = "index.html"
	instance = RootPage(page_url)
	instance.get_items_link()
