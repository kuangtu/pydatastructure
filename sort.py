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



def selectSort1(alist):
    for slot in range(len(alist) - 1, 0, -1):
        posMax = 0
        for pos in range(1,slot + 1):
            if alist[pos] > alist[posMax]:
                posMax = pos

        temp = alist[slot]
        alist[slot] = alist[posMax]
        alist[posMax] = temp

def insertSort(alist):
    for index in range(1, len(alist)):
        currvalue = alist[index]
        position = index

        while position > 0 and alist[position - 1] > currvalue:
            alist[position] = alist[position - 1]
            position = position - 1

        alist[position] = currvalue





if __name__ == '__main__':
    alist = [1,2,3,4,5,6]
    bubbleSort(alist)
    print alist

    alist = [1,2,3,4,5,6]
    shortBubbleSort(alist)
    print alist

    alist = [2,3,4,1,6,7]
    selectSort1(alist)
    print alist

    alist = [10,2,9,3,4,6,5]
    insertSort(alist)

    alist = [10,34,6,3,9,18]
    mergeSort(alist)
    print alist