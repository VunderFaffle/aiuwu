from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/compute', methods=['POST'])
def compute():
    data = request.json  # Получить данные
    # Выполнить вычисления
    result = data['value'] * 2  # пример
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(port=5000)
