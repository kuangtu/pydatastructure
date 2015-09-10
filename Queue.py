 # -*- coding: utf-8 -*-
__author__ = 'user'

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def EnqueueTest():
    queue = Queue()
    queue.enqueue("a")
    queue.enqueue("b")
    queue.enqueue(123)
    print("the queu len is: %", queue.size())

    a = queue.dequeue()
    print(a)

def hotPotato(namelist, num):
    simplequeue = Queue()
    for name in namelist:
        simplequeue.enqueue(name)

    while simplequeue.size() > 1:
        for i in range(num):
            simplequeue.enqueue(simplequeue.dequeue())

        simplequeue.dequeue()

    return simplequeue.dequeue()

if __name__ == '__main__':
    #EnqueueTest()
    print(hotPotato(["abc", "abd", "abe", "abf", "abg", "abh"], 7))