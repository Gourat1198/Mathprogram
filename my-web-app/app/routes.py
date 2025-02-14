from flask import Flask, render_template, request
from mathprogram import some_math_function  # Import the necessary functions from mathprogram.py

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    input_value = request.form.get('input_value')
    result = some_math_function(input_value)  # Call the math function with the input value
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)