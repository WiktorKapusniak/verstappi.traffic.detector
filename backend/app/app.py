from flask import Flask, jsonify, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/message', methods=['GET'])
def message():
    return jsonify({"message": "Don't honk in the woods"}), 200

@app.route('/login',methods=['POST'])
def login():
    if(request.args.get("username")=="Admin") and (request.args.get("password")=="12345"):
        return jsonify({"message":"Witaj, "+request.args.get("username"),"AccessLevel":"Admin"})
    elif(request.args.get("username")=="User") and (request.args.get("password")=="12345"):
        return jsonify({"message":"Witaj, "+request.args.get("username"),"AccessLevel":"User"})
    else:
        return jsonify({"message":"Nieprawidlowy login lub haslo"})

@app.route('/getUserData', methods=['GET'])
def getUserData():
    return jsonify({"AccessLevel":"User","Username":"Jelen"})

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

