from flask import Flask, render_template, request, make_response, jsonify
import werkzeug
import bcrypt
import json
import re

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/user")
def user():
    return readJson()

@app.route("/user/<int:user_id>")
def userById(user_id):
    data = parseJson()
    user = findUser(user_id, data)

    if user != False:
        return jsonify(user)
    else:
        return jsonify({"Error":"user not found"})    

@app.route("/save", methods=['POST'])
def clientSave():
    data = parseJson()

    if str(request.form['user_id']).isdigit == True:
        for user in data['users']:
            if str(user['id']) == str(request.form['user_id']):
                user['username'] = request.form['username']
                user['email'] = request.form['email']
                user['id'] = request.form['user_id']
    else:
        if request.form['user_id'] != '':
            id = request.form['user_id']
        else:
            id = len(data['users']) + 1

        newUser = {
            "username": request.form['username'],
            "email": request.form['email'],
            "id": id
        }
        data['users'].append(newUser)

    writeJson(data)

    return jsonify({"message":'User data saved!'})

@app.route("/reset")
def reset():
    b = open('data/backup.json', 'r')
    backup = b.read()

    u = open('data/users.json', 'w')
    u.write(backup)

    return jsonify({"message":'User data reset!'})

##################################
## Helper functions
def readJson():
    f = open('data/users.json', 'r')
    contents = f.read()
    contents = re.sub('\s{3,}','', contents.strip())
    return contents

def parseJson():
    f = open('data/users.json', 'r')
    contents = f.read()
    data = {"users":[]}

    result = re.match('\{"users":\[(.+?)\]\}', contents, flags=re.MULTILINE|re.DOTALL)
    group = result.group(1)
    result = group[1:len(group) - 1]
    split = result.split('},{')

    for item in split:
        item = re.sub('\s{3,}','', item.strip())

        u = re.search('"username":"(.+?)"', item, flags=re.MULTILINE|re.DOTALL)
        e = re.search('"email":"(.+?)"', item, flags=re.MULTILINE|re.DOTALL)
        i = re.search('"id":(.+?)$', item, flags=re.MULTILINE|re.DOTALL)
        
        user = {
            "id": int(i.group(1)),
            "email": e.group(1),
            "username": u.group(1)
        }
        data['users'].append(user)

    return data

def writeJson(data):
    json = '{"users":['
    for user in data['users']:
        json += """{
            "username":"%s",
            "email":"%s",
            "id":%s
},""" % (user['username'], user['email'], user['id'])
    # Remove the last character so we don't get an extra comma
    json = json[0:len(json) - 1]
    json += ']}'

    with open('data/users.json', 'w') as f:
        f.write(json)

    return True

def findUser(user_id, data):
    for user in data['users']:
        if user['id'] == user_id:
            return user
    
    return False