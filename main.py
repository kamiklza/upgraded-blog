from flask import Flask, render_template, request
import requests
import smtplib
import os

username = os.environ["GMAIL_USERNAME"]
password = os.environ["GMAIL_PASSWORD"]

response = requests.get(url="https://api.npoint.io/a28614a95d2bdf0666ea")
data = response.json()

class Blog:
    def __init__(self, post_id, body, title, subtitle, author, date):
        self.id = post_id
        self.body = body
        self.title = title
        self.subtitle = subtitle
        self.author = author
        self.date = date

all_posts = []
for post in data:
    blog_post = Blog(post.get('id'), post.get('body'), post.get('title'), post.get('subtitle'), post.get('author'), post.get('date'))
    all_posts.append(blog_post)

print(all_posts)
print(all_posts[0].body)





app = Flask(__name__)



@app.route('/')
def home():
    return render_template('index.html', all_posts=all_posts)

@app.route('/about')
def about_section():
    return render_template('about.html')

@app.route('/contact', methods=["GET", "POST"])
def contact_section():
    if request.method == 'POST':
        data = request.form
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(from_addr="kamiklza@gmail.com", to_addrs="kamiklza@hotmail.com", msg=f"Subject: Fans message\n\n Name: {data['name']}\n\n"
                                                                                                 f"Email: {data['email']}\n\n"
                                                                                                 f"Phone: {data['phone']}\n\n"
                                                                                                 f"Message: {data['message']}")
        connection.close()
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

@app.route('/post/<int:index>')
def blog_post(index):
    for blog in all_posts:
        if index == blog.id:
            title = blog.title
            subtitle = blog.subtitle
            body = blog.body
            author = blog.author
            date = blog.date
    return render_template('post.html', title=title, subtitle=subtitle, body=body, author=author, date=date)

# @app.route('/form-entry', methods=['POST'])
# def receive_data():
#     received = True
#     return render_template('contact.html', receive=received)


if __name__ == "__main__":
    app.run(debug=True)
