from flask import Flask, Response, request, render_template, session, url_for
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
@app.route('/home')
def homePage():
    return render_template('layout.html', title='Home')


@app.route('/about_us')
def about_us():
    return render_template('about_us.html', title='About_us')


@app.route('/subscribe')
def subscribe():
    return render_template('subscribe.html', title='Subscribe')

@app.route('/collection')
def collection():
    return render_template('collection.html', title='Product Collection')

@app.route('/Aglaonema-Pink-Star')
def AGLAONEMA_PINK_STAR():
    return render_template('/flower_pages/aps.html', title='Aglaonema Pink Star')

@app.route('/Epipremnum-Aureum')
def Epipremnum_Aureum():
    return render_template('/flower_pages/ea.html', title='Epipremnum Aureum')

@app.route('/STRELITZIA-NICOLAI')
def STRELITZIA_NICOLAI():
    return render_template('/flower_pages/sn.html', title='Strelitzia Nicolai')

@app.route('/login', methods=['GET', 'POST'])
def customer_login_url():
    print(request.method)
    if request.method == 'POST':
        session['username'] = request.form['username']
        print(session['username'])
        return render_template('customer_login.html', title='Customer Login')
    return render_template('customer_login.html', title='Customer Login')

# SUGGESTION: ADD A TABLE TO ALLOW A POST REQUEST INTO A DATABASE. COLUMNS: PERSON ID, FIRST NAME, LAST NAME AND EMAIL, PASSWORD
# SUBSCRIBE PAGE
# @app.route('/subscribe') #ROUTE TO SUBSCRIBE PAGE
# def subscribe_url():
#     home_page = url_for('homepage_url')
#     about_us = url_for('about_us_url')
#     collection = url_for('collection_url')
#     login = url_for('customer_login_url')
#     admin = url_for('admin_login_url')
#     return render_template('subscribedemo.html', title='Subscribe')


# SUGGESTION: INTEGRATED INTO A DATABASE TO CHECK CREDENTIALS (USERNAME = EMAIL, PASSWORD)
# SUGGESTION: INTEGRATE TO AN ADMINISTRATOR DATABASE. COLUMNS: PERSON ID, FIRST NAME, LAST NAME, EMAIL ADDRESS PASSWORD
@app.route('/admin')  # ROUTE TO CUSTOMER LOGIN PAGE
def admin_login_url():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    collection = url_for('collection_url')
    subscribe = url_for('subscribe_url')
    login = url_for('customer_login_url')
    return f"""
        <!doctype>
        <html>
            <head>
                <title>Administrator Login</title>
                <link rel="stylesheet" href="{url_for('static', filename='mainStyle.css')}">
            </head>
            <body>
                <h1>
                    Plantify
                </h1>

                <h2>
                    Log Into Your Account
                </h2>

                <p>
                    Enter your Administrator login details:
                    <br>
                </p>
                <hr>
                <h2>
                    Menu
                </h2>
                    <a href="{home_page}">Home</a>
                    <a href="{about_us}">About Us</a>
                    <a href="{collection}">Collection</a>
                    <a href="{subscribe}">Subscribe</a>
                    <a href="{login}">Log in</a>
                    <b>Administrator Login</b>
                <hr>
                <h8>
                    copyright Plantify ltd
                </h8>
            </body>
        </html> 
        """


# RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=True)