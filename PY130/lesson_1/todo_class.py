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
        for todo in self._todos:
            todo.done = True

    def mark_all_undone(self):
        for todo in self._todos:
            todo.done = False

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


empty_todo_list = TodoList('Nothing Doing')

def setup():
    todo1 = Todo('Buy milk')
    todo2 = Todo('Clean room')
    todo3 = Todo('Go to gym')

    todo2.done = True

    todo_list = TodoList("Today's Todos")
    todo_list.add(todo1)
    todo_list.add(todo2)
    todo_list.add(todo3)

    return todo_list

def step_12():
    print('--------------------------------- Step 12')
    todo_list = setup()

    def y_in_title(todo):
        return 'y' in todo.title

    print(todo_list.select(y_in_title))
    # ---- Today's Todos -----
    # [ ] Buy milk
    # [ ] Go to gym

    print(todo_list.select(lambda todo: todo.done))
    # ---- Today's Todos -----
    # [X] Clean room

step_12()
