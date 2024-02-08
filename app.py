from flask import *

from ast import literal_eval

app = Flask(__name__)

app.secret_key = "abc"


@app.route("/", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        with open("creads.txt") as f:
            Lines = f.readlines()
            for line in Lines:
                newline = literal_eval(line)
                if username == newline["username"] and password == newline["password"]:
                    flash(f"Login  Successful! '{username}' Welcome to our website.")
                    return render_template("index.html")

        flash("Wrong UserName And PassWord..")
        return render_template("login.html")

    if request.method == "GET":
        return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "GET":
        return render_template("signup.html")
    elif request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        email = request.form["email"]
        number = request.form["number"]

        new_obj = {
            "username": username,
            "password": password,
            "email": email,
            "number": number,
        }
        # print(str(new_obj))
        file1 = open("creads.txt", "a")  # append mode
        file1.write(str(new_obj) + "\n")
        file1.close()

        file1 = open("creads.txt", "r")  # read mode
        print("CREADS FILE ALL DATA ARE READ..")
        print(file1.read())
        file1.close()

        return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
