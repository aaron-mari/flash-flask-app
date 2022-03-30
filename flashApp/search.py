from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, abort
)
from flashApp.db import get_db
from pprint import pprint as p
bp = Blueprint('search', __name__)

@bp.route("/search", methods=('GET',))
def search():
	term = ''
	if request.method == 'GET':
		term = request.args.get('term','')
	else:
		redirect(url_for('home'))
	db = get_db()
	results = db.execute('''
	SELECT swf.id, swf.title, authors.author_name, swf.thumbnail, swf.filepath
	FROM swf, authors JOIN works ON swf_id=swf.id AND author_id=authors.id
	WHERE title LIKE ? OR author_name LIKE ?;
	''', ("%"+term+"%", "%"+term+"%")).fetchall()
	return render_template('search.html', search_term=term, results=results)
