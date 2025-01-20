import sys
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/PoC')
def proof_of_concept():
    return render_template('poc.html')

@app.route('/contact')
def contact():
    return redirect('/PoC')

@app.route('/login')
def login():
    return redirect('/PoC')

@app.route('/instapay', methods=['post'])
def instapay():
    try:
        recipient_phone = request.form['phone']
        debit_amount = request.form['amount']

        _phone = f"+1 ({recipient_phone[:3]})-{recipient_phone[3:6]}-{recipient_phone[6:]}"
    except Exception as ex:
        print('[ERROR]')
        print(ex, file=sys.stderr)
    return render_template('success.html', phone=_phone, amount=debit_amount)

if __name__ == "__main__":
    app.run(debug=True)
