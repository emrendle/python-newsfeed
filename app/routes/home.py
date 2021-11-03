from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

# equivalent to an express router
bp = Blueprint('home', __name__, url_prefix='/')

# @bp.route decorator turns the following function into a route
@bp.route('/')
# whatever the function returns becomes the response - here we're using render template to respond with a template
def index():
  # get all posts
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all()
  return render_template(
    'homepage.html',
    posts=posts
)

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
# to capture the value of the id we have to include it as a function parameter
def single(id):
  # get single post by id
  db = get_db()
  # using the filter() method on the connection object to specify the WHERE clause
  # using the one() method instead of all()
  post = db.query(Post).filter(Post.id == id).one()
  # render single post template
  return render_template(
    'single-post.html',
    post=post
  )