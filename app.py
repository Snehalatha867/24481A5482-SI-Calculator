from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to Flask App => Routing"

@app.route('/greet/<uname>')
def greet(uname):
    return f"Good morning, {uname}"

@app.route('/delete/<int:roll>')
def delete_user(roll):
    return redirect(url_for('greet', uname=roll))

@app.route('/calculate', methods=['GET', 'POST'])
def Si():
    if request.method == 'POST':
        p = float(request.form['p'])
        r = float(request.form['r'])
        t = float(request.form['t'])

        si = (p * r * t) / 100
        total = p + si

        return render_template(
            'index.html',
            result=si,
            total=total,
            p=p,
            r=r,
            t=t
        )

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, port=3500)