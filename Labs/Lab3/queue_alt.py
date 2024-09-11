### File: queue_alt.py
class QueueAlt:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        # ADD CODE HERE
        pass

    def dequeue(self):
        # ADD CODE HERE
        pass
    
    def peek(self):
        # ADD CODE HERE
        pass

    def size(self):
        return len(self.items)

    def __str__(self):
        resultStr = "(front)"
        for item in self.items:
            resultStr = resultStr + " " + str(item)
        resultStr = resultStr + " (rear)"
        return resultStr
    
        
