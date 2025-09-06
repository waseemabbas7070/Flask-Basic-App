from flask import Flask

app = Flask(__name__)

# URL Bindings
@app.route('/')
def home():
    return "Welcome to the Home Page!"

@app.route('/about')
def about():
    return "About Us Page"

@app.route('/contact')
def contact():
    return "Contact Us Page"

@app.route('/services')
def services():
    return "Our Services Page"

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
    # app.run(port=8000)
