# ipip
通过爬虫爬取ipip.net的信息并保存成txt文档,支持单个ip和从列表读取

依赖库：
lxml、argparse、requests

参数说明：

--ip 指定ip进行查询

--file 从列表读取ip进行查询

例子：

python ipip.py --ip=1.1.1.1

或

python ipip.py --file=list.txt
