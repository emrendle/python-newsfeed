from flask import Flask
# importing home directly from the routes package because the init file imported and renamed blueprint
from app.routes import home, dashboard

def create_app(test_config=None):
  # set up app config
  app = Flask(__name__, static_url_path='/')
  app.url_map.strict_slashes = False
  app.config.from_mapping(
    SECRET_KEY='super_secret_key'
  )

  @app.route('/hello')
  def hello():
    return 'hello world'
  
  app.register_blueprint(home)
  app.register_blueprint(dashboard)
  
  return app