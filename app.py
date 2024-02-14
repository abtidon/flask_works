from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting_message = 'Hello, World!'
    return render_template('hello.html', greeting=greeting_message)

if __name__ == '__main__':
    app.run(debug=True)

