from flask import Flask, render_template, redirect, url_for, request, session, flash
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your-secret-key-1234'  # Change for production

# Temporary user storage (replace with database in production)
users = {}

# ------------------- Authentication Routes -------------------
@app.route('/')
def welcome():
    return redirect(url_for('welcome'))

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = users.get(email)
        if user and check_password_hash(user['password'], password):
            session['user'] = email
            return redirect(url_for('home'))
        
        flash('Invalid email or password', 'error')
        return redirect(url_for('login'))
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        if password != confirm_password:
            flash('Passwords do not match', 'error')
            return redirect(url_for('register'))
        
        if email in users:
            flash('Email already registered', 'error')
            return redirect(url_for('register'))
        
        users[email] = {
            'password': generate_password_hash(password)
        }
        flash('Registration successful! Please login', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

# ... rest of the routes remain unchanged ...

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('welcome'))

# ------------------- Product Category Routes -------------------
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

# ------------------- Product Collection Routes -------------------
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

# ------------------- Other Pages -------------------
@app.route('/about_us')
def about_us():
    return render_template('aboutus.html')

@app.route('/assistant')
def assistant():
    return render_template('assistant.html')

@app.route('/checkout')
def checkout():
    return render_template('checkout.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)