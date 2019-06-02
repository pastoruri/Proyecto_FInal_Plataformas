from flask import Flask, render_template, url_for
app = Flask(__name__)

posts=[
    {
        'author':'Rodrigo Cespedes',
        'title': 'Blog post 1',
        'content' : 'First post content',
        'date_posted' : 'June 2, 2019'
    },
    {
        'author':'Gabriel Spranger',
        'title': 'Blog post 2',
        'content' : 'Second post content',
        'date_posted' : 'June 3, 2019'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


if __name__=='__main__':
    app.run(debug=True)