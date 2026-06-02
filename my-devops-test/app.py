from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>new   sssssssssss           Mabrouk! Your first Docker container is working! 🎉</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
