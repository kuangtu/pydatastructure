 # -*- coding: utf-8 -*-
__author__ = 'user'

import urllib2


def UrlPrint():

    response = urllib2.urlopen('http://financecomputing.net')
    html = response.read()
    print html



if __name__ == '__main__':
   UrlPrint()

