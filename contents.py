from flask import Flask, render_template
app = Flask(__name__)

@app.route("")
@app.route("/index.html")
def index():
	return render_template('index.html')

@app.route("/superman.html")
def superman():
    return render_template('superman.html')

@app.route("/home.html")
def home():
    return render_template('home.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/recipesideas.html")
def recipesideas():
    return render_template('recipesideas.html')

@app.route("/instagramsuggestions.html")
def instagramsuggestions():
    return render_template('instagramsuggestions.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
  