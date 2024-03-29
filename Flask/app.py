from flask import Flask,redirect,url_for

# WSGI APP
app = Flask(__name__)


@app.route('/')
def welcome():
    return "I am learning Flask yeah!! hehehhe hohoh"


@app.route('/keshav')

def welcome_keshav():
    return "Keshav is Awesome"


@app.route('/success/<int:score>')

def success(score):

    return "Wohoo! You passed and your score is " + str(score)


@app.route('/fail/<int:score>')

def fail(score):

    return "Sorry You failed and your score is " + str(score)


@app.route('/results/<int:marks>')

def results(marks):
    result = ""
    if marks < 75:
        result = 'fail'
    else:
        result = 'success'
    return redirect(url_for(result,score = marks))




if __name__ == '__main__':
    app.run(debug=True)
