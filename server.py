from flask import Flask, request, render_template, redirect
import os

def rot_n(text, n):
    return text.translate(str.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "abcdefghijklmnopqrstuvwxyz"[n:] + "abcdefghijklmnopqrstuvwxyz"[:n]
    ))

app = Flask(__name__)

correct_value = rot_n("incognitoctf", 11)

@app.route('/')
def index():
    challenge_cookie = request.cookies.get("challenge")
    print(f"Received Cookie: {challenge_cookie}")  # Debugging line
    
    if challenge_cookie == correct_value:
        return render_template('hidden.html', audio_file="/static/youshouldknowthis.mp3")
    elif challenge_cookie == rot_n("incognitoctf", 1):
        return render_template('rot1.html')
    elif challenge_cookie == rot_n("incognitoctf", 2):
        return render_template('rot2.html')
    elif challenge_cookie == rot_n("incognitoctf", 3):
        return render_template('rot3.html')
    elif challenge_cookie == rot_n("incognitoctf", 4):
        return render_template('rot4.html')
    elif challenge_cookie == rot_n("incognitoctf", 5):
        return render_template('rot5.html')
    elif challenge_cookie == rot_n("incognitoctf", 6):
        return render_template('rot6.html')
    elif challenge_cookie == rot_n("incognitoctf", 7):
        return render_template('rot7.html')
    elif challenge_cookie == rot_n("incognitoctf", 8):
        return render_template('rot8.html')
    elif challenge_cookie == rot_n("incognitoctf", 9):
        return render_template('rot9.html')
    elif challenge_cookie == rot_n("incognitoctf", 10):
        return render_template('rot10.html')
    elif challenge_cookie == rot_n("incognitoctf", 12):
        return render_template('rot12.html')
    elif challenge_cookie == rot_n("incognitoctf", 13):
        return render_template('rot13.html')
    else:
        return render_template('index.html', message="Invalid cookie value! Check your cookies, hacker. Tracing IP...")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
