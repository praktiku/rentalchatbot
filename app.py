from flask import Flask, render_template, request, jsonify
from chat import chatbot

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/sendmsg", methods = ['post'])
def sendmsg():
    msg = request.get_json().get("message")
    print(str(msg))
    get_chat = chatbot(msg)

    return jsonify(answer=get_chat)

# if __name__ == '__main__':
#     app.run(debug=True)
