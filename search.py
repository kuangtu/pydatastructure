 # -*- coding: utf-8 -*-
__author__ = 'user'


def sequentialSearch(list, item):
    pos = 0
    found = False

    while pos < len(list) and not found:
        if list[pos] == item:
            found = True
        else:
            pos = pos + 1

    return found

def ordsequentialSearch(list, item):
    pos = 0
    found = False
    stop = False

    while pos < len(list) and not found and not stop:
        if list[pos] == item:
            found = True
        else:
            if list[pos] > item:
                stop = True;
            else:
                 pos = pos + 1

    return found

def binarySearch(list, item):
    first = 0
    last = len(list) - 1
    found = False

    while first <= last and not found:
        midpoint = first + (last - first) / 2
        if list[midpoint] == item:
            found = True
        else:
            if item < list[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1

    return found


if __name__ == '__main__':
    list = [1, 5, 3, 9, 11, 80, 1]
    print (sequentialSearch(list, 1))
    orderlist = [1,3,5,6,7,8,9]
    print(ordsequentialSearch(orderlist, 5))

    print(binarySearch(orderlist, 9))

