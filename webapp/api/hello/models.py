import datetime

from webapp import db    

class Greeting(db.Model):
    __tablename__ = 'greetings'
    id = db.Column(db.Integer(), primary_key=True)
    greeting = db.Column(db.Text(), nullable=False)
    greeted_by = db.Column(db.String(255), nullable=False)
    created_on = db.Column(db.DateTime(), default=datetime.datetime.now)

    def __init__(self, greeting, greeted_by):
        self.greeting = greeting
        self.greeted_by = greeted_by

    def __repr__(self):
        return f'<Greeting: {self.id}>'