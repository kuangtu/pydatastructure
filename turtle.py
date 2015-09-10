 # -*- coding: utf-8 -*-
import turtle
__author__ = 'user'


myTurtle = turtle.Turtle()
myWin = turtle.Screen()


def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

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


if __name__ == "__main__":

    drawSpiral(myTurtle,100)
    myWin.exitonclick()


