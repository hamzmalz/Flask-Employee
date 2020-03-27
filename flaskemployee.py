from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from form import RegistrationForm, PunchInForm, PunchOutForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'password'
app.config['SQL_DATABASE_URI'] = '_sqlite:///site.db'
db = SQLAlchemy(app)


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.Integer, unique=True, nullable=False)
    hourly = db.Column(db.Integer, unique=True, nullable=False)
    work = db.relationship('Work', backref='employee', lazy=True)

    def __repr__(self):
        return f"Name('{self.name}', '{self.hourly}')"


class Work(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    time_in = db.Column(db.Integer, unique=True, nullable=False)
    time_out = db.Column(db.Integer, unique=True, nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'),
                            nullable=False)

    def __repr__(self):
        return f"Name('{self.time_in}', '{self.time_out}')"               


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/punch_in", methods=['GET', 'POST'])
def punch_in():
    form = PunchInForm()
    if form.validate_on_submit():
        flash(f'{form.name.data} has been punched in')
        return redirect(url_for('punch_in'))
    return render_template('punch_in.html', form=form)


@app.route("/punch_out", methods=['GET', 'POST'])
def punch_out():
    form = PunchOutForm()
    if form.validate_on_submit():
        flash(f'{form.name.data} has been punched out')
        return redirect(url_for('punch_out'))
    return render_template('punch_out.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'{form.name.data} has been registered')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
