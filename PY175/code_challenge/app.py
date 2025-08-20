from flask import Flask, render_template, redirect, request
import yaml

app = Flask(__name__)


with open("users.yaml", "r") as file:
    users = yaml.safe_load(file)
    '''users is dict: users name as key: and dict value of their info
        user_dict_info {'email': "email_value",
                        'interests': [list_of interests]}'''


def list_all_interests(users):
    list_interests = [interest for name in users.keys()
                      for interest in users[name]["interests"]]

    return list_interests

def list_other_users(users, u_name):
    other_users = [name for name in users.keys() 
                   if name != u_name]
    
    return other_users

@app.route('/')
def index():
    list_interests = list_all_interests(users)

    return render_template("index.html",
                           users=users,
                           list_interests=list_interests
                           )

@app.route("/user/<user_name>")
def user(user_name):
    list_interests = list_all_interests(users)

    if user_name not in users.keys(): #error handling
        return render_template("error.html", users=users, list_interests=list_interests, user_name=user_name)

    email = users[user_name]['email']
    formatted_interests = (", ").join(users[user_name]['interests'])
    other_users = list_other_users(users, user_name)
    return render_template('user.html', 
                           users=users,
                           list_interests=list_interests,
                           user_name=user_name,
                           email=email,
                           formatted_interests=formatted_interests,
                           other_users=other_users
                           )


@app.errorhandler(404)
def page_not_found(_error):
    return redirect("/")

if __name__ == '__main__':
    app.run(debug=True, port=5003)