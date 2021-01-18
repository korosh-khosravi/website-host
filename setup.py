from flask import Flask, redirect, url_for, render_template, Blueprint

app = Flask(__name__, template_folder='flaskr/templates')

c = ['korosh', 'maryam', 'khosrow',"armin"]

@app.route('/')
def home():
    return render_template('index.html', content=c)


if __name__ == '__main__':
    app.run(debug=True)