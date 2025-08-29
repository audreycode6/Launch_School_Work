from flask import (
    Flask,
    render_template,
    send_from_directory
    )
import os

app = Flask(__name__)

@app.route("/")
def home():
    root = os.path.abspath(os.path.dirname(__file__))
    data_dir = os.path.join(root, "file_cms", "data")
    files = [
        file for file in os.listdir(data_dir)
        if os.path.isfile(os.path.join(data_dir, file)) # ensure you only list actual files
    ]
    return render_template("home.html", files=files)

@app.route("/<file_name>")
def get_file_contents(file_name):
    root = os.path.abspath(os.path.dirname(__file__))
    data_dir =  os.path.join(root, "file_cms", "data")
    return send_from_directory(data_dir, file_name)

if __name__ == "__main__":
    app.run(debug=True, port=5003)