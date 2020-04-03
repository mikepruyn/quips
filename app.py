from flask import Flask, render_template, request
from database import InitDB, QuipsDB
from quip import Quip

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.form:
        db = QuipsDB()
        new_text = request.form.get('quip')
        new_quip = Quip(new_text)
        db.add_quip(new_quip)

    return render_template('home.html')

if __name__ == "__main__":
    InitDB()
    app.run(debug=True)

    