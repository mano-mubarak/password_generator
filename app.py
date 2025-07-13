from flask import Flask, render_template, request, redirect
import string
import random
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def a():
    password = ''
    letters = list(string.ascii_letters)+list("!@#$%^&*()0123456789")
    Number_of_characters = 15
    if request.method == 'POST':
        Number_of_characters = int(request.form.get('num'))
        password = ''.join(random.sample(letters, Number_of_characters))
        with open("password.txt","a") as password_file:
            password_file.write(password + '\n')
    return render_template('password.html', password=password, num=Number_of_characters)
import os
app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
