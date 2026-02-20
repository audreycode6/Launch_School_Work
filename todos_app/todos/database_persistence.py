from uuid import uuid4

class DatabasePersistence:
    def __init__(self):
       pass

    def all_lists(self):
        pass
    def find_list(self, list_id):
        pass
    
    def create_new_list(self, title):
        pass

    def update_list_by_id(self, list_id, new_title):
        pass

    def delete_list(self, list_id):
        pass

    def create_new_todo(self, list_id, todo_title):
        pass

    def delete_todo_from_list(self, list_id, todo_id):
        pass

    def update_todo_status(self, list_id, todo_id, new_completed_status):
        pass

    def mark_all_todos_completed(self, list_id):
        pass

