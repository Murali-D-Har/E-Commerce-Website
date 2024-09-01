python
import random
import string
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

url_mappings = {}

def generate_short_code():
    characters = string.ascii_letters + string.digits
    short_code = ''.join(random.choice(characters) for _ in range(6))
    return short_code

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('original_url')
    if original_url:
        short_code = generate_short_code()
        url_mappings[short_code] = original_url
        short_url = f"http://localhost:5000/{short_code}"
        return render_template('index.html', short_url=short_url)
    return render_template('index.html', error="Invalid URL.")

@app.route('/<short_code>')
def redirect_to_original_url(short_code):
    if short_code in url_mappings:
        original_url = url_mappings[short_code]
        return redirect(original_url, code=302)
    return "URL not found."

if __name__ == '__main__':
    app.run(debug=True)