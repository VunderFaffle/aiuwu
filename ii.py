from flask import Flask, request, jsonify
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
