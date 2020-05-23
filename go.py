#!/usr/bin/env python

from os import environ
from flask import Flask, redirect, abort, render_template, request
import MySQLdb

db = MySQLdb.connect(user=environ['DB_USER'], passwd=environ['DB_PASS'],
	db=environ['DB_NAME'], host=environ['DB_HOST'], autocommit=True)
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