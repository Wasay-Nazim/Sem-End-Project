from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

HARDCODED_CREDENTIALS = {
    "wasaynazim@gmail.com": "123",
    "tasmeenbaloch20@gmail.com": "123",
    "kanzaghalib577@gmail.com": "123",
    "meerabs031@gmail.com": "123"
}

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if email in HARDCODED_CREDENTIALS and HARDCODED_CREDENTIALS[email] == password:
            return redirect(url_for('home'))  
        else:
            return render_template('login.html', error="Invalid email or password")  
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/men')
def men():
    return render_template('men.html')

@app.route('/women')
def women():
    return render_template('women.html')

@app.route('/children')
def children():
    return render_template('children.html')

@app.route('/premium')
def premium():
    return render_template('premium.html')

@app.route('/aboutus')
def about_us():
    return render_template('aboutus.html')

@app.route('/assistant')
def assistant():
    return render_template('assistant.html')

@app.route('/a')  
def a():
    return render_template('a.html')
@app.route('/aa')  
def aa():
    return render_template('aa.html')
@app.route('/aaa')  
def aaa():
    return render_template('aaa.html')
@app.route('/aaaa')  
def aaaa():
    return render_template('aaaa.html')
@app.route('/b')  
def b():
    return render_template('b.html')
@app.route('/bb')  
def bb():
    return render_template('bb.html')
@app.route('/bbb')  
def bbb():
    return render_template('bbb.html')
@app.route('/bbbb')  
def bbbb():
    return render_template('bbbb.html')
@app.route('/c')  
def c():
    return render_template('c.html')
@app.route('/cc')  
def cc():
    return render_template('cc.html')
@app.route('/ccc')  
def ccc():
    return render_template('ccc.html')
@app.route('/cccc')  
def cccc():
    return render_template('cccc.html')
@app.route('/d')  
def d():
    return render_template('d.html')
@app.route('/dd')  
def dd():
    return render_template('dd.html')
@app.route('/ddd')  
def ddd():
    return render_template('ddd.html')
@app.route('/dddd')  
def dddd():
    return render_template('dddd.html')
@app.route('/checkout')  
def checkout():
    return render_template('checkout.html')
@app.route('/thankyou')  
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
