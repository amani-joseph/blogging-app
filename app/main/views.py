from email import message
from flask import render_template, request, redirect, url_for, abort
from ..request import get_quote
from . import main
from .forms import UpdateProfile,BlogForm,CommentForm
from ..models import User,Blog,Comment,Upvote,Downvote
from flask_login import login_required, current_user



@main.route('/')
def index():
    blogs = Blog.query.all()
    random_quote = get_quote()
    
    return render_template('index.html', posts=blogs, quote=random_quote)


@main.route('/about/')
def about():
    message = "This is the about page"
    return render_template('about.html', title='About', message=message)


@main.route('/blog/<int:blog_id>', methods = ['GET'])

def blog(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
   
    return render_template('blog.html', blog = blog,all_comments=all_comments)

@main.route('/comment/<int:blog_id>', methods = ['POST','GET'])
@login_required
def comment(blog_id):
    form = CommentForm()
    blog = Blog.query.get(blog_id)
    all_comments = Comment.query.filter_by(blog_id = blog_id).all()
    if form.validate_on_submit():
        comment = form.comment.data 
        blog_id = blog_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,blog_id = blog_id)
        new_comment.save_c()
        return redirect(url_for('.comment', blog_id = blog_id))
    return render_template('comment.html', form =form, blog = blog,all_comments=all_comments)



@main.route('/create_new', methods = ['POST','GET'])
@login_required
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        title = form.title.data
        post = form.content.data
        user_id = current_user
        new_blog_object = Blog(post=post,user_id=current_user._get_current_object().id,title=title)
        new_blog_object.save_p()
        return redirect(url_for('main.index'))
        
    return render_template('new_blog.html', form = form)


@main.route('/user/<name>')
def profile(name):
    user = User.query.filter_by(username = name).first()
    user_id = current_user._get_current_object().id
    posts = Blog.query.filter_by(user_id = user_id).all()
    image = url_for('static', filename='photos/' + current_user.profile_pic_path)
    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts, image=image)


@main.route('/user/<name>/updateprofile', methods = ['POST','GET'])
@login_required
def updateprofile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username = name).first()
    if user == None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save_u()
        return redirect(url_for('.profile',name = name))
    return render_template('profile/update.html',form =form)


@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',name=name))

@main.route('/like/<int:id>',methods = ['POST','GET'])
@login_required
def like(id):
    get_blogs = Upvote.get_upvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in get_blogs:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_vote = Upvote(user = current_user, blog_id=id)
    new_vote.save()
    return redirect(url_for('main.index',id=id))

@main.route('/dislike/<int:id>',methods = ['POST','GET'])
@login_required
def dislike(id):
    blog = Downvote.get_downvotes(id)
    valid_string = f'{current_user.id}:{id}'
    for p in blog:
        to_str = f'{p}'
        print(valid_string+" "+to_str)
        if valid_string == to_str:
            return redirect(url_for('main.index',id=id))
        else:
            continue
    new_downvote = Downvote(user = current_user, blog_id=id)
    new_downvote.save()
    return redirect(url_for('main.index',id = id))
