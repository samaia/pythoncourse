from flask import Flask, render_template
app = Flask(__name__)

@app.route("https://immense-ridge-70695.herokuapp.com/")
@app.route("https://immense-ridge-70695.herokuapp.com/index.html")
def index():
	return render_template('index.html')

@app.route("https://immense-ridge-70695.herokuapp.com/superman.html")
def superman():
    return render_template('superman.html')

@app.route("https://immense-ridge-70695.herokuapp.com/home.html")
def home():
    return render_template('home.html')

@app.route("https://immense-ridge-70695.herokuapp.com/about.html")
def about():
    return render_template('about.html')

@app.route("https://immense-ridge-70695.herokuapp.com/recipesideas.html")
def recipesideas():
    return render_template('recipesideas.html')

@app.route("https://immense-ridge-70695.herokuapp.com/instagramsuggestions.html")
def instagramsuggestions():
    return render_template('instagramsuggestions.html')

@app.route("https://immense-ridge-70695.herokuapp.com/contact.html")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
  