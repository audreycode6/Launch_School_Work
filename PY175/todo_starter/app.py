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

from todos.utils import error_for_list_title, error_for_title_length

from werkzeug.exceptions import NotFound

app = Flask(__name__)
app.secret_key = "secret1"

def find_list_by_id(list_id, lists):
    return next((lst for lst in lists if lst['id'] == list_id), None)


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


if __name__ == "__main__":
    app.run(debug=True, port=5003)
