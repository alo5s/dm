from flask import Flask, redirect, url_for, render_template

app = Flask('__name__')


@app.route('/')
def redic():
    return redirect(url_for('login'))



@app.route('/home')
def home():
    return render_template('cosa.html')

@app.route('/tablas')
def tablas():
    return render_template('tablas.html')

@app.route('/opcion')
def opcion():
    return render_template('opcion.html')


@app.route('/login',  methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')




if __name__=='__main__':
    app.run(host='127.0.0.1', port=8000, debug=True )