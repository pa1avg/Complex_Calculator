from flask import Flask, render_template, request, jsonify
import math

app = Flask(__name__)

# Route for the frontend
@app.route('/')
def home():
    return render_template('index.html')

# API endpoint for calculations
@app.route('/api/calculate', methods=['POST'])
def calculate():
    data = request.get_json()
    operation = data.get('operation')
    num1 = data.get('num1')  # num1 is mandatory
    num2 = data.get('num2')  # num2 is optional

    if num1 is None:
        return jsonify(error="First number (num1) is required"), 400

    try:
        num1 = float(num1)
        num2 = float(num2) if num2 else None  # Convert num2 only if provided

        if operation == "add":
            result = num1 + (num2 if num2 is not None else 0)
        elif operation == "subtract":
            result = num1 - (num2 if num2 is not None else 0)
        elif operation == "multiply":
            result = num1 * (num2 if num2 is not None else 1)
        elif operation == "divide":
            if num2 is None or num2 == 0:
                return jsonify(error="Division by zero or missing second number is not allowed"), 400
            result = num1 / num2
        elif operation == "power":
            result = math.pow(num1, num2 if num2 is not None else 1)
        elif operation == "sqrt":
            if num1 < 0:
                return jsonify(error="Square root of negative number is not allowed"), 400
            result = math.sqrt(num1)
        elif operation == "factorial":
            if num1 < 0 or not num1.is_integer():
                return jsonify(error="Factorial is only defined for non-negative integers"), 400
            result = math.factorial(int(num1))
        else:
            return jsonify(error="Invalid operation"), 400
    except Exception as e:
        return jsonify(error=str(e)), 500

    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
