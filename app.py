from flask import Flask, render_template, request

app = Flask(__name__)

# Main route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/onezerolang')
def binary_code_one():
    return render_template('one.html')

@app.route('/binary')
def binary_code_two():
    return render_template('two.html')

@app.route('/code')
def binary_code_three():
    return render_template('three.html')
    
@app.route('/home')
def binary_code_four():
    return render_template('four.html')

# Hidden endpoint 1
@app.route('/flag')
def flag():
    return "Hidden endpoint is not here"

# Hidden endpoint 2 (fake endpoint)
@app.route('/fakeflag')
def fakeflag():
    return "faking the flag"
#endpoint 1
@app.route('/REALITY-SHIFT')
def reality_shift():
    return render_template('reality_shift.html')

#endpoint 2
@app.route('/ECHO-SILENCE')
def echo_silence():
    return render_template('echo_silence.html')

# @app.route('/echo-silence')
# def echo_silence():
#     return render_template('echo_silence.html')
#endpoint 3
@app.route('/VEIL-WALKER')
def veil_walker():
    return render_template('veil_walker.html')

# @app.route('/veil-walker')
# def veil_walker():
#     return render_template('veil_walker.html')
#endpoint 4
@app.route('/ETHEREAL-DREAM')
def ethereal_dream():
    return render_template('etherel_dream.html')

# @app.route('/ethereal-dream')
# def ethereal_dream():
#     return render_template('etherel_dream.html')

#endpoint 5
@app.route('/LABYRINTH-PATH')
def labrinth_path():
    return render_template('laby.html')

# @app.route('/labyrinth-path')
# def labrinth_path():
#     return render_template('laby.html')

#endpoint 6
@app.route('/ABYSS-GATE')
def abyss_gate():
    return render_template('abyss.html')

# @app.route('/abyss-gate')
# def abyss_gate():
#     return render_template('abyss.html')

#endpoint 7
@app.route('/REVELATION')
def revelation():
    return "THE FLAG MAY BE THIS ENDPOINT ONLY"

# @app.route('/revelation')
# def revelation():
#     return "THE FLAG MAY BE THIS ENDPOINT ONLY"

#endpoint 8
@app.route('/THRESHOLD-CODE')
def threshold_code():
    return render_template('threshold.html')

# @app.route('/threshold-code')
# def threshold_code():
#     return render_template('threshold.html')
#endpoint 9
@app.route('/ILLUSION-VEIL')
def illusion_veil():
    return render_template('illusion_veil.html')

# @app.route('/illusion-veil')
# def illusion_veil():
#     return render_template('illusion_veil.html')


#endpoint 10
@app.route('/OBLIVION-TRUTH')
def oblivion_truth():
    return render_template('ob_truth.html')

# @app.route('/oblivion-truth')
# def oblivion_truth():
#     return render_template('ob_truth.html')

#endpoint 11
@app.route('/NIGHTFALL-ECHO')
def nightfall_echo():
    return render_template('night_echo.html')

# @app.route('/nightfall-echo')
# def nightfall_echo():
#     return render_template('night_echo.html')
#endpoint 11
# @app.route('/fragment')
# def frag():
#     return render_template('frag.html')

@app.route('/FRAGMENT')
def frag():
    return render_template('frag.html')


# Hidden endpoint 3 (requires a specific header)
@app.route('/secret')
def secret():
    if 'X-Secret' in request.headers and request.headers['X-Secret'] == 'true':
        return "Congrats! You have done it, Password='codeOfLies'"
    else:
        return "Access Denied", 403

# Start the server
if __name__ == '__main__':
    app.run()
