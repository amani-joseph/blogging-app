'''Basic User model without a one to many relationship'''
# from . import db


# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key = True)
#     username = db.Column(db.String(255),unique = True,nullable = False)
#     email  = db.Column(db.String(255),unique = True,nullable = False)
#     secure_password = db.Column(db.String(255),nullable = False)
#     bio = db.Column(db.String(255))
    