 # -*- coding: utf-8 -*-
__author__ = 'user'

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


def testDeque():
    d = Deque()

    d.addFront(1)
    d.addRear("2")
    print (d.size())

    print(d.removeRear())
    print(d.removeFront())

def palchecker(string):
    charDeque = Deque()
    for c in string:
        charDeque.addRear(c)

    stillEqual = True

    while charDeque.size() > 1 and stillEqual:
        front = charDeque.removeFront()
        rear = charDeque.removeRear()

        if front != rear:
            stillEqual = False

    return stillEqual

if __name__ == '__main__':
    testDeque()
    print(palchecker("radar"))