from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

