from flask import Flask, render_template, flash
from wtforms import Form, BooleanField, TextField, PasswordField, validators


app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
	return render_template('index.html')

@app.route("/superman")
def superman():
    return render_template('superman.html')

@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/recipesideas")
def recipesideas():
    return render_template('recipesideas.html')

@app.route("/instagramsuggestions")
def instagramsuggestions():
    return render_template('instagramsuggestions.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
	class RegistrationForm(Form):
		First_Name= TextField('First Name', [validators.Length(min=1, max=20)])
		Last_Name= TextField('Last Name', [validators.Length(min=1, max=20)])
		Username = TextField('Username', [validators.Length(min=4, max=20)])
    	Email = TextField('Email Address', [validators.Length(min=6, max=50)])
    	Password = PasswordField('New Password', [validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')])
    	confirm = PasswordField('Repeat Passowrd')

     	accept_tos = BooleanField('I accept the <a href="/tos/"> Terms of Service<a/> and the<a href="/Privacy/"> Privacy Notice<a/> (updated Jan 01, 2018)', [validators.Required()])
     	return render_template('signup.html')

"""@app.route('/signup3', methods=['GET', 'POST'])
def signup():
	try:
		form = RegistrationForm(request.form)
		if request.method == "POST" and form.validate():
            		Username = form.Username.data()
            		Email = form.Email.data()
			flash('Thanks for registration ' + First_Name) 
		else:
      			flash('Error: All the form fields are required. ')
		return render_template('signup.html')
	except:
		pass
"""
if __name__ == '__main__': 
	app.run(debug=True)