from flask  import Flask,jsonify,request
from appdb import Users,Usersdb,Action
import os

app = Flask(__name__)

users_instance = Usersdb()
user_match = Action()

@app.route('/',methods=['GET'])
def viewusers():
    view_list = users_instance.view_users()
    if not view_list:
        return jsonify({'message':'list is empty'})
    return view_list
@app.route('/adduser',methods=['POST'])
def add_user():
    data = request.get_json()
    name = data['name']
    email = data['email']
    if_match = user_match.match_email(email)

    if if_match:
        return jsonify({'message':'email is already used'}),400
    users_instance.add(name,email)
    return jsonify({'message':'added successfully'}),201
@app.route('/updateuser',methods=['PUT'])
def update_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    id = data.get('id')

    if not id:
        return jsonify({'message':'input an id to update'}),400

    find_user = user_match.match(id)

    if find_user:
        users_instance.update(name, email, id)
        return jsonify({'message': 'update successfully'})

    return jsonify({'message':'id not match'}),400
@app.route('/deleteuser',methods=['DELETE'])
def delete_user():
    data = request.get_json()
    id = data.get('id')

    if not id:
        return jsonify({'message':'input an id to delete'}),400

    find_user = user_match.match(id)
    # print(find_user)
    if find_user:
        users_instance.delete(id)
        return jsonify({'message':'delete successfully'}),200

    return jsonify({'message':'id not found'}),404

print("Available routes:")
print(app.url_map)


if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))
    app.run(debug=False,host='0.0.0.0',port=port)
