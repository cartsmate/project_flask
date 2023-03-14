from flask import render_template
from app import app


@app.route('/edit')
def edit():
    return render_template('edit.html')
