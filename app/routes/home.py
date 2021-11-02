from flask import Blueprint, render_template

# equivalent to an express router
bp = Blueprint('home', __name__, url_prefix='/')

# @bp.route decorator turns the following function into a route
@bp.route('/')
# whatever the function returns becomes the response - here we're using render template to respond with a template
def index():
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

@bp.route('/post/<id>')
# to capture the value of the id we have to include it as a function parameter
def single(id):
  return render_template('single-post.html')