from flask import Flask, render_template

app= Flask(__name__)

@app.route('/')
def home():
    return render_template("HTML assessment LEVEL TWO.html")

@app.route('/about/')
def about():
    return render_template("basics.html")


if __name__ == "__main__":
    app.run(debug=True)
