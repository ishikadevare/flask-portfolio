from flask import Flask, render_template, request

app = Flask(__name__)

# Home page
@app.route('/')
def home():
    return render_template('index.html')

# About page
@app.route('/about')
def about():
    return render_template('about.html')

# Contact page
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # process the form data
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # render the contact template with success message
        return render_template('contact.html', success=True)
    else:
        # render the contact template with failure message
        return render_template('contact.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)
