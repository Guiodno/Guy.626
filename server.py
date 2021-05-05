from flask import Flask ,request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "GET":
        return render_template('index.html')
    elif request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        # debug 
        print(email)
        print(password)

        if ((email == "") or (password== "")) or ((email == None) or (password== None)):
            return "please give your email and your password"
        return "Connect"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
