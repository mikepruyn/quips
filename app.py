from flask import Flask, render_template, request, redirect, url_for
from database import InitDB, QuipsDB
from quip import Quip

app = Flask(__name__)


'''handles replies and redirects to random quip'''
@app.route('/', methods=['GET', 'POST'])
def index():
    db = QuipsDB()
    rand_quip = db.get_any_quip()

    #handles new quip entries
    if request.form:
        
        new_text = request.form.get('quip')
        new_quip = Quip(new_text)
        db.add_quip(new_quip)

    return redirect(url_for('quip_page', id=rand_quip.id))

@app.route('/<id>')
def quip_page(id):
    db = QuipsDB()

    #display random quip
    curr_quip = db.get_quip(id)

    return render_template('home.html', quip=curr_quip)

@app.route('/getchild/<id>')
def child_redirect(id):
    db = QuipsDB()
    child = db.get_random_child(id)
    return redirect(url_for('quip_page', id=child.id))

if __name__ == "__main__":
    InitDB()
    app.run(debug=True)

    