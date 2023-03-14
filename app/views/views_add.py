from flask import render_template
from app import app


@app.route('/add')
def add():
    return render_template('add.html')
