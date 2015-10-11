# -*- coding: utf-8 -*-
import sys

def openTable():
    f = open('lib/gb-pinyin.table', 'r')
    table = f.read()
    f.close()
    return table

def searchPinyin(num, table):
    if(num>0 & num<160):
        return chr(num)

    v=table.split(';')
    for i in xrange(len(v)-1,-1,-1):
        s=v[i].split(',')
        if int(s[1])<=num:
            return s[0]
            break

def search(chinese):
    table = openTable()
    i=0
    string = ''
    while(i<len(chinese)-1):
        p = ord(chinese[i:i+1])
        if(p>160):
            i+=1
            q = ord(chinese[i:i+1])
            p = p*256+q-65536
        i+=1
        string = '%s%s' % (string, searchPinyin(p,table))
    return string




if __name__ == "__main__":
    table = openTable()

    if len(sys.argv) == 2:
        chinese = sys.argv[1]
    else:
        sys.exit("Usage: python "+sys.argv[0]+" chinese")
        
    i=0
    str = ''
    while(i<len(chinese)-1):
        p = ord(chinese[i:i+1])
        if(p>160):
            i+=1
            q = ord(chinese[i:i+1])
            p = p*256+q-65536
        i+=1
        str = '%s%s' % (str, searchPinyin(p,table))
    print str
