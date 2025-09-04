from flask import (
    flash,
    Flask,
    redirect,
    request,
    render_template,
    send_from_directory,
    url_for
    )

from markdown import markdown
import os

app = Flask(__name__)
app.secret_key = "secret1" # need for using flash

def get_data_path(): # replaces DATA_DIR
    if app.config["TESTING"]:
        return os.path.join(os.path.dirname(__file__), 'tests', 'data')
    else:
        return os.path.join(os.path.dirname(__file__), 'file_cms', 'data')

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
def submit_edit(file_name):
    new_content = request.form.get('content') 
    update_file_content(file_name, new_content)
    flash(f"{file_name} has been updated.")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True, port=5003)