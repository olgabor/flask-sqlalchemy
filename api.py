from models import app, User
from flask import jsonify

@app.route('/')
def home():
  first_user = User.query.first()
  print(f'🎀 {first_user}')
  return jsonify(user=first_user.as_dict())


