from flask import Flask,render_template
import pandas as pd

app = Flask(__name__)
df = pd.read_csv("dictionary.csv")
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<words>/")
def api(words):
    defination = df.loc[df['word'] == words]['definition'].squeeze()
    result = {'words':words,'defination': defination}
    return result

if __name__ == '__main__':
    app.run(debug=True)
