from flask import render_template, flash, redirect, session, url_for, request, g, jsonify
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    loginform=LoginForm()
    
    return render_template('splash.html', loginform=loginform)

