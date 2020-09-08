from models import app, User
from flask import jsonify, request
from crud.user_crud import get_all_users, get_user, create_user, update_user


@app.route('/')
def home():
  first_user = User.query.first()
  print(f'🎀 {first_user}')
  return jsonify(user=first_user.as_dict())

# User GET and POST Routes 
@app.route('/users/', methods=['GET', 'POST'])
def user_index_create(): 
    if request.method == 'GET':
        return get_all_users()
    if request.method == 'POST': 
        return create_user(**request.form)

#user GET, PUT, and DELETE routes 
@app.route('/users/<int:id>', methods=['GET', 'PUT'])
def user_show_put_delete(id):
    if request.method == 'GET':
        return get_user(id)
    if request.method == 'PUT': 
        return update_user(
                        id, 
                        name=request.form['name'], 
                        email=request.form['email'],
                        bio=request.form['bio'])

#error handler 
@app.errorhandler(Exception) 
def unhandeled_error(e):
    app.logger.error('Unhandeled Exception: %s' , (e))
    message_str = e.__str__()
    return jsonify(message=message_str.split(':')[0])