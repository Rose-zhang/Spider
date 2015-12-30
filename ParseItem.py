# encoding: UTF-8
import re
import hashlib
import os
import uuid
import logging

import requests
from bs4 import BeautifulSoup

import threading

from errcode import *
from constants import *

import codecs
import csv

__author__ = 'Jason-Zhang'

protocol = 'https:'

logger = logging.getLogger("crawler")

mutex = threading.Lock()


# Acknowledge
# http://ar.newsmth.net/thread-b99daa8fc0a336.html
def parse_js(expr):
	import ast
	m = ast.parse(expr)
	a = m.body[0]

	def parse(node):
		if isinstance(node, ast.Expr):
			return parse(node.value)
		elif isinstance(node, ast.Num):
			return node.n
		elif isinstance(node, ast.Str):
			return node.s
		elif isinstance(node, ast.Name):
			return node.id
		elif isinstance(node, ast.Dict):
			return dict(zip(map(parse, node.keys), map(parse, node.values)))
		elif isinstance(node, ast.List):
			return map(parse, node.elts)
		else:
			raise NotImplementedError(node.__class__)

	return parse(a)


class Item:
	def __init__(self, url):
		self.url = url

	def parse_and_save(self, path, file_path):
		# s = requests.session()
		r = requests.get(self.url)
		soup = BeautifulSoup(r.text, "html.parser")
		# pattern = re.compile(r'".*"')

		title = self.__get_item_title(soup)
		cid = self.__get_item_cid(soup)
		price = self.__get_item_price(soup)
		inputValues = self.__get_item_inputValues(soup)
		subtitle = self.__get_item_subtitle(soup)
		picture = self.__get_item_picture(soup)
		description = self.__get_item_description(soup, path + '\\' + str(uuid.uuid1()))

		# 下载主图
		picture = self.__download_acution_pictures(picture, path)
		# print picture
		picture_union = ''
		i = 0
		for p in picture:
			append = p + ':1:' + str(i) + ':|;'
			picture_union += append
		item_info = [
			title,
			cid,
			price,
			str(self.__get_item_number()),
			description,
			picture_union,
			self.__get_item_inputPids(),
			inputValues,
			subtitle
		]

		mutex.acquire()
		self.__write_info_csv(item_info, file_path)
		mutex.release()

	@staticmethod
	def __write_info_csv(item_info, file_path):
		# write main info
		f = None
		try:
			f = open(file_path, 'ab+')
			csv_writer = csv.writer(f)
			csv_writer.writerow(item_info)
		finally:
			f.close()

	def __get_item_description(self, soup, path):
		pattern = re.compile(r'//dsc\.taobaocdn\.com.*?,')
		scripts = soup.find_all("script")
		for script in scripts:
			if len(script.contents) == 0:
				continue
			match = pattern.findall(script.contents[0])
			if len(match) != 1:
				continue
			description_url = match[0].split(":")[0][:-2]
			# description_url = description_url.replace('"', '')
			# description_url = description_url.replace(' ', '')

			protocol = 'http:'
			description = requests.get(protocol + description_url)
			description = description.text
			pattern = re.compile(r'<.*>')
			match = pattern.findall(description)
			s = BeautifulSoup(match[0], 'html.parser')
			img_list = s.find_all('img')

			# 创建描述图片存放目录
			if not os.path.exists(path):
				os.makedirs(path)
			if len(img_list) != 0:
				self.__download_and_replace(img_list, path)
			return str(s.encode('utf-8').replace('\n', ''))
		raise Exception(ERROR_DESCRIPTION_URL)

	@staticmethod
	def __download_and_replace(img_list, path):
		i = 1
		for img in img_list:
			if img.get('src') is None:
				continue
			# logger.debug(img)
			pic_url = img['src']
			if pic_url.find('http') == -1:
				pic_url = protocol + pic_url
			pic = requests.get(pic_url)
			pic_content = pic.content
			pic_path = path + '\\' + str(i) + '.jpg'
			f = open(pic_path, 'wb')
			f.write(pic_content)
			f.flush()
			f.close()
			img['src'] = pic_path
			i += 1

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

	# FIXME improve this stupid parsing
	@staticmethod
	def __get_item_picture(soup):
		# pattern = re.compile(r'g_config.*idata.*?;')

		pattern = re.compile(r'auctionImages.*?]')
		scripts = soup.find_all("script")
		for script in scripts:
			if len(script.contents) == 0:
				continue
			match = pattern.findall(script.contents[0].replace('\n', '').replace('\r', ''))
			if len(match) != 1:
				continue
			config_data = match[0]
			pattern = re.compile(r'\[.*\]')
			description = pattern.findall(config_data)[0][1:-1].replace('\"', '').split(',')

			return description
		raise Exception(ERROR_DESCRIPTION_URL)

	@staticmethod
	def __download_acution_pictures(pic_list, path):
		pic_md5_list = []
		protocol = "http:"

		for pic_url in pic_list:
			pic = requests.get(protocol + pic_url)
			pic_content = pic.content
			m = hashlib.md5()
			m.update(pic_content)
			m_hexdigest = m.hexdigest()
			pic_md5_list.append(m_hexdigest)
			f = open(path + '\\' + m_hexdigest + '.tbi', 'wb')
			f.write(pic_content)
			f.flush()
			f.close()
		return pic_md5_list

	@staticmethod
	def __get_item_inputPids():
		return ISBN_KEY

	@staticmethod
	def __get_item_number():
		return 200

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
		return ''

	@staticmethod
	def __get_item_subtitle(soup):
		subtitle = soup.select('[class~=tb-subtitle]')
		# print subtitle
		if len(subtitle) == 0 or len(subtitle[0]) == 0:
			return ''
		# print subtitle[0].contents[0].replace('\n', '')
		return subtitle[0].contents[0].replace('\n', '')


if __name__ == '__main__':
	url = "https://item.taobao.com/item.htm?spm=a1z10.3-c.w4002-11395459624.10.XXQdqt&id=523002034838"
	item = Item(url)
	item.parse_and_save('C:\\Users\\think\\Desktop\\123', 'C:\\Users\\think\\Desktop\\123.csv')
