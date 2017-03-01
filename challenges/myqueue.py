
"""MyQueue Package"""


class MyQueue(object):
    """MyQueue"""

    def __init__(self):
        self.first = []
        self.second = []

    def peek(self):
        if self.first:
            return self.first[-1]
        else:
            return self.second[0]

    def pop(self):
        if not self.first:
            while self.second:
                self.first.append(self.second.pop())

        return self.first.pop()

    def put(self, value):
        self.second.append(value)
