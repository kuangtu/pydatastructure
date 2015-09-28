 # -*- coding: utf-8 -*-
__author__ = 'user'


def BinaryTree(r):
    return [r, [] ,[]]

def insertLeft(root, Node):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [Node, t, []])
    else:
        root.insert(1, [Node, [], []])

    return root

def insertRight(root, Node):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [Node, [], t])
    else:
        root.insert(2, [Node, [], []])

    return root

def getRoot(root):
    return root[0]

def getLeft(root):
    return root[1]

def getRight(root):
    return root[2]

def test():
    print "test"
    t = BinaryTree(3)
    print len(t)

def buildTree():
    r = BinaryTree(3)
    insertLeft(r, 1)
    insertLeft(r, 2)
    insertLeft(r, 4)

    l = getLeft(r)
    print l


if __name__ == '__main__':
    test()
    buildTree()
