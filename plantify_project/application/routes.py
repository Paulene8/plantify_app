from flask import Flask, Response, request, render_template, session, url_for
from plantify_project.application.forms.register_form import RegisterForm
from plantify_project.application.data_access import add_blogpost, get_blogpost
from plantify_project.application.forms.register_form import RegisterForm
from plantify_project.application.data_access import add_blogpost, get_blogpost
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


@app.route('/collection')
def collection():
    return render_template('collection.html', title='Product Collection')

# INDIVIDUAL PLANT INFO PAGES
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

# SUPPOSED TO DISPLAY THE HISTORICAL POSTS
@app.route('/blogposts')
def blogposts():
    db = get_blogpost()   # TO DO: CREATE BLOGPOSTDB. COLS: POST ID (p.id), TITLE, USERNAME, POST, DATE (?)
    posts = db.execute(
        'SELECT p.id, title, post, date, username'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('getblog.html', title='Blogposts')


@app.route('/submit_post', methods=['GET', 'POST'])
def submit():
    error = ""
    register_form = RegisterForm()

    if request.method == 'POST':
        user_name = register_form.user_name.data
        title = register_form.title.data
        post = register_form.post.data

        if len(user_name) == 0 or len(title) == 0 or len(post) == 0:
            error = 'Please complete the form in full'

        else:
            blogpost.append({'Username': user_name, 'Title': title, 'Post': post})
            add_blogpost(user_name, title, post)
            return redirect(url_for('submit'))

    return render_template('custom_login.html', form=register_form, title='Submit a Blog Post', message=error)



# RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=True)