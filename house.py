# -*- coding: utf-8 -*-

from urllib2 import urlopen
from pyquery import PyQuery as pq
import sys
import hashlib
import os

url = 'http://suumo.jp/jj/bukken/ichiran/JJ012FC001/?ar=030&bs=021&cn=9999999&cnb=0&ekTjCd=&ekTjNm=&hb=0&ht=9999999&kb=1&kt=9999999&ta=09&tb=0&tj=0&tt=9999999&pc=30&po=16&pj=1'

matchstr = u'築年月'
matchselector = u'.property_unit .property_unit-info dt:contains("%s") + dd' % (matchstr)

h = urlopen(url).read()

t = pq(h)

track_dir = "/home/ed/housebot"
try:
    os.stat(track_dir)
except:
    os.mkdir(track_dir)       


for i in (t(matchselector).items()):
    built = i.text()
    yr = int(built[0:4])

    if yr > 1968:
        continue

    par = i.closest('div.property_unit')

    lnk = par.find('h2.property_unit-title a').attr('href')
    fname = track_dir + '/' + hashlib.md5(lnk).hexdigest()

    if os.path.exists(fname):
        continue

    with open(fname, 'a'):
        os.utime(fname, None)

    txt = par.find('h2.property_unit-title a').text()
    print built
    print lnk
    print txt
    print ""
