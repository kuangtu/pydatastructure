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


def ConvtBin(number):
    s = Stack()
    if number <= 0:
        print ("number must > 0")
    while( number > 0):
        rem = number % 2
        s.push(rem)
        number = number / 2
    binstring = ""
    while not s.isEmpty():
        binstring = binstring + str(s.pop())
    return binstring

if __name__ == '__main__':
    print(ConvtBin(56))