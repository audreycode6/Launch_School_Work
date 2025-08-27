MAX_TITLE_LEN = 100


def error_for_title_length(title):
    if not 1 <= len(title) <= MAX_TITLE_LEN:
        return "The title must be between 1 and 100 characters."
    return None

def error_for_list_title(title, lists):
    if any(lst['title'] == title for lst in lists):
        return "The title must be unique."
    return error_for_title_length(title)

def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst['id'] == list_id), None)

def find_todo_by_id(todo_id, todos):
    return next((todo for todo in todos if todo['id'] == todo_id), None)

def mark_todos_complete(todos):
    for todo in todos:
        todo['completed'] = True
