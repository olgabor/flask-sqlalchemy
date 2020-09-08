from flask import jsonify, redirect
from models import db, User

#gets all users from DB and returns as JSON 
def get_all_users():
    all_users = User.query.all()
    results = [ user.as_dict() for user in all_users] # user is a temporary variable to use for list comprehension 
    return jsonify(results)

#gets a single user, by the ID and returns it as a JSON 
def get_user(id):
    user = User.query.get(id)
    if user: 
        return jsonify(user.as_dict()) 
    else: 
        raise Exception(f'Error getting user at ID {id}')

#create a user 
def create_user(**form_kwargs): 
    #new_user = User(name=name, email=email, bio=bio or None) # this is when passing name, email, bio as arguments in function 
    new_user = User(**form_kwargs)
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.as_dict())

def update_user(id, name, email, bio): 
    user = User.query.get(id)
    if user:
        user.name = name or user.name
        user.email = email or user.email
        user.bio = bio or user.bio
        db.session.commit()
        return jsonify(user.as_dict())
    else:
        raise Exception(f'No user at id {id}')


