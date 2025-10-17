from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
import keycloak_config
app = Flask(__name__)
CORS(app)

@app.route('/message', methods=['GET'])
def message():
    return jsonify({"message": "Don't honk in the woods"}), 200

@app.route('/login',methods=['POST'])
def login():
    try:
        data = request.json()
        username = data.get("username")
        password = data.get("password")
        token = keycloak_config.keycloak_openid.token(username, password)
        user_id = keycloak_config.keycloak_admin.get_user_id(request.args.get("username"))
        realm_roles = keycloak_config.keycloak_admin.get_realm_roles_of_user(user_id)
        return jsonify({"message":"Witaj, "+request.args.get("username"),"AccessLevel":realm_roles[0],"token":token})
    except:
        return jsonify({"message":"Nieprawidlowy login lub haslo"})

@app.route('/getUserData', methods=['GET'])
def getUserData():
    print(keycloak_config.keycloak_openid.well_known())
    try:
        token = request.headers.get("Authorization").split(" ")[1]
        userinfo = keycloak_config.keycloak_openid.userinfo(token)
        return jsonify({"UserData":userinfo})
    except:
        return jsonify({"message":"Nieprawidlowy token"})

@app.route('/getDBData',methods=["GET"])
def getDayData():
    return jsonify({"DBData":"TODO"})

@app.route('/getCameraImage',methods=['GET'])
def getCameraImage():
    return jsonify({"CamImage":"TODO"})

@app.route('/dhitw',methods=['GET'])
def dhitw():
    return send_file("./public/sarnaLICENCJAT.png", mimetype='image/png')

if __name__ == '__main__':
    app.run(port=5000)

