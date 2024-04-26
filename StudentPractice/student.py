from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<words>/")
def api(words):
    defination = words.upper()
    resilt = {'words':words,'defination': defination}
    return resilt

if __name__ == '__main__':
    app.run(debug=True)
