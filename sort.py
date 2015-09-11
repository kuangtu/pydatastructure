 # -*- coding: utf-8 -*-
__author__ = 'user'

def show():
    print "sort "

def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] < alist[i + 1]:
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)  - 1
    while passnum > 0 and exchanges:
        exchanges = False
        for i in range(passnum):
            if alist[i] < alist[i + 1]:
                exchanges = True
                temp = alist[i]
                alist[i] = alist[i + 1]
                alist[i + 1] = temp

        passnum = passnum - 1


if __name__ == '__main__':
    alist = [1,2,3,4,5,6]
    bubbleSort(alist)
    print alist

    alist = [1,2,3,4,5,6]
    shortBubbleSort(alist)
    print alist