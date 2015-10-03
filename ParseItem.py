# encoding: UTF-8
import requests
from bs4 import BeautifulSoup
import re
from errcode import *
from constants import *

__author__ = 'Jason-Zhang'


class Item:
	def __init__(self, url):
		self.url = url

	def parse(self):
		s = requests.session()
		r = s.get(self.url)
		soup = BeautifulSoup(r.text, "html.parser")
		# pattern = re.compile(r'".*"')
		content = soup.find_all("script")[0].contents[0]
		description = self.__get_item_description(content)
		title = self.__get_item_title(soup)
		cid = self.__get_item_cid(soup)
		price = self.__get_item_price(soup)
		inputValues = self.__get_item_inputValues(soup)
		subtitle = self.__get_item_subtitle(soup)
		print subtitle

	@staticmethod
	def __get_item_description(content):
		pattern = re.compile(r'//desc\.alicdn.com.*"')
		match = pattern.findall(content)
		if len(match) != 1:
			raise Exception(ERROR_DESCRIPTION_URL)
		description = match[0].split(":")[0]
		description = description.replace('"', '')
		description = description.replace(' ', '')
		return description

	@staticmethod
	def __get_item_title(soup):
		title = soup.select("[class~=tb-main-title]")
		if len(title) != 1 or not title[0].has_attr('data-title'):
			raise Exception(ERROR_TITLE_LOCATION)
		return title[0].attrs['data-title']

	@staticmethod
	def __get_item_cid(soup):
		J_Pine = soup.select("[class~=tb-pine]")
		if len(J_Pine) != 1:
			raise Exception(ERROR_CID_LOCATION)
		return J_Pine[0].attrs['data-catid']

	@staticmethod
	def __get_item_price(soup):
		J_PromoPriceNum = soup.select("[class~=tb-rmb-num]")
		if len(J_PromoPriceNum) != 1:
			raise Exception(ERROR_PRICE_LOCATION)
		return J_PromoPriceNum[0].contents[0]

	@staticmethod
	def __get_item_picture(soup):
		return

	@staticmethod
	def __get_item_inputPids():
		return ISBN_KEY

	@staticmethod
	def __get_item_inputValues(soup):
		attribute_list = soup.select('[class~=attributes-list]')
		if attribute_list is None:
			return None
		contents = attribute_list[0].contents
		pattern = re.compile(r'ISBN')
		for content in contents:
			if pattern.match(content.string):
				str = content.string
				return str.split(':')[1].replace(' ', '')
		return None

	@staticmethod
	def __get_item_subtitle(soup):
		subtitle = soup.select('[class~=tb-subtitle]')
		if subtitle is None:
			return None
		return subtitle[0].contents[0].replace('\n', '')


if __name__ == '__main__':
	url = "https://item.taobao.com/item.htm?spm=a230r.1.14.150.Ui4Azt&id=43676300251&ns=1&abbucket=8#detail"
	item = Item(url)
	item.parse()
