"""
File: cursor_based_list.py
Description:  Cursor-based list utilizing a header node and a trailer node.
Author:  <PUT YOUR NAME HERE>
"""

# NOTE: Start with getCurrent, isEmpty, __len__, and insertAfter to help
# see if your code is working

from node2way import Node2Way

class CursorBasedList(object):
    """ Linked implementation of a positional list."""
    
    def __init__(self):
        """ Creates an empty cursor-based list with header and trailer nodes.
            The header and trailer nodes help reduce special cases because all"""
        self._header = Node2Way(None)
        self._trailer = Node2Way(None)
        self._trailer.setPrevious(self._header)
        self._header.setNext(self._trailer)
        self._current = None
        self._size = 0

    def hasNext(self):
        """ Returns True if the current item has a next item.
            Precondition:  the list is not empty."""
        if self.isEmpty():
            raise AttributeError("Empty list has no next item")
        return self._current.getNext() != self._trailer

    def hasPrevious(self):
        """ Returns True if the current item has a previous item.
            Precondition:  the list is not empty."""
        pass
    
    def first(self):
        """Moves the cursor to the first item
        if there is one.
        Precondition:  the list is not empty."""
        pass
        
    def last(self):
        """Moves the cursor to the last item
        if there is one.
        Precondition:  the list is not empty."""
        pass

    def next(self):
        """Precondition: hasNext returns True.
        Postcondition: The current item is has moved to the right one item"""
        pass

    def previous(self):
        """Precondition: hasPrevious returns True.
        Postcondition: The current item is has moved to the left one iten"""
        pass

    def insertAfter(self, item):
        """Inserts item after the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        pass

    def insertBefore(self, item):
        """Inserts item before the current item, or
        as the only item if the list is empty.  The new item is the
        current item."""
        pass

    def getCurrent(self):
        """ Returns the current item without removing it or changing the
        current position.
        Precondition:  the list is not empty"""
        pass

    def remove(self):
        """Removes and returns the current item. Making the next item
        the current item if one exists; otherwise the tail item in the
        list is the current item.
        Precondition: the list is not empty."""
        pass

    def replace(self, newItemValue):
        """Replaces the current item by the newItemValue.
        Precondition: the list is not empty."""
        pass

    def isEmpty(self):
        pass

    def __len__(self):
        """ Returns the number of items in the list (excluding the header and
            trailer nodes).
        """
        # replace below
        return 0

    def __str__(self):
        """Includes items from first through last. Remember that the
           header and trailer nodes don't contain actual data.
        """
        resultStr = ""
        temp = self._header.getNext()
        while temp != self._trailer: # stop when temp gets to trailer node
            resultStr += str(temp.getData()) + " "
            temp = temp.getNext()
        # replace below
        return resultStr
