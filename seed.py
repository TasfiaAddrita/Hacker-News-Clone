import config
from model import Users, Posts, Comments

config.db.drop_all()
config.db.create_all()

user_one = Users('taddrita', 'pass')
user_two = Users('julissa', 'pass')
user_three = Users('jason', 'pass')

post_one = Posts(**{
    'user_id': 1,
    'title': 'Programming as a Way of Thinking',
    'url': 'https://blogs.scientificamerican.com/guest-blog/programming-as-a-way-of-thinking/'
})
post_two = Posts(**{
    'user_id': 2,
    'title': 'Ask HN: Who is Hiring? (May 2017)',
    'text': 'Please lead with the location of the position and include the keywords REMOTE, INTERNS and/or VISA when the corresponding sort of candidate is welcome. When remote work is not an option, please include ONSITE. A one-sentence summary of your interview process would also be helpful.'
})
post_three = Posts(**{
    'user_id': 3,
    'title': 'Facebook',
    'url': 'https://www.facebook.com/'
})
post_four = Posts(**{
    'user_id': 1,
    'title': 'Reddit',
    'url': 'https://www.reddit.com/'
})

config.db.session.add(user_one)
config.db.session.add(user_two)

config.db.session.add(post_one)
config.db.session.add(post_two)
config.db.session.add(post_three)
config.db.session.add(post_four)

config.db.session.commit()
