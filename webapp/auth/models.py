from webapp import db 
from flask_login import AnonymousUserMixin
from . import bcrypt  

roles = db.Table(
    'role_users',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id')),
    db.Column('role_id', db.Integer, db.ForeignKey('user_roles.id')),
)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255), nullable=False, index=True, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    password = db.Column(db.String(255))

    roles = db.relationship('Role', secondary=roles,
        backref=db.backref('users', lazy='dynamic'))

    def __init__(self, username):
        self.username = username    

    def __repr__(self):
        return f'<User: {self.username}'

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    def has_role(self, name):
        for role in self.roles:
            if role.name == name:
                return True 
        return False

    @property
    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    @property
    def is_active(self):
        return True


class Role(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, name):
        self.name = name 

    def __repr__(self):
        return f"<Role: {self.name}>"