from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world!'

@app.route('/test')
def test():
    return 'test world!'

if __name__ == "__main__":
    app.run(debug=True)