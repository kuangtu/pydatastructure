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

def mergeSort(alist):
    print "splitting", alist
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)


        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1

        print ("merge list", alist)



if __name__ == '__main__':
    alist = [1,2,3,4,5,6]
    bubbleSort(alist)
    print alist

    alist = [1,2,3,4,5,6]
    shortBubbleSort(alist)
    print alist

    alist = [10,34,6,3,9,18]
    mergeSort(alist)
    print alist