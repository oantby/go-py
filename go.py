#!/usr/bin/env python

from flask import Flask, redirect, abort
import MySQLdb

db = MySQLdb.connect(user='go', passwd="the go password",db="go", host='127.0.0.1')
app = Flask(__name__)

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