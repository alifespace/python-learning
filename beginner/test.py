from flask import Flask
app = Flask(__name__)

@app.route('/')
def Hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)
    app.run(host='0.0.0.0', port=5000)
