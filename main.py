from flask import Flask, render_template
import requests

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

@app.route('/contact')
def contact_section():
    return render_template('contact.html')

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



if __name__ == "__main__":
    app.run(debug=True)
