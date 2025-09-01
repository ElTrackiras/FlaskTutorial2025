from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

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
    students = (
        ("Joplo", "Female", 21), 
        ("Landar", "Male", 22), 
        ("Escultero", "Female", 19)
        )
    return render_template("home.html", std=students)



if __name__ == "__main__":
    app.run(debug=True)

