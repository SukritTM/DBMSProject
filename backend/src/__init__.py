import os 
from flask import Flask

def create_app(test_config=None):
    # create the app

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'src.sqlite')
    )

    if test_config is None:
        # load from instance file if exists
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load from test config when testing
        app.config.from_mapping(test_config)

    # ensure instance directory exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass
    
    from . import db
    db.init_app(app)
    
    # test page
    @app.route('/hello')
    def hello():
        return 'hello world'
    
    return app