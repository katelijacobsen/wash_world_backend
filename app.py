from flask import Flask, render_template, request, jsonify, session, redirect
import config
import uuid
import time
from flask_session import Session
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_cors import CORS 

from icecream import ic
ic.configureOutput(prefix=f'______________ | ', includeContext=True)

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# CORS(app, origins=["http://localhost:3000"])

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



#______LOGIN_____##################################
 
@app.post("/login")
def login():
    try:
        #TODO Validate data 
        user_email = config.validate_user_email(request.form.get("user_email", "").strip()) 
        user_password = request.form.get("user_password", "").strip()        
        
        db, cursor = config.db()
        
        
        q = "SELECT * FROM users WHERE user_email = %s"
        
        cursor.execute(q, (user_email,))
        user = cursor.fetchone()
        
        if not user: 
            data = {"status" : "!ok", "role" : "unknown"}
            return jsonify(data)
        
        if not user_password == user["user_password"]:
            raise Exception("Invalid credentials 02")
        
        if "@a" in user_email:
            data = {"status" : "ok", "role" : "user"}
            return jsonify(data)
        if "@b" in user_email:
            data = {"status" : "ok", "role" : "admin"}
            return jsonify(data)
        
        #app.logger.info("%s", user_email)
        #data = { "email" : "user" }
    except Exception as ex:
        #TODO Error handling
        ic(ex)
        raise ex
    finally:
        if "cursor" in locals(): cursor.close()
        if "db" in locals(): db.close()
    
 
##################################______LOGIN_____#