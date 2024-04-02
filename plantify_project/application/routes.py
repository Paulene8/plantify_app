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
def homepage():
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


# created a blog post route
# created the function for the customer blog url
# printed the initial requests method to check
# if statement to check if the method is a post, if it is we define the property in the session object called username
# assign it to the username that we get from the request form
# print out the session username to confirm that it has been assigned
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
    postlist = get_blogpost()
    # posts = db.execute(
    #     'SELECT title, post, date, username'
    #     'ORDER BY created DESC'
    # ).fetchall()
    return render_template('getblog.html', title='Blogposts', posts=postlist)


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
            blogposts.append({'Username': user_name, 'title': title, 'Post': post})
            add_blogpost(user_name, title, post)
            return redirect(url_for('submit'))

    return render_template('custom_login.html', form=register_form, title='Submit a Blog Post', message=error)



# RUN FLASK APP
if __name__ == "__main__":
    app.run(debug=True)