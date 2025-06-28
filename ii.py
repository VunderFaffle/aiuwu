from flask import Flask, request, jsonify, send_file
from openai import OpenAI


app = Flask(__name__)

client = None

def setClient(apikey):
    global client
    client = OpenAI(
        api_key=apikey,
        base_url='https://bothub.chat/api/v2/openai/v1'
    )

def ask(query):
    global client
    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': f"{query}",
            }
        ],
        model='gpt-4.1',

    )
    return chat_completion.choices[0].message.content



@app.route('/download1')
def download_file1():
    # путь к файлу на сервере
    filepath = 'dist/client.exe'
    return send_file(
        filepath,
        as_attachment=True,  # указывает, что файл должен скачиваться, а не отображаться
    )

@app.route('/download2')
def download_file2():
    # путь к файлу на сервере
    filepath = 'client.apk'
    return send_file(
        filepath,
        as_attachment=True,  # указывает, что файл должен скачиваться, а не отображаться
    )

@app.route('/compute', methods=['POST'])
def compute():
    global ask, setkey
    data = request.json  # Получить данные
    # Выполнить вычисления
    req = data['value']
    
    if data['apikey'] != "":
        setClient(data["apikey"])
        
    result = ask(req)
    print(result)
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000)
