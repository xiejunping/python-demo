# -*- coding: UTF-8 -*-

import os
import json

src_dir = './src'
dist_dir = './dist'

def load_json(file_name, file_path):
	# 读取json文件内容,返回字典格式
	with open(file_name, 'r', encoding='utf8') as f:
		json_data = json.load(f)
		json_data = dict(json_data)
		write_info(file_path, json_data)

def write_info(file_name, file_info):
	# 写入文件
	with open(file_name, 'w') as fp:
		json.dump(file_info, fp, indent=4, sort_keys=True)

def main():
	# 判断文件夹是否存在
	if not os.path.exists(dist_dir):
		os.makedirs(dist_dir)

	# 需要格式化数据
	pages = os.listdir(src_dir)
	for page_name in pages:
		# 源路径
		src_path = os.path.join(src_dir, page_name)
		# 写入路径
		file_path = os.path.join(dist_dir, page_name)
		load_json(src_path, file_path)# 源路径
		print("format JSON Sort => {}".format(file_path))

	print("format complete !")

if __name__ == "__main__":
	main()