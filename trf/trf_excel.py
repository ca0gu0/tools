#!/usr/bin/env python
# coding=utf-8

from lib.chinese2pinyin import search
from time import sleep
import win32com.client as win32
import getopt, sys


class Excel(object):
    def __init__(self):
        app = 'Excel'
        xl = win32.gencache.EnsureDispatch('%s.Application' %app)
        ss = xl.Workbooks.Add()
        self.sh = ss.ActiveSheet
        xl.Visible = True

    def write(self, row, column, string):
        sleep(0.1)
        print string, row, column
        try:
            self.sh.Cells(row,column).Value = u'%s' %string
        except UnicodeDecodeError:
            self.sh.Cells(row,column).Value = '%s' %string



    
def Links(url,title,readfile):
    fobj = open(readfile, 'r')
    excel = Excel()
    title = title.split(',')
    for column,string in enumerate(title):
        column += 1
        excel.write(1,column, string)
    
    row = 2
    for eachline in fobj:
        LIST = eachline.split()
        PIN = []
        for ch in LIST:
            #ch = ch.decode('utf-8')
            #ch = ch.encode('gbk')
            result = search(ch)
            PIN.append(result)
        try:
            tp = tuple(PIN)
            link = url %tp
            LIST.append(link)
            print LIST
            
            for column,string in enumerate(LIST):
                column += 1
                excel.write(row,column, string)
        except TypeError,e:
            print e
        row += 1     
    fobj.close()

def usage():
    print u"Usage: python trf_excel.py -u http://www.xxcc.cn/?%s?%s?%s -t 计划,单元,关键词,链接"

def main():
    if len(sys.argv) <2:
        usage()
    try:
        opts, args = getopt.getopt(sys.argv[1:], "hu:t:", ["url=", "title="])
    except getopt.GetoptError as err:
        print str(err)
        usage()
        sys.exit(2)
    for o, a in opts:
        if o in ("-h"):
            usage()
        if o in ("-u", "--url"):
            url = a
        if o in ("-t", "--title"):
            title = a



    #url = "http://www.xxcc.cn/?%s?%s?%s"
    #title = u"计划,单元,关键词,链接"
    
    readfile = 'citiao.txt'
    Links(url,title,readfile)

    
if __name__ == '__main__':
    main()
