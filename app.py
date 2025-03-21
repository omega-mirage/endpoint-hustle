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
