### File: linked_queue.py
from node import Node

class LinkedQueue(object):
    def __init__(self):
        self._front = None
        self._size = 0
        self._rear = None

    def isEmpty(self):
        return self._size == 0

    def enqueue(self, item):
        temp = Node(item)
        if self._size == 0:
            self._front = temp
        else:
            self._rear.next = temp
        self._rear = temp
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise AttributeError('Queue is empty')
        temp = self._front
        self._front = self._front.next
        self._size -= 1
        return temp.getData()

    def peek(self):
        return self._front.data

    def size(self):
        return self._size

    def __str__(self):
        resultStr = ""
        temp = self._front
        while temp != None:
            resultStr += str(temp.getData()) + " "
            temp = temp.getNext()
        resultStr = "(front) " + resultStr + "(rear)"
        return resultStr
    

