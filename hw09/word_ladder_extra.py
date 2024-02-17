from queue import Queue
from stack import Stack

class WordLadder2:
    # """A class providing functionality to create word ladders"""
    # # TODO:
    # # Implement whatever functionality is necessary to generate a
    # # stack representing the word ladder based on the parameters
    # # passed to the constructor.
    # def __init__(self, w1, w2, wordlist):
    def __init__(self, w1, w2, wordlist):
        self.w1 = w1
        self.w2 = w2 
        self.wordlist = wordlist

    def make_ladder(self):
        queue = Queue()
        start = Stack()
        start.push(self.w1)
        queue.enqueue(start)
        visited = set()
        visited.add(self.w1)
        while not queue.isEmpty():
            stack = queue.dequeue()
            word = stack.peek()

            if word == self.w2:
                return stack

            for i in range(-1, len(word)):
                if i == -1:
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = char + word
                        if new_word in self.wordlist and new_word not in visited:
                            visited.add(new_word)
                            new_stack = stack.copy()
                            new_stack.push(new_word)
                            queue.enqueue(new_stack)
                elif i < len(word):
                    for char in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + char + word[i+1:]
                        if new_word in self.wordlist and new_word not in visited:
                            visited.add(new_word)
                            new_stack = stack.copy()
                            new_stack.push(new_word)
                            queue.enqueue(new_stack)
                else:
                    new_word = word[:i-1] + word[i:]
                    if new_word in self.wordlist and new_word not in visited:
                        visited.add(new_word)
                        new_stack = stack.copy()
                        new_stack.push(new_word)
                        queue.enqueue(new_stack)
        return None