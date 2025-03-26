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

#endpoint 3
@app.route('/VEIL-WALKER')
def veil_walker():
    return "VEIL-WALKER"

#endpoint 4
@app.route('/ETHEREAL-DREAM')
def ethereal_dream():
    return "ETHEREAL-DREAM"

#endpoint 5
@app.route('/LABYRINTH-PATH')
def labrinth_path():
    return "LABYRINTH-PATH"

#endpoint 6
@app.route('/ABYSS-GATE')
def abyss_gate():
    return "ABYSS-GATE"

#endpoint 7
@app.route('/REVELATION')
def revelation():
    return "THE FLAG MAY BE THIS ENDPOINT ONLY"

#endpoint 8
@app.route('/THRESHOLD-CODE')
def threshold_code():
    return "THRESHOLD-CODE"

#endpoint 9
@app.route('/ILLUSION-VEIL')
def illusion_veil():
    return "ILLUSION-VEIL"

#endpoint 10
@app.route('/OBLIVION-TRUTH')
def oblivion_truth():
    return "OBLIVION-TRUTH"

#endpoint 11
@app.route('/NIGHTFALL-ECHO')
def nightfall_echo():
    return "NIGHTFALL-ECHO"

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
