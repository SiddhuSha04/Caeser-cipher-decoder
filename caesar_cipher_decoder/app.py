from flask import Flask, render_template, request

app = Flask(__name__)


def caesar_cipher_encrypt(text, shift):
    encrypted_text = []
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text.append(chr((ord(char) - shift_base + shift) % 26 + shift_base))
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def caesar_cipher_bruteforce(text):
    results = []
    for shift in range(26):
        decrypted_text = caesar_cipher_decrypt(text, shift)
        results.append((shift, decrypted_text))
    return results

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ''
    brute_force_results = []
    if request.method == 'POST':
        text = request.form.get('text', '')
        if 'shift' in request.form:
            shift = int(request.form['shift'])
            operation = request.form['operation']
            if operation == 'encrypt':
                result = caesar_cipher_encrypt(text, shift)
            elif operation == 'decrypt':
                result = caesar_cipher_decrypt(text, shift)
        elif 'bruteforce' in request.form:
            if text:
                brute_force_results = caesar_cipher_bruteforce(text)
    return render_template('index.html', result=result, brute_force_results=brute_force_results)

if __name__ == '__main__':
    app.run(debug=True)
