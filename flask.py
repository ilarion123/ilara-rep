from flask import Flask,request
app = Flask(__name__)

@app.route('/')
def get_user():
    return "text"
if __name__ == '__main__':
    app.run(debug=True)
