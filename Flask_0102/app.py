from flask import Flask, render_template
import calendar


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('base.html')

@app.route("/<name>")
def word(name):
    daugina = name*5
    return render_template('ivestas.html', name=daugina)

@app.route("/keliamieji")
def keliamieji():
    return render_template("keliamieji.html", calendar=calendar)

if __name__ == "__main__":
    app.run(debug=True)