from flask import Flask, render_template, request, jsonify, session
from chatbot import get_answer

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/')
def chat():
    return render_template('chat.html', chat_history=session.get('chat_history', []))

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['user_input']
    lang_pref = request.form.get('language', 'en')

    bot_response, citation = get_answer(user_input, lang_pref, include_raw=True)

    if citation:
        bot_response += f"\n\n📘 *Source: {citation}*"

    chat_history = session.get('chat_history', [])
    chat_history.append({'user': user_input, 'bot': bot_response})
    session['chat_history'] = chat_history

    return jsonify({
        'user': user_input,
        'bot': bot_response
    })

@app.route('/clear')
def clear_chat():
    session['chat_history'] = []
    return jsonify({'status': 'cleared'})

if __name__ == '__main__':
    app.run(debug=False)
