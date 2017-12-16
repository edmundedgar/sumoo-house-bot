# -*- coding: utf-8 -*-

from urllib2 import urlopen
from lxml import html
from pyquery import PyQuery as pq
import sys
import hashlib
import os

url = 'http://kominka.net/?price_high=&prefcat%5B%5D=65&s='

matchselector = u'#masonry div.panel-body a'
#print matchselector

h = urlopen(url).read()

t = pq(h)
# print tree.xpath('//div[@class="property_unit"]/text()')

track_dir = "/home/ed/housebot"
try:
    os.stat(track_dir)
except:
    os.mkdir(track_dir)       


for i in (t(matchselector).items()):
    lnk = i.attr('href')
    txt = i.text()

    fname = track_dir + '/' + hashlib.md5(lnk).hexdigest()

    if os.path.exists(fname):
        continue

    with open(fname, 'a'):
        os.utime(fname, None)

    print lnk
    print txt
