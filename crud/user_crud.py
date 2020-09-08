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

