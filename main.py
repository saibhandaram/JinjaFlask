from flask import Flask, render_template, request
import requests

# Rendering Predefined JSON from npoint API
response = requests.get("https://api.npoint.io/2788e8816edaf3bf9fc3")
response.raise_for_status()
blog_posts = response.json()

app = Flask(__name__)


@app.route('/')
def get_homepage():
    return render_template("index.html", posts=blog_posts['next_steps'])


@app.route('/about.html')
def get_about():
    return render_template("about.html")


def send_email(param, param1, param2, param3):
    print(f"Name is {param}, email is {param1}, Phone is {param2} and Message is {param3}")




@app.route('/contact', methods=['POST', 'GET'])
def get_contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:num>')
def get_post(num):
    print(num)
    return render_template("blog.html", post=blog_posts['next_steps'][num])



if __name__ == "__main__":
    app.run(debug=True)
