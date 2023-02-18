from flask import Flask, render_template, request
from ppio.push import push_to_db

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":

       username = request.form.get("user")

       password = request.form.get("pass")


    return render_template('sign-in.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == "POST":
        name = request.form.get("Name")
        username = request.form.get("user")
        password = request.form.get("pass")
        year = request.form.get("year")
        school = request.form.get("school")
        sex = request.form.get("sex")
        insta= request.form.get("insta")
        print("name: ", name)
        print("username: ", username)
        print("password: ", password)
        print("year: ", year)
        print("sex: ", school)
        print("school: ", sex)
        print("insta: ", insta)


        user_template = {
              "_id" : "1",
              "name" : name,
              "year" : year,
              "school" : school,
              "socials" : insta,
              "Area" : [""],
              "courses": "",
              "topics": "",
              "bio": "",
              "user": username,
              "pass": password,
              "likedby": [""]
        }


        push_to_db(user_template)


    return render_template('sign-up.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('profile.html')




if __name__ == "__main__":
    app.run(debug=True)