from flask import Flask, render_template, request


app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('page.html')


@app.route('/login', methods=["GET", "POST"])
def shashank():
    if request.method == "POST":
        details = request.form
        name = details['name']
        email = details['email']
        password = details['password']

        return 'success'
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
