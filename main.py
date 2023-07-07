from flask import Flask, render_template
import requests

# Rendering Predefined JSON from npoint API
response = requests.get("https://api.npoint.io/2788e8816edaf3bf9fc3")
response.raise_for_status()
blog_posts = response.json()

app = Flask(__name__)


@app.route('/')
def get_blogs():
    print(blog_posts)
    return render_template("post.html", posts=blog_posts['next_steps'])


@app.route('/post/<int:num>')
def get_post(num):
    print(num)
    return render_template("blog.html", post=blog_posts['next_steps'][num])


if __name__ == "__main__":
    app.run(debug=True)
