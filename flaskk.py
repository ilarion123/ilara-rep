from flask import Flask,render_template

app = Flask(__name__,template_folder=("flask"))

@app.route('/')
def home():
    return render_template('flask.html')

if __name__ == '__main__':
    app.run(debug=True)