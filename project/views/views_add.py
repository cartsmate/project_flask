from project import app


@app.route('/add')
def add():
    return 'hello ADD index world!'
