from flask import Flask, render_template, request, jsonify, session, redirect
import config
import uuid
import time
from flask_session import Session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_cors import CORS 

from icecream import ic
ic.configureOutput(prefix=f'_________ | ', includeContext=True)

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

CORS(app, origins=["http://localhost:3000"])

##############################
@app.route("/")
def show_index():
    return render_template("index.html")


####################################################
#######################____APIs___##################
####################################################

@app.post("/api-get-name") #use dashes for url
def api_get_name():
    name = "Kat" #This comes from the database
    data = {"name":name} #dictionary aka json
    return jsonify(data)