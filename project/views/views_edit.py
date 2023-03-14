from project import app


@app.route('/edit')
def edit():
    return 'hello EDIT index world!'
