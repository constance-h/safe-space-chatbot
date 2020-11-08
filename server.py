from flask import Flask, render_template, request
from chatbot import bot

app = Flask(__name__)


# while True:
#     user_input = input(">>>")

#     if user_input == "goodbye":
#         print("goodbye")
#         break
#     else:
#         response = spacey.get_response(user_input)
#         print(response)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/chatbot')
def chatbot():
    return render_template("chatbot.html")

@app.route('/get_response')
def get_bot_response():
   
    user_input = request.args.get("msg")
    bot_response = bot.get_response(user_input)
    return str(bot_response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
