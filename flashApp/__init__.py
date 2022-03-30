import os

from flask import Flask
from flask import abort, url_for, redirect, render_template


def create_app(test_config=None):
    #create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get("APP_KEY"),
        DATABASE=os.path.join(app.instance_path, 'flashApp.sqlite')
    )
    if test_config is None:
        #load instance config
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    from . import db
    db.init_app(app) 

    @app.route('/')
    def home():
        f_db = db.get_db()
        rows = f_db.execute("""
        SELECT * FROM swf
        """).fetchall()
        return render_template('home.html', rows=rows)

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('404.html'), 404

    from . import view, search
    app.register_blueprint(view.bp)
    app.register_blueprint(search.bp)
    app.add_url_rule('/', endpoint='home')


    return app