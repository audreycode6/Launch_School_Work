class Todo:
    COMPLETE = "X"
    INCOMPLETE = " "

    def __init__(self, title):
        self._title = title
        self._done = False

    @property
    def title(self):
        return self._title

    @property
    def done(self):
        return self._done

    @done.setter
    def done(self, new_value):
        self._done = new_value

    def __str__(self):
        symbol = Todo.COMPLETE if self.done else Todo.INCOMPLETE
        return f"[{symbol}] {self._title}"

    def __eq__(self, other):
        if not isinstance(other, Todo):
            return NotImplemented
        return  self.title == other.title and self.done == other.done