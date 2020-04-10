from flask import Flask, render_template, request, redirect, url_for
from database import InitDB, QuipsDB
from quip import Quip

app = Flask(__name__)


'''home page'''
@app.route('/', methods=['GET', 'POST'])
def index():
    db = QuipsDB()
    
    #handles new quip entries
    if request.form:
        new_text = request.form.get('quip')
        new_quip = Quip(new_text)
        new_id = db.add_quip(new_quip)
        new_quip.id = new_id
        print('new id', new_quip.id)
        return redirect(url_for('quip_page', id=new_quip.id))

    return render_template('home.html')

'''about page'''
@app.route('/about')
def about():
    return render_template('about.html')

'''main page displaying a quip'''
@app.route('/<id>', methods=['GET', 'POST'])
def quip_page(id):
    db = QuipsDB()
    curr_quip = db.get_quip(id)

    has_child = db.has_child(curr_quip)

    #handles new quip entries
    if request.form:
        new_text = request.form.get('quip')
        new_quip = Quip(new_text, parent=curr_quip.id)
        new_id = db.add_quip(new_quip)
        new_quip.id = new_id
        print('new id', new_quip.id)
        return redirect(url_for('quip_page', id=new_quip.id))
    
    return render_template('quip.html', quip=curr_quip, has_child=has_child)

'''handles redirects to random child'''
@app.route('/getchild/<id>')
def child_redirect(id):
    db = QuipsDB()
    child = db.get_random_child(id)

    return redirect(url_for('quip_page', id=child.id))

if __name__ == "__main__":
    InitDB()
    app.run(debug=True)

    