from flask import Flask, request, jsonify
import calculation

app = Flask(__name__)

@app.route('/process_file', methods=['POST'])
def process_file():
    file_path = request.json.get('file_path')

    # print('file path fetched!')
    return jsonify({'result': file_path})

@app.route('/calculate', methods=['POST'])
def calculating_numbers():
    value_a = request.json.get('value_a')
    value_b = request.json.get('value_b')
    result = calculation.addition_calc(value_a, value_b)

    return jsonify({'result': result})

@app.route('/calculate_sub', methods=['POST'])
def calculating_num_sub():
    value_a = request.json.get('value_a')
    value_b = request.json.get('value_b')
    result = calculation.subtraction_calc(value_a, value_b)

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True) 
