import os
import pathlib as p
from markupsafe import Markup
from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)
from flashApp.db import get_db

bp = Blueprint('view', __name__)


@bp.route('/flash/<int:id>')
def view(id):
    db = get_db()
    rows = db.execute(
        '''SELECT swf.id, swf.title,swf.desc,swf.filepath, swf.thumbnail, swf.filename,authors.author_name FROM swf
        JOIN works ON swf.id=works.swf_id 
        JOIN authors ON works.author_id=authors.id
        WHERE swf.id=?''', (str(id),)
    ).fetchone()
    fullpath = p.Path(rows['filepath']).joinpath(rows['filename']).as_posix()
    print(fullpath)
    if rows==None:
        abort(404)
    else:
        return render_template('view.html', row=rows, path=Markup(fullpath))