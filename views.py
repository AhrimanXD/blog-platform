from flask import Flask, render_template, Blueprint, request, redirect, url_for,session,flash
from models import db, Post

#Create a Blueprint for views
views = Blueprint("views", __name__)


@views.route('/')
def home():
    posts = Post.query.all()
    return render_template("home.html", posts = posts)

@views.route("/post/<int:post_id>")
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template("post.html", post=post)

@views.route("/new_post", methods=["GET", "POST"])
def new_post():
    if "user_id" not in session:
        flash("You must be logged in to create a post.", "danger")
        return redirect(url_for("auth.login"))
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        new_post = Post(title=title, content = content,author_id=1)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for("views.home"))
    return render_template("new_post.html")

@views.route("/edit_post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == "POST":
        post.title = request.form["title"]
        post.content = request.form["content"]
        db.session.commit()
        return redirect(url_for("views.view_post", post_id=post.id))
    return render_template("edit_post.html",post=post)

@views.route("/delete_post/<int:post_id>", methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("views.home"))
