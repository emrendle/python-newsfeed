from flask import Blueprint, render_template

# when we use the url_prefix argument we prefix every route in the blueprint with /dashboard
# every route here becomes '/dashboard/' and '/dashboard/edit/<id>'
bp = Blueprint('dashboard', __name__, url_prefix='/dashboard')

@bp.route('/')
def dash():
  return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
  return render_template('edit-post.html')