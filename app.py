from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Generate a new OTP
def generate_otp():
    return random.randint(100000, 999999)

# Store the OTP in memory
otp = generate_otp()

@app.route('/')
def index():
    return render_template('index.html', otp=otp)

@app.route('/verify', methods=['POST'])
def verify():
    entered_otp = request.form.get('otp')
    if entered_otp and int(entered_otp) == otp:
        return render_template('result.html', message="✅ OTP Verified Successfully!")
    else:
        return render_template('result.html', message="❌ Invalid OTP. Please try again.")

if __name__ == '__main__':
    app.run(debug=True)
