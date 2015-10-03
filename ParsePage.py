# encoding: UTF-8
import re
import requests
from bs4 import BeautifulSoup

__author__ = 'think'


# this module is for dealing with the rootURL and get a bunch of the links to each item
protocol = "https:"


class RootPage:
	def __init__(self, url):
		self.url = url
		self.item_info = []

	# fetch all item from the root page
	def get_items_link(self):
		s = requests.session()
		r = s.post(self.url)
		soup = BeautifulSoup(r.text, "html.parser")

		# locating the item by the key class 'item\dline\d'
		# which means there are several items in a line
		line_pool = soup.find_all("div", re.compile(r'item\dline\d'))
		for line in line_pool:
			self.get_items_from_line(line)
		# print item_info
		return self.item_info

	# items are arranged in line
	def get_items_from_line(self, line):
		details = line.find_all("dd", "detail")
		for detail in details:
			item_url = detail.a.attrs['href']
			item_name = self.generate_item_name(detail.a.contents)
			self.item_info.append(
				{
					'item_url': protocol + item_url,
					'item_name': item_name
				}
			)

	# some key words may be stressed, we need to get pure item name
	def generate_item_name(self, name_list):
		whole_name = ''
		for name in name_list:
			whole_name += name.string
		return whole_name


if __name__ == '__main__':
	page_url = protocol + "//chengxinshudian88.taobao.com/search.htm?orderType=coefp_desc&viewType=grid&keyword=%CA%B5%D1%E9%B0%E0&lowPrice=&highPrice="
	instance = RootPage(page_url)
	instance.get_items_link()
