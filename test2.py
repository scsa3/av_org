import requests
from pathlib import Path
from lxml import etree

r = requests.get('http://www.dmm.co.jp/digital/videoa/-/detail/=/cid=team00100/?i3_ref=search&i3_ord=2')
tree = etree.HTML(r.content)
i = tree.find('.//*[@id="sample-video"]/a')
print(i.get('href'))
