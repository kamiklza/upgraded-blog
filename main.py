from flask import Flask, render_template

app = Flask(__name__)
print(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about_section():
    return render_template('about.html')

@app.route('/contact')
def contact_section():
    return render_template('contact.html')



if __name__ == "__main__":
    app.run(debug=True)
