from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "superSecret"

@app.route('/')
def index():
    if 'name' in session:
        session['name'] = session['name']
    else:
        session['name'] = "Your Name"
    if 'comment' in session:
        session['comment'] = session['comment']
    else:
        session['comment'] = ""
    return render_template("index.html", name=session['name'], comment=session['comment'])

@app.route('/users', methods=['POST'])
def create_user():
    if len(request.form['inputName']) < 1:
        flash("Name cannot be blank!")
        session['name'] = request.form['inputName']
        session['comment'] = request.form['inputComment']
        return redirect('/')
    if len(request.form['inputComment']) > 120:
        flash("Comment cannot exceed 120 characters!")
        session['name'] = request.form['inputName']
        session['comment'] = request.form['inputComment']
        return redirect('/')
    session['name'] = request.form['inputName']
    session['dojo'] = request.form['inputDojo']
    session['language'] = request.form['inputLanguage']
    session['comment'] = request.form['inputComment']
    return render_template("submitted.html", name=session['name'], dojo=session['dojo'], language=session['language'], comment=session['comment'])

@app.route('/go_back')
def go_back():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)