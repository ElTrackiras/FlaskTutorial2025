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


@app.route("/enroll_student", methods=["POST"])
def enroll_student():
    name = request.form.get('name_inp')
    sex = request.form.get('sex_inp')
    age = request.form.get('age_inp')

    sql = "INSERT INTO students (student_name, student_sex, student_age) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, sex, age))
    connection.commit()

    return redirect(url_for('home_page'))


@app.route("/delete_student", methods=["POST"])
def delete_student():
    btn_pressed = request.form.get("action_btn")

    if btn_pressed == "update_btn":
        print("YOU ARE TRYING TO UPDATE")
    else:
        student_id = request.form.get("student_id_inp")
        sql = "DELETE FROM students WHERE student_id=%s"
        cursor.execute(sql, (student_id, ))
        connection.commit()
        return redirect(url_for("home_page"))

    

if __name__ == "__main__":
    app.run(debug=True)

