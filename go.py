#!/usr/bin/env python

from os import environ
from flask import Flask, redirect, abort, render_template, request
import MySQLdb

def req_auth(func):
	def auth_wrapper(*args, **kwargs):
		if request.form.get('banana'):
			return func(*args, **kwargs)
		
		abort(403)
	return auth_wrapper

db = MySQLdb.connect(user=environ['DB_USER'], passwd=environ['DB_PASS'],
	db=environ['DB_NAME'], host=environ['DB_HOST'], autocommit=True)
app = Flask(__name__)

@app.route('/admin', methods=['GET', 'POST'])
@req_auth
def admin():
	
	return render_template('admin.html')

# prevent admin/anything from being added; that'd be too confusing.
@app.route('/admin/<path:garbage>')
def admin_placeholder(garbage):
	abort(404)

@app.route('/<path:path>')
def index(path):
	c = db.cursor()
	count = c.execute('SELECT `redirect` FROM `redirects` WHERE path = %s', (path,))
	if not count:
		c.close()
		abort(404)
	r = c.fetchone()
	c.close()
	if r is not None: return redirect(r[0])
	abort(500)