from validate import validate
from flask import Flask, request, render_template, url_for, redirect, session, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import URL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'fj39as$9d@411Fe'

class URLForm(FlaskForm):
    url = StringField('Enter URL: ', validators=[URL()])
    submit = SubmitField("Go")

@app.route("/", methods=['GET','POST'])
def home():
    form = URLForm()

    if form.validate_on_submit():
        url = form.url.data
        response = validate(url)
        session['validateURL'] = url
        session['validateResponse'] = response
        return redirect(url_for('report')) #use redirect to avoid refresh/resubmit
    else:  
        if request.method == 'POST':
            flash('URL is invalid')  
            return redirect(url_for('home'))
        else:
            return render_template("home.html", form=form)

@app.route('/report')
def report():
    return render_template("report.html",url=session['validateURL'],response=session['validateResponse'])

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/contact/")
def contact():
    return render_template("contact.html")




