from uuid import uuid4

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
    mark_todos_complete
    )

from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.secret_key = "secret1"


@app.before_request
def initialize_session():
    if 'lists' not in session:
        session['lists'] = []


@app.route("/")
def index():
    return redirect(url_for("get_lists"))


@app.route("/lists/new")
def add_todo_list():
    return render_template("new_list.html")


@app.route("/lists")
def get_lists():
    return render_template("lists.html", lists=session["lists"])


@app.route("/lists", methods=["POST"])
def create_list():
    title = request.form['list_title'].strip() # access to the values the user entered on the form

    error = error_for_list_title(title, session['lists'])
    if error:
        flash(error, "error")
        return render_template("new_list.html", title=title)
    
    session['lists'].append({
        'id' : str(uuid4()), # create UUID for list
        'title': title,
        'todos': []})
        
    flash("The list has been created.", "success")
    session.modified = True #  ensure Flask is aware of the change                                                                                                                                                            
    return redirect(url_for('get_lists'))


@app.route('/lists/<list_id>')
def show_list(list_id):
    lst = find_list_by_id(list_id, session['lists'])

    if not lst:
        raise NotFound('List not found.')
    
    return render_template('list.html', lst=lst)

@app.route('/lists/<list_id>/todos', methods=['POST'])
def add_todo(list_id):
    todo_title = request.form['todo'].strip() 

    error = error_for_title_length(todo_title)
    if error:
        flash(error, 'error')
        return render_template('list.html', lst=find_list_by_id(list_id, session['lists']))

    lst = find_list_by_id(list_id, session['lists'])
    if not lst:
        raise NotFound('List not found.')

    lst['todos'].append({
        'id': str(uuid4()),
        'title': todo_title,
        'completed': False}) 
    
    flash('Successfuly added a new todo.', 'success')
    session.modified = True
    return redirect(url_for("show_list", list_id=list_id))

@app.route('/lists/<list_id>/todos/<todo_id>/toggle', methods=['POST'])
def update_completion_status(list_id, todo_id):
    lst = find_list_by_id(list_id, session['lists'])
    if not lst:
        raise NotFound('List not found.')
    
    todo = find_todo_by_id(todo_id, lst['todos'])
    if not todo:
        raise NotFound('Todo not found.')
    
    new_status = not todo.get('completed')
    todo['completed'] = new_status
    session.modified = True

    message = 'complete' if new_status else 'incomplete'
    flash(f'Todo marked {message}', 'success')
    return redirect(url_for("show_list", list_id=list_id))

@app.route('/lists/<list_id>/todos/<todo_id>/delete', methods=['POST'])
def delete_todo(list_id, todo_id):
    lst = find_list_by_id(list_id, session['lists'])
    if not lst: 
        raise NotFound("List not found.")
    
    todo = find_todo_by_id(todo_id, lst['todos'])
    if not todo:
        raise NotFound('Todo not found.')
    
    lst['todos'].remove(todo) # delete todo
    session.modified = True
    flash('Todo has been successfully deleted.', 'success')
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/complete_all", methods=['POST'])
def complete_all_todos(list_id):
    lst = find_list_by_id(list_id, session['lists'])
    if not lst:
        raise NotFound("List not found.")
    
    mark_todos_complete(lst['todos'])
    session.modified = True
    flash('Todos have been marked complete!', 'success')
    return redirect(url_for('show_list', list_id=list_id))

@app.route("/lists/<list_id>/edit")
def edit_list(list_id):
    lst = find_list_by_id(list_id, session['lists'])
    if not lst:
        raise NotFound("List not found.")
    
    return render_template("edit_list.html", lst=lst)

@app.route("/lists/<list_id>/delete", methods=['POST'])
def delete_list(list_id):
    lst = find_list_by_id(list_id, session['lists'])
    if not lst:
        raise NotFound("List not found.")

    session['lists'].remove(lst)
    session.modified = True
    flash(f"List has been deleted.", "success")
    return redirect(url_for("get_lists"))
    
@app.route("/lists/<list_id>", methods=['POST'])
def update_list_title(list_id):
    lst = find_list_by_id(list_id, session['lists'])
    if not lst:
        raise NotFound("List not found.")
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
