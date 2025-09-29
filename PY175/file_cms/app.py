from bcrypt import checkpw, hashpw, gensalt
from flask import (
    flash,
    Flask,
    redirect,
    request,
    render_template,
    send_from_directory,
    session,
    url_for
    )
from functools import wraps
from markdown import markdown
import os
import yaml

app = Flask(__name__)
app.secret_key = "secret1" # need for using flash

def get_data_path(): # replaces DATA_DIR
    if app.config["TESTING"]:
        return os.path.join(os.path.dirname(__file__), 'tests', 'data')
    else:
        return os.path.join(os.path.dirname(__file__), 'file_cms', 'data')
    
def get_user_credentials():
    file_name = 'users.yaml'
    root_dir = os.path.dirname(__file__)
    if app.config['TESTING']:
        credential_path = os.path.join(root_dir, 'tests', file_name)
    else:
        credential_path = os.path.join(root_dir, 'file_cms', file_name)
    
    with open(credential_path, 'r') as file:
        return yaml.safe_load(file)
    
def is_valid_credential(username, password):
    data = get_user_credentials()

    if username in data: # ensure input username in database
        stored_hash = data[username].encode('utf-8')
        pw_input_bytes = password.encode('utf-8')
        return checkpw(pw_input_bytes, stored_hash) # ensure user pw input == hashed password
    
    return False

def is_signed_in():
    return session.get('username') 

def require_login(func):
    @wraps(func)
    def decorated_func(*args, **kwargs):
        if not is_signed_in():
            flash("You must be signed in to do that.")
            return redirect(url_for('display_signin'))

        return func(*args, **kwargs)
    
    return decorated_func

def get_file_content(file_path):
    with open(file_path, "r") as file:
        file_content = file.read()
    return file_content 

def update_file_content(file_name, new_content):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, file_name)
    with open(file_path, "w") as file:
       file.write(new_content)

@app.route("/")
def index():
    data_dir = get_data_path()
    files = [file for file in os.listdir(data_dir)]
    return render_template("index.html", files=files)

@app.route("/<file_name>")
def display_file_contents(file_name):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, file_name)
    files = [file for file in os.listdir(data_dir)
             if os.path.isfile(os.path.join(data_dir, file)) # ensure only files
            ]
    
    if file_name not in files:
        flash(f"{file_name} does not exist.")
        return redirect(url_for('index'))

    extension = os.path.splitext(file_name)[1] 
    if extension == ".md":
        file_content = get_file_content(file_path)
        return render_template("view_md_files.html", formatted_content=markdown(file_content))
    
    return send_from_directory(data_dir, file_name)

@app.route("/<file_name>/edit")
@require_login
def edit_file(file_name):
    data_dir = get_data_path()
    file_path = os.path.join(data_dir, file_name)
    files = [file for file in os.listdir(data_dir)
             if os.path.isfile(os.path.join(data_dir, file))
            ]
    
    if file_name not in files:
        flash(f"{file_name} does not exist.")
        return redirect(url_for('index'))
    
    file_content = get_file_content(file_path)
    return render_template("edit.html", file_name=file_name, file_content=file_content)

@app.route("/<file_name>", methods=['POST'])
@require_login
def submit_edit(file_name):
    new_content = request.form.get('content') 
    update_file_content(file_name, new_content)
    flash(f"{file_name} has been updated.")
    return redirect(url_for('index'))

@app.route("/new")
@require_login
def display_new_file_page():
    return render_template("new.html")

@app.route("/new", methods=['POST'])
@require_login
def create_new_file():
    file_name = request.form.get('file_name').strip()
    data_dir = get_data_path()
    files = [file for file in os.listdir(data_dir)
             if os.path.isfile(os.path.join(data_dir, file))
            ]

    if file_name in files: # not unique
        flash(f"{file_name} already exists, please try a new name")
        return render_template("new.html"), 422
    
    if not file_name: # empty name
        flash("A name is required")
        return render_template("new.html"), 422
  
    with open(os.path.join(data_dir, file_name), 'w') as file:
        file.write("")
    flash(f'{file_name} was created')
    return redirect(url_for('index'))

@app.route('/<file_name>/delete', methods=['POST'])
@require_login
def delete_file(file_name):
    data_dir = get_data_path()
    files = [file for file in os.listdir(data_dir)
             if os.path.isfile(os.path.join(data_dir, file))
            ]
    if file_name not in files:
        flash(f"{file_name} does not exist")
        return render_template("index.html"), 422
    
    file_path = os.path.join(data_dir, file_name)

    os.remove(file_path) # delete file
    flash(f"{file_name} has been deleted")
    return redirect(url_for("index"))

@app.route("/users/signin")
def display_signin():
    return render_template("signin.html")

@app.route("/users/signin", methods=["POST"])
def signin():
    username = request.form.get("username").strip()
    password = request.form.get("password").strip()
  
    if is_valid_credential(username, password):
            session['username'] = username # only want to store username
            flash(f"Welcome {username}!")
            return redirect(url_for("index"))
    
    flash("Invalid credentials, please try again")
    return render_template("signin.html", username=username), 422


@app.route("/users/signout", methods=["POST"])
def signout():
    session.clear() # clear username and password
    flash("You have been signed out.")
    return redirect(url_for("index")) 

if __name__ == "__main__":
    app.run(debug=True, port=5003)