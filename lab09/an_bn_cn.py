import sys

sys.path.append("..")  # Lets us import from the parent directory
# Either of the following Stack imports will work identically
from stack_python_list import Stack  # nopep8
# from stack_linked_list import Stack  # nopep8


class AnBnCn:
    """Class for evaluating strings of N a's followed by N b's"""
    def __init__(self):
        self.stack_ab = Stack()
        # I divided a, b and c into two groups for comparison.
        # The first stack is a and b.
        # And the second one is b and c.
        self.stack_bc = Stack()

    def accept(self, in_string):
        """Takes a string and returns a boolean
indicating whether the string matches the pattern"""
        expect_a = True
        # Since if b show up earlier than a, the result will be rejected.
        # So I initailize expect_b as False first.
        expect_b = False
        for ch in in_string:
            if ch == "a":
                if expect_a:
                    # push an a onto the stack
                    self.stack_ab.push(ch)
                else:
                    # Unexpected a
                    return False
            elif ch == "b":
                if self.stack_ab.is_empty():
                    # Too many b's. We ran
                    # out of a's on the stack.
                    return False
                else:
                    # Pop an a off of the stack
                    if expect_a:
                        # Once we've seen a b,
                        # we never expect to see
                        # an a again
                        expect_a = False
                    
                    self.stack_ab.pop()
                    # Append b into the second stack, which is self.stack_bc.
                    self.stack_bc.push(ch)
            elif ch == "c":
                # Since we do not expect that a will show up in the second stack.
                # Therefore, if ch == a, it return False immidiately.
                if expect_a:
                    return False
                
                if self.stack_bc.is_empty():
                    # Too many c's. We ran
                    # out of b's on the stack.
                    return False
                else:
                    if expect_b:
                        # Once we've seen a c,
                        # we never expect to see
                        # an b again
                        expect_b = False
                    self.stack_bc.pop()
                
        # After seeing two different stacks, 
        # a and b should have popped from these stack.
        if self.stack_ab.is_empty() and self.stack_bc.is_empty():
            return True
        return False

    def clear(self):
        """Clear the stack at the end of each checker"""
        self.stack_ab = Stack()
        self.stack_bc = Stack()