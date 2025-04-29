from todo import Todo

class TodoList:
    def __init__(self, title):
        self._title = title
        self._todos = [] # no getter to enforce encapsulation
                        # and prevent direct access from outside the class

    @property
    def title(self):
        return self._title

    def __str__(self):
        string_todos = [str(todo) for todo in self._todos]
        return f'---- {self.title} ----\n' + "\n".join(string_todos)
    
    def __len__(self):
        return len(self._todos)
    
    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only add Todo objects")
        
        self._todos.append(todo)

    def first(self):
        return self._todos[0]

    def last(self):
        return self._todos[-1]
    
    def to_list(self):
        return self._todos.copy()
    
    def todo_at(self, index):
        return self._todos[index]
    
    def mark_done_at(self, index):
        self._todos[index].done = True

    def mark_undone_at(self, index):
        self._todos[index].done = False

    def mark_all_done(self):
        def mark_done(todo):
            todo.done = True

        self.each(mark_done)

    def mark_all_undone(self):
        def mark_undone(todo):
            todo.done = False

        self.each(mark_undone)

    def all_done(self):
        return all(todo.done for todo in self._todos)
    
    def remove_at(self, index):
        self._todos.pop(index)

    def each(self, callback):
        for todo in self._todos:
            callback(todo)

    def select(self, callback):
        new_list = TodoList(self.title) # create new list

        def choose(todo):
            if callback(todo): # perform selection
                new_list.add(todo) 

        self.each(choose)
        return new_list
    
    def find_by_title(self, todo_title):
        found = self.select(lambda todo: todo.title == todo_title)
        return found.todo_at(0)
    
    def done_todos(self):
        return self.select(lambda todo: todo.done)

    def undone_todos(self):
        return self.select(lambda todo: not todo.done)
    
    def mark_done(self, title):
        found = self.find_by_title(title)
        found.done = True
        
