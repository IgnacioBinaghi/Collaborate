from flask import Flask, render_template, request, redirect, url_for, flash
from ppio.push import *
from ppio.pull import *
from ppio.random_pull import *

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == "POST":
        username = request.form.get("user")
        password = request.form.get("pass")

        print(login(username, password))

        if login(username, password) == True:
            return redirect(url_for('profile'))
        else:
            flash('Your username or password is incorrect')

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
              "Area" : "",
              "courses": "",
              "topics": "",
              "bio": "",
              "user": username,
              "pass": password
        }


        push_to_db(user_template)
        return redirect(url_for('profile'))

    return render_template('sign-up.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    with open("resources/id.txt", "r") as r:
        user_info = get_user(r.readline())


    return render_template('profile.html', bio = user_info["bio"], name = user_info["name"], year = user_info["year"], school = user_info["school"],
        courses = user_info["courses"], topics = user_info["topics"], area = user_info["Area"])


@app.route('/match', methods=['GET', 'POST'])
def match():
    if have_liked_by():
        user_info = get_user(pull_liked_by())
        match = True
    else:
        user_info = get_user(next_rand_user())
        match = False

    with open("resources/last.txt", "w") as w:
        w.write(user_info["_id"] + "\n")
        w.write(str(match))


    return render_template('match.html', bio = user_info["bio"], name = user_info["name"], year = user_info["year"], school = user_info["school"], insta = user_info["socials"],
        courses = user_info["courses"], topics = user_info["topics"], area = user_info["Area"])


@app.route('/match_yes')
def match_yes():
    with open("resources/last.txt", "r") as r:
        last_id = r.readline().strip()
        match = r.readline().strip()
        if match == "True":
            push_match_to(last_id)
            print("match: ", (get_user(last_id)["name"]))
        else:
            push_like_to(last_id)
            print("like: ", (get_user(last_id)["name"]))
    return redirect(url_for('match'))




@app.route('/edit', methods=['GET', 'POST'])
def edit():
    if request.method == "POST":
        bio = request.form.get("bio")
        area = request.form.get("area")
        topics = request.form.get("topics")
        courses = request.form.get("courses")
        insta= request.form.get("insta")

        if courses:
            update_courses(courses)
        if topics:
            update_topics(topics)
        if area:
            update_area(area)
        if bio:
            update_bio(bio)
        if insta:
            update_insta(insta)


        return redirect(url_for('profile'))
    return render_template('edit_account.html')




if __name__ == "__main__":
    app.run(debug=True)