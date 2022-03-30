import sqlite3

import click
from flask import current_app, g, url_for
from flask.cli import with_appcontext

import pathlib as p

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    return g.db

def close_db(e=None):
    db = g.pop('db', None)
    if db is not None:
        db.close()

def init_db():
    db = get_db()
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))

    flash_path = p.Path(current_app.static_folder + '/flash')
    swfs = []
    for a_folder in flash_path.iterdir():
        if a_folder.is_dir():
            f_id = db.execute("SELECT id FROM authors WHERE author_name=?", (a_folder.name,)).fetchone()
            if f_id == None:
                db.execute('INSERT INTO authors VALUES(NULL,?)', (a_folder.name,))
                f_id = db.execute("SELECT id FROM authors WHERE author_name=?", (a_folder.name,)).fetchone()
            for w_folder in a_folder.iterdir():
                swf_path = w_folder.relative_to(current_app.static_folder)
                print(swf_path)
                swf_title = w_folder.name
                swf_file = sorted(w_folder.glob("*.swf"))
                swf_file = swf_file[0].name
                thumbnail = sorted(w_folder.glob("thumbnail.*"))
                if len(thumbnail) !=0:
                    thumbnail = thumbnail[0].name
                else:
                    thumbnail = None
                db.execute('INSERT INTO swf("title", "filepath", "filename", "thumbnail") VALUES(?,?,?,?)', (swf_title,str(swf_path), swf_file,thumbnail))

                swf_id = db.execute('SELECT id FROM swf WHERE title=?;', (swf_title,)).fetchone()
                db.execute('INSERT INTO works(swf_id, author_id) VALUES(?,?)', (swf_id[0], f_id[0]))
    db.commit()
                
                

@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized database.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
    