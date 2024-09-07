from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get('https://api.npoint.io/c790b4d5cab58020d391')
blog_data = response.json()

@app.route('/')
def home():
    return render_template("index.html",blog_data = blog_data)

@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html',blog_data = blog_data,id=id)

if __name__ == "__main__":
    app.run(debug=True)
