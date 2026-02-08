from flask  import Flask,jsonify,request
from appdb import Users,Usersdb

app = Flask(__name__)

users_instance = Usersdb()

@app.route('/',methods=['GET'])
def viewusers():
    view_list = users_instance.view_users()
    if not view_list:
        return jsonify({'message':'list is empty'})
    return view_list
@app.route('/adduser',methods=['POST'])
def add_user():
    view_list = users_instance.view_users()
    data = request.get_json()
    name = data['name']
    email = data['email']

    if_match = next((v for v in view_list if v['email'] == email),None)

    if if_match:
        return jsonify({'message':'email is already used'}),400
    users_instance.add(name,email)
    return jsonify({'message':'added successfully'}),201

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=5000)
