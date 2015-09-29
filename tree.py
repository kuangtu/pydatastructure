 # -*- coding: utf-8 -*-
__author__ = 'user'


import tushare as tu;
from sqlalchemy import create_engine;
import operator;


class BinaryTree:
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self, newNode):
        if self.leftChild is None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self, newNode):
        if self.rightChild is None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

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


def testBinaryTree():
    t = BinaryTree('a')
    t.insertLeft('b')
    t.insertRight('c')
    print t.getRootVal()
    print (t.getLeftChild().getRootVal())


def BuildParseTree(exp):
    #fplist = exp.split()
    #print fplist
    pStack = Stack()
    eTree = BinaryTree('')
    pStack.push(eTree)
    current = eTree
    for i in exp:
        if i == '(':
            current.insertLeft('')
            pStack.push(current)
            current = current.getLeftChild()
        elif i == ')':
            current = pStack.pop()
        elif i in ['+', '-', '*', '/']:
            current.setRootVal(i)
            current.insertRight('')
            pStack.push(current)
            current = current.getRightChild()
        elif i not in ['+', '-', '*', '/']:
            current.setRootVal(int(i))
            parent = pStack.pop()
            current = parent

        else:
            raise ValueError

    return eTree

def evaluate(parseTree):
    opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}

    leftC = parseTree.getLeftChild()
    rightC = parseTree.getRightChild()

    if leftC and rightC:
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(leftC),evaluate(rightC))
    else:
        return parseTree.getRootVal()

def test():
    df = tu.get_hist_data('000001')
    df.to_sql()

if __name__ == '__main__':
    tree = BuildParseTree(['(', '3', '+', '(', '4', '*', '5' ,')',')'])
    print evaluate(tree)
    test()



