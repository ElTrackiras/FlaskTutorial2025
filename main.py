from flask import Flask, render_template, request, url_for, redirect
import pymysql

app = Flask(__name__)

connection = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "flaskpassword123",
    database = "ui_aims_db",
    cursorclass=pymysql.cursors.DictCursor
    )
cursor = connection.cursor()

@app.route("/")
def landing_page():
    return render_template("landing.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/login_process", methods=["POST"])
def login_process():
    user = request.form.get('user_inp')

    if user == "escultero":
        return redirect(url_for('home_page'))
    else:
        return redirect(url_for('landing_page'))

@app.route("/home")
def home_page():
    sql = "SELECT * FROM students"
    cursor.execute(sql)
    result = cursor.fetchall()
    return render_template("home.html", std=result)



if __name__ == "__main__":
    app.run(debug=True)

