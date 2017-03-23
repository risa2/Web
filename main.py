import flask

app=flask.Flask(__name__)

@app.route('/')
def form():
    return flask.render_template('form.html')

@app.route('/calc_input', methods=['POST'])
def answer():
    if flask.request.form['o']=='+':
        return str(flask.request.form['a']+flask.request.form['b'])
    elif flask.request.form['o']=='-':
        return str(flask.request.form['a']-flask.request.form['b'])
    elif flask.request.form['o']=='*':
        return str(flask.request.form['a']*flask.request.form['b'])
    elif flask.request.form['o']=='/':
        return str(flask.request.form['a']/flask.request.form['b'])
