from flask import Flask, redirect, url_for, render_template
# from flask_caching import Cache

# cache = Cache()
app = Flask(__name__)
app.static_folder = 'static'
app.template_folder = 'templates'
# app.config['SERVER_NAME, SERVER_NAME'] = 'www.swimmingworld.ir, swimmingworld.ir'
# app.config['SERVER_NAME, SERVER_NAME'] = '127.0.0.1:5000, localhost:5000'



@app.route('/')
def home():
    return render_template('blog/index.html')

# ####################### butterfly ####################### #

@app.route('/butterfly/arm_drills')
def butterfly_arm():
    return render_template('blog/butterfly/arm.html')

@app.route('/butterfly/kick_drills')
def butterfly_kick():
    return render_template('blog/butterfly/kick.html')

@app.route('/butterfly/body_position_drills')
def butterfly_body_position():
    return render_template('blog/butterfly/body-position.html')

@app.route('/butterfly/breathing_drills')
def butterfly_breathing():
    return render_template('blog/butterfly/breathing.html')

@app.route('/butterfly/coordination_drills')
def butterfly_coordination():
    return render_template('blog/butterfly/coordination.html')

@app.route('/butterfly/leverage_drills')
def butterfly_leverage():
    return render_template('blog/butterfly/leverage.html')

@app.route('/butterfly/recovery_drills')
def butterfly_recovery():
    return render_template('blog/butterfly/recovery.html')

# ####################### breaststroke ####################### #


@app.route('/breaststroke/arm_drills')
def breaststroke_arm():
    return render_template('blog/breaststroke/arm.html')

@app.route('/breaststroke/kick_drills')
def breaststroke_kick():
    return render_template('blog/breaststroke/kick.html')

@app.route('/breaststroke/body_position_drills')
def breaststroke_body_position():
    return render_template('blog/breaststroke/body-position.html')

@app.route('/breaststroke/breathing_drills')
def breaststroke_breathing():
    return render_template('blog/breaststroke/breathing.html')

@app.route('/breaststroke/coordination_drills')
def breaststroke_coordination():
    return render_template('blog/breaststroke/coordination.html')

@app.route('/breaststroke/leverage_drills')
def breaststroke_leverage():
    return render_template('blog/breaststroke/leverage.html')

@app.route('/breaststroke/recovery_drills')
def breaststroke_recovery():
    return render_template('blog/breaststroke/recovery.html')

# ####################### backstroke ####################### #


@app.route('/backstroke/arm_drills')
def backstroke_arm():
    return render_template('blog/backstroke/arm.html')

@app.route('/backstroke/kick_drills')
def backstroke_kick():
    return render_template('blog/backstroke/kick.html')

@app.route('/backstroke/body_position_drills')
def backstroke_body_position():
    return render_template('blog/backstroke/body-position.html')

@app.route('/backstroke/breathing_drills')
def backstroke_breathing():
    return render_template('blog/backstroke/breathing.html')

@app.route('/backstroke/coordination_drills')
def backstroke_coordination():
    return render_template('blog/backstroke/coordination.html')

@app.route('/backstroke/leverage_drills')
def backstroke_leverage():
    return render_template('blog/backstroke/leverage.html')

@app.route('/backstroke/recovery_drills')
def backstroke_recovery():
    return render_template('blog/backstroke/recovery.html')

# ####################### freestyle ####################### #


@app.route('/freestyle/arm_drills')
def freestyle_arm():
    return render_template('blog/freestyle/arm.html')

@app.route('/freestyle/kick_drills')
def freestyle_kick():
    return render_template('blog/freestyle/kick.html')

@app.route('/freestyle/body_position_drills')
def freestyle_body_position():
    return render_template('blog/freestyle/body-position.html')

@app.route('/freestyle/breathing_drills')
def freestyle_breathing():
    return render_template('blog/freestyle/breathing.html')

@app.route('/freestyle/coordination_drills')
def freestyle_coordination():
    return render_template('blog/freestyle/coordination.html')

@app.route('/freestyle/leverage_drills')
def freestyle_leverage():
    return render_template('blog/freestyle/leverage.html')

@app.route('/freestyle/recovery_drills')
def freestyle_recovery():
    return render_template('blog/freestyle/recovery.html')

# ####################### flexibility ####################### #

@app.route('/Flexibility')
def flexibility():
    return render_template('blog/flexibility/flexibility.html')

# ####################### bodybuilding ####################### #

@app.route('/full_body')
def full_body():
    return render_template('blog/bodybuilding/fullbody.html')

@app.route('/upper_lower')
def upper_lower():
    return render_template('blog/bodybuilding/upper_lower.html')

@app.route('/pull_push_legs')
def pull_push_legs():
    return render_template('blog/bodybuilding/pull_push_legs.html')

@app.route('/Body_Part')
def body_part():
    return render_template('blog/bodybuilding/body_part.html')

# ####################### amoozesh ####################### #

@app.route('/butterfly')
def butterfly():
    return render_template('blog/amoozesh/butterfly.html')

@app.route('/backstroke')
def backstroke():
    return render_template('blog/amoozesh/backstroke.html')

@app.route('/breaststroke')
def breaststroke():
    return render_template('blog/amoozesh/breaststroke.html')

@app.route('/freestyle')
def freestyle():
    return render_template('blog/amoozesh/freestyle.html')

# ####################### login ####################### #
@app.route('/login')
def login():
    return render_template('auth/login.html')

@app.route('/forget_password')
def forget():
    return render_template('auth/forget.html')

@app.route('/register')
def register():
    return render_template('auth/register.html')

@app.route('/about_us')
def about():
    return render_template('blog/about.html')

# ####################### article ####################### #

@app.route('/Winter_mixed_swim')
def number_1():
    return render_template('blog/article/1.html')

@app.route('/Wim_Hof_Method')
def number_2():
    return render_template('blog/article/2.html')

@app.route('/How_to_adapt_your_breaststroke')
def number_3():
    return render_template('blog/article/3.html')

@app.route('/Sea_swimming_for_beginners')
def number_4():
    return render_template('blog/article/4.html')

@app.route('/How_to_improve_your_swim_strength')
def number_5():
    return render_template('blog/article/5.html')

@app.route('/How_to_get_more_out_of_each_stroke')
def number_6():
    return render_template('blog/article/6.html')

@app.route('/The_Difference_Between_Short_Swim_Fins_And_Long')
def number_7():
    return render_template('blog/article/7.html')

@app.route('/Which_part')
def number_8():
    return render_template('blog/article/8.html')

@app.route('/Can_swimming_help')
def number_9():
    return render_template('blog/article/9.html')

@app.route('/How_to_keep_your_swim_fitness')
def number_10():
    return render_template('blog/article/10.html')
@app.route('/Overcome_your_open-water_swimming_fears')
def number_11():
    return render_template('blog/article/11.html')
@app.route('/Top_6_annoying_habits_of_pool_swimmers')
def number_12():
    return render_template('blog/article/12.html')


if __name__ == '__main__':
    app.run(debug=True)