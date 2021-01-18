from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('blog/index.html')

# ####################### butterfly ####################### #

@app.route('/butterfly/arm_drills')
def arm():
    return render_template('blog/butterfly/arm.html')

@app.route('/butterfly/kick_drills')
def kick():
    return render_template('blog/butterfly/kick.html')

@app.route('/butterfly/body_position_drills')
def body_position():
    return render_template('blog/butterfly/body-position.html')

@app.route('/butterfly/breathing_drills')
def breathing():
    return render_template('blog/butterfly/breathing.html')

@app.route('/butterfly/coordination_drills')
def coordination():
    return render_template('blog/butterfly/coordination.html')

@app.route('/butterfly/leverage_drills')
def leverage():
    return render_template('blog/butterfly/leverage.html')

@app.route('/butterfly/recovery_drills')
def recovery():
    return render_template('blog/butterfly/recovery.html')

















@app.route('/about_us')
def about():
    return render_template('blog/about.html')

if __name__ == '__main__':
    app.run(debug=True)