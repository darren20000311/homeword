class Stack:
    """A stack class implemented with a Python list"""
    def __init__(self):
        # we can use a python list as the underlying
        # representation, but this is an implementational
        # choice. We do not have to use a list, we just need
        # to make sure we have an ordered collection and are
        # able to access the first and the last.
        self.items = []

    def __str__(self):
        return str(self.items)

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        if len(self.items) == 0:
            return True
        else:
            return False