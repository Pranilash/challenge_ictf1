from flask import Flask, request, render_template, redirect, make_response
import base64

app = Flask(__name__)

def rot_n(text, n):
    return text.translate(str.maketrans(
        "abcdefghijklmnopqrstuvwxyz",
        "abcdefghijklmnopqrstuvwxyz"[n:] + "abcdefghijklmnopqrstuvwxyz"[:n]
    ))

def encode_hex(text):
    return text.encode('utf-8').hex()

def encode_base64(text):
    return base64.b64encode(text.encode()).decode()

target = "incognitoctf"
correct_value = rot_n(target, 23)

@app.route('/')
def index():
    challenge_cookie = request.cookies.get("admin")
    print(f"Received Cookie: {challenge_cookie}")

    if not challenge_cookie:
        resp = make_response(render_template('index.html', message="Welcome agent."))
        resp.set_cookie("admin", "none")
        return resp

    if challenge_cookie == correct_value:
        return render_template('hidden.html', audio_file="/static/youshouldknowthis.mp3")

    for i in range(1, 27):
        if i == 11:
            continue
        if challenge_cookie == rot_n(target, i):
            return render_template(f'rot{i}.html')

    if challenge_cookie == encode_base64(target):
        return render_template('rot_base64.html')

    if challenge_cookie == encode_hex(target):
        return render_template('rot_hex.html')

    return render_template('index.html', message="Invalid cookie value! Check your cookies, hacker. Tracing IP...")

@app.route('/setcookie/<method>')
def set_cookie(method):
    val = ""
    if method.startswith("rot") and method[3:].isdigit():
        n = int(method[3:])
        if 1 <= n <= 26:
            val = rot_n(target, n)
    elif method == "hex":
        val = encode_hex(target)
    elif method == "base64":
        val = encode_base64(target)
    else:
        return "Invalid method", 400

    resp = make_response(redirect("/"))
    resp.set_cookie("admin", val)
    return resp

if __name__ == '__main__':
    app.run(debug=True, port=5000)
