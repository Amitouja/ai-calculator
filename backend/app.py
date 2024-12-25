from flask import Flask, jsonify, render_template, request
from util.ai import ai_calc

app = Flask(__name__)   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calc2')
def calc2():
    return render_template('ai_calculator.html')



@app.route('/calculator')
def calculator():
    # Get parameters from the query string (URL)
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        operation = request.args.get('operation')

        # Perform the calculation based on the operation
        if operation == 'add':
            result = num1 + num2
        elif operation == 'subtract':
            result = num1 - num2
        elif operation == 'multiply':
            result = num1 * num2
        elif operation == 'divide':
            if num2 != 0:
                result = num1 / num2
            else:
                return jsonify({"error": "Division by zero is not allowed"}), 400
        else:
            return jsonify({"error": "Invalid operation"}), 400

        # Return the result as JSON
        return jsonify({"result": result})


@app.route('/ai_calculator')
def ai_calculator():
    question = request.args.get('question')

    result = ai_calc(question)

    return jsonify({"result": result})




if __name__ == '__main__':
    app.run(debug=True)

