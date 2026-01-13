from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, Flask!'

# Задание 1
@app.route('/hello')
def hello_world():
    return 'Hello, world!'

@app.route('/info')
def info():
    return 'This is an informational page.'

# Задание 2
@app.route('/calc/<int:a>/<int:b>')
def calc(a, b):
    return f"The sum of {a} and {b} is {a + b}."

# Задание 3
@app.route('/reverse/<text>')
def reverse(text):
    return text[::-1]

# Задание 4
@app.route('/user/<name>/<int:age>')
def user(name, age):
    if age < 0:
        return 'Error: Age cannot be negative.', 400
    return f"Hello, {name}. You are {age} years old."

if __name__ == '__main__':
    app.run(debug=True)