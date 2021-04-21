class my_stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[len(self.items) - 1]
    def is_empty(self):
        return self.items == []
    def size(self):
        return len(self.items)

class Solution:
    def isValid(self, s: str) -> bool:

        stack = my_stack()
        table = {'(': ')', '{': '}', '[': ']'}
        judge = True

        for l in s:
            if l in table:
                stack.push(l)
            else:
                if stack.is_empty():
                    judge = False
                    break
                tmp = stack.pop()
                if table[tmp] == l:
                    continue
                else:
                    judge = False
                    break
        if stack.size() == 0 and judge:
            return True
        else:
            return False