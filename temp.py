from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import datetime
import secrets
import json


app = Flask(__name__, template_folder='templates')
app.secret_key = 'your_secret_key_here'
secret_key = secrets.token_hex(16)

# Configure MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Owenisas@123",
    database="owenisas",
    port=3305
)


@app.route('/', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        print(request.form)
        captcha_response = request.form['h-captcha-response']
        import requests
        response = requests.post('https://hcaptcha.com/siteverify', data={
            'response': captcha_response,
            'secret': '0x2c8ef7Fe739e3a6171B9dD4a951C1e3AE8506fFE'
        })
        data = response.json()
        if data['success']:
            username = request.form['username']
            email = request.form['email']
            password = request.form['password']
            # Create a cursor to execute SQL queries
            cursor = db.cursor()
            cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
            existing_users = cursor.fetchall()
            print(existing_users)
            for user in existing_users:
                if user[1] == username and user[3] == email:
                    return "Username and email already exist"
                elif user[1] == username:
                    print("Username already exist")
                    return "Username already exist"
                elif user[3] == email:
                    print("Email already exist, Please try another Email or login")
                    return "Email already exist, Please try another Email or login"
            # Insert data into the database
            sql = "INSERT INTO users (username, password, email, registered_at) VALUES (%s, %s, %s, %s)"
            values = (username, email, password, datetime.datetime.now())
            cursor.execute(sql, values)
            db.commit()

            cursor.close()

            return "Registration successful!"
        else:
            return "Please finish the Captcha and try again"
    else:
        return render_template('register.html')


if __name__ == '__main__':
    app.run()
