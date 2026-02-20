from uuid import uuid4

class SessionPersistence:
    def __init__(self, session):
        self.session = session
        if 'lists' not in self.session:
            self.session['lists'] = []

    def all_lists(self):
        return self.session['lists']

    def find_list(self, list_id):
        found = (lst for lst in self.session['lists'] if lst['id'] == list_id)
        return next(found, None)
    
    def create_new_list(self, title):
        lists = self.all_lists()
        lists.append({
            'id': str(uuid4()),
            'title': title,
            'todos': []
        })
        self.session.modified = True

    def update_list_by_id(self, list_id, new_title):
        lst = self.find_list(list_id)
        if lst:
            lst['title'] = new_title
            self.session.modified = True

    def delete_list(self, list_id):
        lists = self.all_lists()
        self.session['lists'] = [lst for lst in lists
                                if lst['id'] != list_id]
        self.session.modified = True

    def create_new_todo(self, list_id, todo_title):
        lst = self.find_list(list_id)
        lst['todos'].append({
            'id': str(uuid4()),
            'title': todo_title,
            'completed': False
        })

        self.session.modified = True

    def delete_todo_from_list(self, list_id, todo_id):
        lst = self.find_list(list_id)
        lst['todos'] = [todo for todo in lst['todos'] 
                        if todo['id'] != todo_id]
        self.session.modified = True

    def update_todo_status(self, list_id, todo_id, new_completed_status):
        lst = self.find_list(list_id)
        todo = next(
                    (td for td in lst['todos']
                     if td['id'] == todo_id)
                     )
        todo['completed'] = new_completed_status

        self.session.modified = True

