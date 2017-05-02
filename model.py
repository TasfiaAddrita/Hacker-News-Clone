from config import db
import datetime

class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    password = db.Column(db.String)
    karma = db.Column(db.Integer)
    account_created = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    posts = db.relationship('Posts')

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.karma = 1

class Posts(db.Model):
    __tablename__ = 'posts'
    post_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    title = db.Column(db.String)
    url = db.Column(db.String)
    text = db.Column(db.String)
    comments = db.relationship('Comments')

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.title = kwargs.get('title')
        self.url = kwargs.get('url', 'N/A')
        self.text = kwargs.get('text', 'N/A')

class Comments(db.Model):
    __tablename__ = 'comments'
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.post_id'))
    comment = db.Column(db.String)

    def __init__(self, **kwargs):
        self.user_id = kwargs.get('user_id')
        self.post_id = kwargs.get('post_id')
        self.comment = kwargs.get('comment')

def get_username(user_id):
    sql_username = Users.query.filter_by(user_id = user_id).first()
    print(sql_username)
    return sql_username.username

def get_all_posts():
    all_posts = []
    sql_posts = Posts.query.all()
    # print(sql_posts)

    for posts in sql_posts:
        post = {
            "username": get_username(posts.user_id),
            "title": posts.title,
            "url": posts.url,
            "text": posts.text
        }
        all_posts.append(post)

    return all_posts
