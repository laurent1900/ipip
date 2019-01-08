#coding:utf-8
import sys
import argparse
import requests
from lxml import etree


reload(sys)
sys.setdefaultencoding('utf-8')


def check(ip):
	try:
		url = 'https://www.ipip.net/ip.html'
		headers = {	'Host': 'www.ipip.net',
					'Connection': 'close',
					'Content-Length': '18',
					'Pragma': 'no-cache',
					'Cache-Control': 'no-cache',
					'Upgrade-Insecure-Requests': '1',
					'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
					'Origin': 'https://www.ipip.net',
					'Content-Type': 'application/x-www-form-urlencoded',
					'DNT': '1',
					'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
					'Referer': 'https://www.ipip.net/ip.html',
					'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7'
					}
		data = {'ip':ip}
		response = requests.post(url, data=data, headers=headers)
		results = ['#####################################################################################################################################']
		html = etree.HTML(response.text)
		html_data = html.xpath('/html/body/div[3]/div/table[1]//td/text()')
		key1 = []
		value1 = []
		for i in html_data:
			if not i.strip()=='':
				key1.append(str(i.strip()))
		html_data = html.xpath('/html/body/div[3]/div/table[1]//a/text()')
		value1.append(str(html_data[0].strip()))
		html_data = html.xpath('/html/body/div[3]/div/table[1]//span/text()')
		for i in html_data:
			if not i.strip()=='' and not i.strip()==')' and not i.strip()=='|':
				value1.append(str(i.strip()))
		del value1[1]
		data1 = zip(key1,value1)
		for i in data1:
			results.append(str(i[0]+':'+i[1]))
		return results
	except Exception,e:
		print e
		return results

def write(results):
	f = open('results.txt','a+')
	for i in results:
		f.write(i.strip()+'\n')
	f.close

def main(ip,file):
	try:
		if ip:
			write(check(ip))
		elif file:
			m = open(file)
			for i in m:
				write(check(i.strip()))
			m.close()
		else:
			print 'usage: ipip.py [-h] [--ip IP] [--file FILE]'
			print 'optional arguments:'
			print '-h, --help   show this help message and exit'
			print '--ip IP      Enter the IP that you want to check'
			print '--file FILE  Input from list of IPs'
	except Exception,e:
		print e
	
if __name__ == '__main__':
	parse = argparse.ArgumentParser()
	parse.add_argument('--ip', help="Enter the IP that you want to check")
	parse.add_argument('--file', help="Input from list of IPs")
	args = parse.parse_args()
	if len(sys.argv) == 1:
		print 'usage: ipip.py [-h] [--ip IP] [--file FILE]'
		print 'optional arguments:'
		print '-h, --help   show this help message and exit'
		print '--ip IP      Enter the IP that you want to check'
		print '--file FILE  Input from list of IPs'
	else:
		ip = args.ip
		file = args.file
		main(ip,file)
