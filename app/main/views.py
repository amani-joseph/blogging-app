# from turtle import title
from email import message
from flask import render_template, request, redirect, url_for, abort
from . import main
# from .forms import exampleForm
from flask_login import login_required, current_user

posts = [
    {
        'author': 'Amani',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'March 12, 2022'
    },
    {
        'author': 'Joe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'March 12, 2022'
    }
]

@main.route('/')
def index():
    message = 'Hello Amani'
    return render_template('index.html', message=message, posts=posts)


@main.route('/about/')
def about():
    message = "This is the about page"
    return render_template('about.html', title='About', message=message)
