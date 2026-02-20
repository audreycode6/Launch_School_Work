from contextlib import contextmanager

import psycopg2
from psycopg2.extras import DictCursor

class DatabasePersistence:
    def __init__(self):
       pass

    @contextmanager
    def _database_connect(self):
        connection = psycopg2.connect(dbname='todos')
        try:
            with connection:
                yield connection
        finally:
            connection.close()

    def all_lists(self):
        query = "SELECT * FROM lists;"
        with self._database_connect() as conn:
            with conn.cursor(cursor_factory=DictCursor) as cursor:
                cursor.execute(query)
                results = cursor.fetchall()
            
        lists = [dict(result) for result in results]
        for lst in lists:
            lst.setdefault('todos', [])
        return lists

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

