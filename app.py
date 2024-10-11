from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/checkin')
def checkin():
    return render_template('checkin.html')

@app.route('/resources')
def resources():
    return render_template('resources.html')

@app.route('/mood_response/<mood>')
def mood_response(mood):
    if mood in ['glad', 'great']:
        message = "That's great to hear! Keep it up!"
    elif mood == 'sad':
        message = "Are you experiencing a breakup, or did you do poorly on a test?"
    elif mood == 'moody':
        message = "It's okay to feel moody sometimes. Want to talk about it?"
    elif mood == 'heartbroken':
        message = "It's tough to feel heartbroken. Remember, it's okay to seek help."
    
    return jsonify({"message": message})

"""@app.route('/mood_response/<mood>')
def mood_response(mood):
    api_key = "YOUR_OPENAI_API_KEY"
    ai_message = f"User feels {mood}. Generate follow-up questions or encouragement."
    
    # Make a request to the AI API
    response = requests.post(
        'https://api.openai.com/v1/chat/completions',
        headers={
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        },
        json={
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'user', 'content': ai_message}]
        }
    )

    if response.status_code == 200:
        ai_response = response.json()
        message = ai_response['choices'][0]['message']['content']
    else:
        message = "Sorry, I couldn't generate a response right now."

    return jsonify({"message": message})
"""

if __name__ == '__main__':
    app.run(debug=True)
