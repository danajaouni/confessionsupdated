from flask import Flask, render_template, request,redirect, url_for
from database import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'changeme'

@app.route("/" , methods = ['GET', 'POST'])
def home():
  if request.method == 'GET':
    return render_template("home.html")
  else:
    form = request.form
    message = request.form['message']
    hub = request.form['hub']
    add_Confession(message, hub)
    if request.method == 'POST':
      return redirect(url_for('confessions'))

@app.route("/letter" , methods = ['GET', 'POST'])
def letter():
  if request.method == 'GET':
    return render_template("letter.html")
  else:
    form = request.form
    initials = request.form['initials']
    seclet = request.form['seclet']
    add_Letter(initials, seclet)
    if request.method == 'POST':
      return redirect(url_for('letters'))

@app.route('/confessions')
def confessions():
  return render_template('confessions.html', confessions=session.query(Confession).all())

@app.route('/letters')
def letters():
  return render_template('letters.html', confessions=session.query(Letter).all())


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080, debug=True)
