 # -*- coding: utf-8 -*-
__author__ = 'user'

class HashTable:

    def __init__(self, slot):
        self.size = slot
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key ,data):
        hashvalue = self.hashfunc(key, len(self.slots))

        #slot empty, put the key and data
        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:   #已存在key，更新data
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data
            else: #没有空的slot，进行rehash
                nextslot = self.rehash(hashvalue, len(self.slots))
                while self.slots[nextslot] != None and  self.slots[nextslot] != key:
                    nextslot = self.rehash(hashvalue, len(self.slots))

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data

    def hashfunc(self, key, size):
        return key % size

    def rehash(self, key , size):
        return (key + 1) % size

    def get(self, key):
        startslot = self.hashfunc(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == startslot:
                    stop = True

        return data

    def getItem(self, key):
        return self.get(key)

    def setItem(self, key, data):
        self.put(key, data)




def hash():
    s = HashTable(3)
    s.put(0,0)
    print s.slots
    print s.data

    s.put(1,1)
    print s.slots
    print s.data

    s.put(2,2)
    print s.slots
    print s.data

if __name__ == '__main__':
    hash()
    print "hash finished"