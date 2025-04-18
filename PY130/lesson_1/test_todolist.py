import unittest
from todolist import Todo, TodoList

class TestTodoList(unittest.TestCase):
    def setUp(self):
        self.todo1 = Todo("Buy milk")
        self.todo2 = Todo("Clean room")
        self.todo3 = Todo("Go to the gym")

        self.todos = TodoList("Today's Todos")
        self.todos.add(self.todo1)
        self.todos.add(self.todo2)
        self.todos.add(self.todo3)

    def test_to_list(self):
        self.assertEqual([self.todo1, self.todo2, self.todo3], self.todos.to_list())
        '''def to_list(self):
        return self._todos.copy()'''

    def test_first(self):
        self.assertEqual(self.todo1, self.todos.first())
        '''
        def first(self):
            return self._todos[0]'''
        
    def test_last(self):
        self.assertEqual(self.todo3, self.todos.last())
        '''def last(self):
                return self._todos[-1]'''

    def test_not_done(self):
        self.assertFalse(self.todos.all_done())
        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True
        self.assertTrue(self.todos.all_done())
    '''  
    This method returns True when all items in the list are done, 
    False otherwise.
    def all_done(self):
        return all(todo.done for todo in self._todos)'''

    def test_add_invalid(self):
        with self.assertRaises(TypeError):
            foo = "Do dishes"
            self.todos.add(foo)
        with self.assertRaises(TypeError):
            bar = 12
            self.todos.add(bar)

        with self.assertRaises(TypeError):
            bux = TodoList("Test")
            self.todos.add(bux)

        # with self.assertRaises(TypeError):
        #     '''AssertionError: TypeError not raised'''
        #     bux = Todo("Test")
        #     self.todos.add(bux)
    ''' 
    def add(self, todo):
        if not isinstance(todo, Todo):
            raise TypeError("Can only add Todo objects")'''

    def test_todo_at(self):
        with self.assertRaises(IndexError):
            self.todos.todo_at(3)
        # if wanting to test correct value is returned can use assertEqual
        self.assertEqual(self.todo1, self.todos.todo_at(0)) 
        # if wanting to just make sure there is a value at index can use assertTrue
        self.assertTrue(self.todos.todo_at(0)) 
        self.assertTrue(self.todos.todo_at(1))
        self.assertTrue(self.todos.todo_at(2))

        ''' 
        def todo_at(self, index):
            return self._todos[index]
        '''

    def test_mark_done_at(self):
        self.assertFalse(self.todo1.done)
        self.todos.mark_done_at(0)
        self.assertTrue(self.todo1.done)

        self.assertFalse(self.todo2.done)
        self.todos.mark_done_at(1)
        self.assertTrue(self.todo2.done)

        self.assertFalse(self.todo3.done)
        self.todos.mark_done_at(2)
        self.assertTrue(self.todo3.done)

        with self.assertRaises(IndexError):
            self.todos.mark_done_at(3)

        '''
        def mark_done_at(self, index):
            self._todos[index].done = True
        '''

    def test_mark_undone_at(self):
        self.todo1.done = True
        self.todo2.done = True
        self.todo3.done = True

        self.todos.mark_undone_at(0)
        self.assertFalse(self.todo1.done)

        self.todos.mark_undone_at(1)
        self.assertFalse(self.todo2.done)

        self.todos.mark_undone_at(2)
        self.assertFalse(self.todo3.done)

        with self.assertRaises(IndexError):
            self.todos.mark_undone_at(6)
        '''
        def mark_undone_at(self, index):
            self._todos[index].done = False
        '''

    def test_mark_all_done(self):
        self.todos.mark_all_done()
        for todo in self.todos._todos:
            self.assertTrue(todo.done)
        '''
        def mark_all_done(self):
            def mark_done(todo):
                todo.done = True

            self.each(mark_done)
        '''

    def test_remove_at(self):
        self.assertEqual(self.todo1, self.todos.todo_at(0)) #check what is first elem
        self.todos.remove_at(0) # removes todo1
        with self.assertRaises(AssertionError):
            self.assertEqual(self.todo1, self.todos.todo_at(0)) # todo1 not longer 1st elem

        self.assertEqual(self.todo2, self.todos.todo_at(0))
        self.todos.remove_at(0) # removes todo2

        self.assertEqual(self.todo3, self.todos.todo_at(0))
        self.todos.remove_at(0) # removies todo3
        with self.assertRaises(IndexError):
            self.todos.remove_at(0) # todos is empty so it would raise an index error


    '''def remove_at(self, index):
        self._todos.pop(index)
    '''
    def test_str(self):
        str_todos = ("---- Today's Todos ----" 
                    "\n[ ] Buy milk"
                    "\n[ ] Clean room"
                    "\n[ ] Go to the gym")
        self.assertEqual(str_todos, str(self.todos))
    
    def test_str_done_todo(self):
        self.todos.mark_done_at(1)
        str_todos = ("---- Today's Todos ----" 
                    "\n[ ] Buy milk"
                    "\n[X] Clean room"
                    "\n[ ] Go to the gym")
        self.assertEqual(str_todos, str(self.todos))

    def test_str_all_done_todos(self):
        self.todos.mark_all_done()
        str_todos = ("---- Today's Todos ----" 
                    "\n[X] Buy milk"
                    "\n[X] Clean room"
                    "\n[X] Go to the gym")
        self.assertEqual(str_todos, str(self.todos))

    def test_each(self):
        result = []
        expected_result = [self.todo1, self.todo2, self.todo3]
        add_to_new_list = lambda todo: result.append(todo)
        self.todos.each(add_to_new_list)
        self.assertEqual(expected_result, result)
        '''
            def each(self, callback):
                for todo in self._todos:
                    callback(todo)
        '''
        
    def test_select_each(self):
        mark_undone = lambda todo: not todo.done
        foo = self.todos.select(mark_undone)
        self.assertEqual(str(foo), str(self.todos))

        '''
        def select(self, callback):
            new_list = TodoList(self.title) # create new list

            def choose(todo):
                if callback(todo): # perform selection
                    new_list.add(todo) 

            self.each(choose)
            return new_list
        '''

if __name__ == "__main__":
    unittest.main()