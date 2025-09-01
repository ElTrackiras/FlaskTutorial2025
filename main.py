from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing_page():
    return render_template("landing.html")

@app.route("/about")
def about_page():
    return render_template("about.html")

@app.route("/home")
def home_page():
    students = (
        ("Joplo", "Female"), 
        ("Landar", "Male"), 
        ("Escultero", "Female")
        )
    return render_template("home.html", std=students)



if __name__ == "__main__":
    app.run(debug=True)

