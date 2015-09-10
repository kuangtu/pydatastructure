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

def runStack():
    s = Stack()
    s.push(4)
    s.push("test")
    s.push(True)
    print ("the size is:%", s.size())

    while not s.isEmpty():
        print (s.pop())


def parChecker(string):
    s = Stack()
    balance = True
    index = 0
    while index < len(string) and balance:
        symbol = string[index]
        if symbol == '(':
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                s.pop()

        index = index + 1

    if balance and s.isEmpty():
        return True
    else:
        return False


def parCheckerAll(string):
    s = Stack()
    balance = True
    index = 0
    while index < len(string) and balance:
        symbol = string[index]
        if symbol in "({[":
            s.push(symbol)
        else:
            if s.isEmpty():
                balance = False
            else:
                top = s.pop()
                if not match(top, symbol):
                    balance = False
        index = index + 1

    if balance and s.isEmpty():
        return True
    else:
        return False


def match(open, close):
    opens = '([{'
    closes = ')]}'

    return opens.index(open) == closes.index(close)



if __name__ == '__main__':
    #runStack()
    print(parChecker('((()))'))
    print(parChecker('((())'))
    print(parCheckerAll("[{()}]"))
    print(parCheckerAll("[{()}]）"))
