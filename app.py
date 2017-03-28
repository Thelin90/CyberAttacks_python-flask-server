# Author: Simon Thelin
# version: 1.2
# date: 2017-03-10

# -*- coding: utf-8 -*-
import pyorient
# render_template is used for showing html in this application, not used here, jsonify to parse the
# fetch and return it in a json format
from flask import Flask, render_template, jsonify
#Allow cross-origin resource sharing (CORS)
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

data_to_json = []

client = pyorient.OrientDB("localhost", 2424)
client.set_session_token(True)
client.connect("user_root", "your_root_pass")
client.db_open("CyberAttacks", "db_user", "db_pass")

loop = (client.command("select * from Domain ORDER BY @rid ASC LIMIT 20"))

for result in loop:
    data_to_json.append({'Domain': result.Domain, 'AuthProtocol': result.AuthProtocol, 'LogonType':result.LogonType, 'Destination': result.Destination,'Source': result.Source,'User': result.User,'DateTime': result.DateTime, 'LogFile': result.LogFile, 'Type': result.Type, 'EventID': result.EventID})

print(data_to_json)

@app.route("/getData")
def index():
    return jsonify(data_to_json)

if __name__ == "__main__":
    app.run()
