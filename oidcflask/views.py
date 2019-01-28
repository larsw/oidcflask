from flask import render_template,jsonify,redirect
from json import dumps
from oidcflask import app,oidc
from jwt import JWT

@app.route('/')
@oidc.require_login
def index():
    access_token = oidc.get_access_token()
    if access_token != None:
        jwt = JWT()
        info = jwt.decode(access_token,do_verify=False)
        return jsonify(info)
    else:
        return "uh oh"

@app.route('/logout')
def logout():
    oidc.logout()
    return redirect('/')
