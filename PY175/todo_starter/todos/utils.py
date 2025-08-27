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

def is_list_completed(lst):
    return len(lst['todos']) > 0 and todos_remaining(lst) == 0

def is_todo_completed(todo):
    return todo['completed']

def mark_todos_complete(todos):
    for todo in todos:
        todo['completed'] = True

def todos_remaining(lst):
    return sum(1 for todo in lst['todos'] if not todo['completed'])

def sort_items(items, select_completed):
    sorted_items = sorted(items, key=lambda item: item['title'].lower())

    incomplete_items = []
    complete_items = []
    for item in sorted_items:
        if select_completed(item):
            complete_items.append(item)
        else:
            incomplete_items.append(item)

    return incomplete_items + complete_items
