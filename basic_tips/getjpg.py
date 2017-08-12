# coding = utf-8
import re
import urllib


def getHtml(url):
    page = urllib.urlopen(url=url)
    html = page.read()
    return html


def getImage(html):
    reg = r'src="(.+?\.jpg)'
    image = re.compile(reg)
    img_list = re.findall(image, html)
    return img_list


html = getHtml("http://tieba.baidu.com/p/5097796122")

print getImage(html)
