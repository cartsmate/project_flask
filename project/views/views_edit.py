from flask import render_template
from project import app


@app.route('/edit')
def edit():
    return render_template('edit.html')
