import Stack
def mystery(s, values):
    for val in values:
        s.push(val)#line a
    n = 20
    for i in range(4):
        n += s.pop()#line b
    for i in range(2):
        n -= s.pop() #line c
    return n
def main():
    values = [1,3,5,7,9,11,13,15,17,19]
    stack = Stack()
    print(mysery(stack, values)) #line d
main()