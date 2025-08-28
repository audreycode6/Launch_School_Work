from uuid import uuid4
from functools import wraps
from flask import ( 
    flash,
    Flask,
    redirect,
    render_template,
    request,
    session,
    url_for,
    )
from todos.utils import (
    error_for_list_title,
    error_for_title_length,
    find_list_by_id,
    find_todo_by_id,
    is_list_completed,
    is_todo_completed,
    mark_todos_complete,
    sort_items,
    todos_remaining
    )
from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.secret_key = "secret1"

DELETED_MESSAGE = "has been deleted."
CREATED_MESSAGE = "has been created!"

def require_list(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        list_id = kwargs.get('list_id')
        lst = find_list_by_id(list_id, session['lists'])
        if not lst:
            raise NotFound("List not found.")
        return f(lst=lst, *args, **kwargs)
    
    return decorated_function

def require_todo(f):
    @wraps(f)
    @require_list
    def decorated_function(lst, *args, **kwargs):
        todo_id = kwargs.get('todo_id')
        todo = find_todo_by_id(todo_id, lst['todos'])
        if not todo:
            raise NotFound("Todo not found.")
        return f(lst=lst, todo=todo, *args, **kwargs)
    
    return decorated_function

@app.context_processor
def list_utilities_processor():
    return dict(
        is_list_completed=is_list_completed
    )

@app.before_request
def initialize_session():
    if 'lists' not in session:
        session['lists'] = []

@app.route("/")
def index():
    return redirect(url_for("get_lists"))


@app.route("/lists")
def get_lists():
    lists = sort_items(session['lists'], is_list_completed)
    return render_template("lists.html", 
                           lists=lists,
                           todos_remaining=todos_remaining)


@app.route("/lists", methods=["POST"])
def create_list():
    # access to the value the user entered on the form for list_title
    title = request.form['list_title'].strip() 

    error = error_for_list_title(title, session['lists'])
    if error:
        flash(error, "error")
        return render_template("new_list.html", title=title)
    
    session['lists'].append({
        'id' : str(uuid4()), # create UUID for list
        'title': title,
        'todos': []})
        
    flash(f"New todo list {CREATED_MESSAGE}", "success")
    session.modified = True #  ensure Flask is aware of the change                                                                                                                                                            
    return redirect(url_for('get_lists'))


@app.route("/lists/new")
def add_todo_list():
    return render_template("new_list.html")


@app.route('/lists/<list_id>')
@require_list
def show_list(lst, list_id):
    lst['todos'] = sort_items(lst['todos'], is_todo_completed)
    return render_template('list.html', lst=lst)


@app.route('/lists/<list_id>/todos', methods=['POST'])
@require_list
def add_todo(lst, list_id):
    todo_title = request.form['todo'].strip() 

    error = error_for_title_length(todo_title)
    if error:
        flash(error, 'error')
        return render_template('list.html', lst=lst)

    lst['todos'].append({
        'id': str(uuid4()),
        'title': todo_title,
        'completed': False}) 
    
    flash(f'New todo {CREATED_MESSAGE}', 'success')
    session.modified = True
    return redirect(url_for("show_list", list_id=list_id))


@app.route('/lists/<list_id>/todos/<todo_id>/toggle', methods=['POST'])
@require_todo
def update_completion_status(lst, todo, list_id, todo_id): 
    new_status = not todo.get('completed')
    todo['completed'] = new_status
    session.modified = True

    message = 'complete' if new_status else 'incomplete'
    flash(f'Todo marked {message}', 'success')
    return redirect(url_for("show_list", list_id=list_id))


@app.route('/lists/<list_id>/todos/<todo_id>/delete', methods=['POST'])
@require_todo
def delete_todo(lst, todo, list_id, todo_id):
    lst['todos'].remove(todo) # delete todo
    session.modified = True
    flash(f'Todo {DELETED_MESSAGE}', 'success')
    return redirect(url_for('show_list', list_id=list_id))


@app.route("/lists/<list_id>/complete_all", methods=['POST'])
@require_list
def complete_all_todos(lst, list_id):
    mark_todos_complete(lst['todos'])
    session.modified = True
    flash('Todos have been marked complete!', 'success')
    return redirect(url_for('show_list', list_id=list_id))


@app.route("/lists/<list_id>/edit")
@require_list
def edit_list(lst, list_id):
    return render_template("edit_list.html", lst=lst)


@app.route("/lists/<list_id>/delete", methods=['POST'])
@require_list
def delete_list(lst, list_id):
    session['lists'].remove(lst)
    session.modified = True
    flash(f"List {DELETED_MESSAGE}", "success")
    return redirect(url_for("get_lists"))
    

@app.route("/lists/<list_id>", methods=['POST'])
@require_list
def update_list_title(lst, list_id):
    new_title = request.form['list_title'].strip()
    
    error = error_for_list_title(new_title, session['lists'])
    if error:
        flash(error, "error")
        return render_template('edit_list.html', lst=find_list_by_id(list_id, session['lists']), title=new_title)
    
    lst['title'] = new_title
    session.modified = True
    flash("Successfully updated title.", "success")
    return redirect(url_for("show_list", list_id=list_id))

if __name__ == "__main__":
    app.run(debug=True, port=5003)