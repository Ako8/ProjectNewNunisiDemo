from flask import render_template, current_app as app


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/blog')
def blog():
    return render_template('blog.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/room')
def room():
    return render_template('room.html')


@app.route('/single-blog')
def single_blog():
    return render_template('single-blog.html')


@app.route('/single-room')
def single_room():
    return render_template('single-room.html')
