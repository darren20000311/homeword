from stack import Stack


class StringProcessor:
    """Class for processing strings"""
    def process_string(self, input_str):
        stack = Stack()
        output_str = ""
        for char in input_str:
            if char == '*':
                popped = stack.pop()
                # add the popped char into output_str.
                output_str += popped
            elif char == '^':
                popped1 = stack.pop()
                popped2 = stack.pop()
                # add the popped char into output_str.
                output_str += popped1
                # add the popped char into output_str.
                output_str += popped2
            else:
                stack.push(char)
        return output_str
