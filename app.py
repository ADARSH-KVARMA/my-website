from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', title="Home")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="contact")

@app.route('/about')
def about():
    return render_template('about.html', title="About")

#rout for project
@app.route('/projects')
def project():
    return render_template('projects.html', title="Project")


if __name__ == '__main__':
    app.run(debug=True)