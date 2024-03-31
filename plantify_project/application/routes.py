from flask import Flask, Response, request, render_template

app = Flask(__name__)


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
def collection_url():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    subscribe = url_for('subscribe_url')
    login = url_for('customer_login_url')
    admin = url_for('admin_login_url')
    return f"""
    <!doctype>
     <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Collection</title>
        <link rel="stylesheet" href="{url_for('static', filename='mainStyle.css')}">
        </head>
        <body>
            <h1>
                Plantify
            </h1>
            <h2>
                Our Collection
            </h2>
            <p>
                Shop our collection and 
                    <a href="{subscribe}">subscribe </a>
                to our mailing list for tips to help your plant flourishing indoors.
                <br>
                <br>
            </p>

            <h3>
                AGLAONEMA PINK STAR
            </h3>
             <a href='/Aglaonema-Pink-Star'>
             <img src="/static/Aglaonema-Pink-Star.png" alt="Aglaonema Pink Star" width="300" height="200">
            </a>
                <br>
            <h3>
                EPIPREMNUM AUREUM (DEVILS IVY, GOLDEN POTHOS)
            </h3>
             <a href='/Epipremnum-Aureum'>
             <img src="/static/Epipremnum-Aureum.png" alt="Epipremnum Aureum" width="300" height="200">
            </a>
                <br>
             <h3>
                STRELITZIA NICOLAI
            </h3>
             <a href='/STRELITZIA-NICOLAI'>
             <img src="/static/STRELITZIA-NICOLAI.png" alt="Strelitzia Nicolai" width="300" height="200">
            </a>
                <br>         
            <hr>
            <h2>
                Menu
            </h2>
                <a href="{home_page}">Home</a>
                <a href="{about_us}">About Us</a>
                <b>Collection</b>
                <a href="{subscribe}">Subscribe</a>
                <a href="{login}">Login</a>
                <a href="{admin}">Administrator Login</a>
            <hr>
            <h8>
                copyright Plantify ltd
            </h8>
        </body>
    </html> 
    """


@app.route('/Aglaonema-Pink-Star')
def AGLAONEMA_PINK_STAR():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    subscribe = url_for('subscribe_url')
    login = url_for('customer_login_url')
    admin = url_for('admin_login_url')
    collection = url_for('collection_url')
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AGLAONEMA PINK STAR</title>
         <link rel="stylesheet" href="{url_for('static', filename='mainStyle.css')}">
    </head>
    <body>
        <h1>AGLAONEMA PINK STAR </h1>
        <p>This Aglaonema Pink Star</p>
        <img src="/static/Aglaonema-Pink-Star.png" alt="Aglaonema Pink Star" width="300" height="200">
        <p>The Aglaonema Pink Star is a gorgeous rare plant that will thrive easily in your home. Tolerant of low light 
        conditions and easy care, they are perfect plants for the beginner but attractive collector plants for more 
        experienced growers.</p>
        <span>Page 1</span>
        <a href='/Epipremnum-Aureum'>Next</a>  
          <br>         
            <hr>
            <h2>
                Menu
            </h2>
                <a href="{home_page}">Home</a>
                <a href="{about_us}">About Us</a>
                <a href="{collection}">Plant Collection</a>
                <a href="{subscribe}">Subscribe</a>
                <a href="{login}">Login</a>
                <a href="{admin}">Administrator Login</a>
            <hr>
            <h8>
                copyright Plantify ltd
            </h8>
        </body>
    </html> 
    """


@app.route('/Epipremnum-Aureum')
def Epipremnum_Aureum():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    subscribe = url_for('subscribe_url')
    login = url_for('customer_login_url')
    admin = url_for('admin_login_url')
    collection = url_for('collection_url')
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>EPIPREMNUM AUREUM</title>
         <link rel="stylesheet" href="{url_for('static', filename='mainStyle.css')}">
    </head>
    <body>
        <h1>EPIPREMNUM AUREUM (DEVILS IVY, GOLDEN POTHOS) </h1>
        <p>This is Epipremnum-Aureum </p>
        <img src="/static/Epipremnum-Aureum.png" alt="Epipremnum-Aureum" width="300" height="200">
        <p>Pothos Plants, or Epipremnum Aureum, are native to the jungles of Malaysia and are highly adaptable, 
        glossy-leafed plants with heart-shaped leaves. Epipremnum Aureum or devils Ivy is easy to care for and can grow 
        almost anywhere. In other words, a perfect houseplant for beginners.</p>
        <span>Page 2</span>
        <a href='/Aglaonema-Pink-Star'>Previous</a>
        <a href='/STRELITZIA-NICOLAI'>Next</a>  
          <br>         
            <hr>
            <h2>
                Menu
            </h2>
                <a href="{home_page}">Home</a>
                <a href="{about_us}">About Us</a>
                <a href="{collection}">Plant Collection</a>
                <a href="{subscribe}">Subscribe</a>
                <a href="{login}">Login</a>
                <a href="{admin}">Administrator Login</a>
            <hr>
            <h8>
                copyright Plantify ltd
            </h8>
        </body>
    </html> 
    """


@app.route('/STRELITZIA-NICOLAI')
def STRELITZIA_NICOLAI():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    subscribe = url_for('subscribe_url')
    login = url_for('customer_login_url')
    admin = url_for('admin_login_url')
    collection = url_for('collection_url')
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>STRELITZIA-NICOLAI</title>
         <link rel="stylesheet" href="{url_for('static', filename='mainStyle.css')}">
    </head>
    <body>
        <h1>STRELITZIA-NICOLAI </h1>
        <p>This Aglaonema Pink Star</p>
        <img src="/static/STRELITZIA-NICOLAI.png" alt="Strelitzia Nicolai" width="300" height="200">
        <p>This is Strelitzia Nicolai, this structural evergreen is primarily grown for its handsome (banana-like) 
        foliage, which becomes shredded as it ages. Given time and the right conditions however, it may occasionally 
        produce a blue and white flowerhead too.</p>
        <span>Page 3</span>
        <a href='/Epipremnum-Aureum'>Previous</a>
          <br>         
            <hr>
            <h2>
                Menu
            </h2>
                <a href="{home_page}">Home</a>
                <a href="{about_us}">About Us</a>
                <a href="{collection}">Plant Collection</a>
                <a href="{subscribe}">Subscribe</a>
                <a href="{login}">Login</a>
                <a href="{admin}">Administrator Login</a>
            <hr>
            <h8>
                copyright Plantify ltd
            </h8>
        </body>
    </html> 
    """


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
@app.route('/login')  # ROUTE TO CUSTOMER LOGIN PAGE
def customer_login_url():
    home_page = url_for('homepage_url')
    about_us = url_for('about_us_url')
    collection = url_for('collection_url')
    subscribe = url_for('subscribe_url')
    admin = url_for('admin_login_url')
    return f"""
        <!doctype>
        <html>
            <head>
                <title>Login</title>
                <link rel="stylesheet" href="{url_for('static', filename='style.css')}">
            </head>
            <body>
                <h1>
                    Plantify
                </h1>
                    <!DOCTYPE html>
                    <html lang="en">
                    <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <title>Login Form</title>
                    </head>
                    <body>
                        <div class="login-container">
                            <h2>Login</h2>
                            <form action="/login" method="post">
                                <input type="text" name="username" placeholder="Username" required>
                                <input type="password" name="password" placeholder="Password" required>
                                <input type="submit" value="Login">
                            </form>
                        </div>
                    </body>
                    </html>

                    Not a member? Create your free account 
                    <a href="{subscribe}">here.</a>
                </p>
                <hr>
                <h2>
                    Menu
                </h2>
                    <a href="{home_page}">Home</a>
                    <a href="{about_us}">About Us</a>
                    <a href="{collection}">Collection</a>
                    <a href="{subscribe}">Subscribe</a>
                    <b>Login</b>
                    <a href="{admin}">Administrator Login</a>
                <hr>
                <h8>
                    copyright Plantify ltd
                </h8>
            </body>
        </html> 
        """


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