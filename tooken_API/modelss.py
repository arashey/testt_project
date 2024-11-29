from peewee import *
import hashlib

db = SqliteDatabase('token.db')

class User(Model):
    username = CharField(max_length=100, primary_key=True)
    password = CharField()

    class Meta:
        database = db

db.create_tables([User], safe=True)

def hash_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

username_to_add = 'arash'
if User.get_or_none(User.username == username_to_add) is None:
    hashed_password = hash_password('1234')
    User.create(username=username_to_add, password=hashed_password)
    print(f'User {username_to_add} created')
else:
    print(f'User {username_to_add} already exists')