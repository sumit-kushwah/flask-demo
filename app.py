from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    with open('./files/one.txt', 'r') as f:
        output = f.read()
    return output


if __name__ == '__main__':
    app.run(debug=False)
