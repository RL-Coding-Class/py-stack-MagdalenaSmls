"""CLASS STACK"""


class Stack:
    """Provides stack container"""
    def __init__(self, typ=None):
        self.items = []
        self.typ = typ

    def push(self, item):
        if self.typ is not None:
            if isinstance(type, type(self.typ)) == False:
                if isinstance(item , type(self.typ)) == False:
                    raise TypeError
            else:
                if isinstance(item , self.typ) == False:
                    raise TypeError
        self.items.insert(0, item)

    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop(0)

    def get(self):
        if len(self.items) == 0:
            return None
        return self.items[-1]

    def length(self):
        return len(self.items)

    def __str__(self):
        pass

    def __repr__(self):
        pass
