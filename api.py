from models import app, User
from flask import jsonify
from crud.user_crud import get_all_users, get_user 

@app.route('/')
def home():
  first_user = User.query.first()
  print(f'🎀 {first_user}')
  return jsonify(user=first_user.as_dict())

#Routes 
@app.route('/users/')
def user_index_create(): 
    return get_all_users()

@app.route('/users/<int:id>')
def user_show_put_delete(id):
    return get_user(id)

#error handler 
@app.errorhandler(Exception) 
def unhandeled_error(e):
    app.logger.error('Unhandeled Exception: %s' , (e))
    message_str = e.__str__()
    return jsonify(message=message_str.split(':')[0])