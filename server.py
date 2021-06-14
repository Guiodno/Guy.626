from flask import Flask ,request, render_template

app = Flask(__name__)

db_email = ['djtrueway@icloud.com', 'guy@yahoo.fr','laguerre@gmail.com','michelle@icloud.com',]
db_password = ['26199210','36476476','93476456','09378726',]

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
        if ((email in db_email) and (password in db_password)):
            return "Connect"
        else:
            return "email or password incorrect"

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
