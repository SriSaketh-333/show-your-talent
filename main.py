from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('page.html')


@app.route('/login')
def shashank():
    return render_template('login.html')


app.run(debug=True)
