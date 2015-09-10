 # -*- coding: utf-8 -*-
__author__ = 'user'

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push (self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

rStack = Stack()

def toStr(n, base):
    convertStr="0123456789"

    if  n < base:
        return convertStr[n]
    else:
        return toStr(n / base, base)  + convertStr[n % base]


def listsum(number):
    if len(number) == 1:
        return number[0]

    else:
        return number[0] + listsum(number[1:])


def stackToStr(n, base):
    convertStr = "0123456789ABCDEF"

    while n > 0:
        if n < base:
            rStack.push(convertStr[n])
        else:
            rStack.push(convertStr[n % base])

        n = n / base

    res = ""

    while not rStack.isEmpty():
        print "pop"

        res = res + str(rStack.pop())

    return res


if __name__ == '__main__':
    #print(listsum([1,2,3,4]))

    #print(toStr(18,10))

    print(stackToStr(17, 16))

