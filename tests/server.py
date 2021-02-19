from sso_ui_auth_client.cas import authenticate, get_login_url, get_logout_url
from flask import Flask,render_template, redirect, request

app = Flask(__name__)

SERVICE_URL="http://localhost:5000/login"

@app.route('/login')
def login():
  ticket = request.args.get('ticket')
  error, sso_profile = authenticate(ticket, SERVICE_URL)

  if error:
    return "Login Failure"

  if sso_profile is not None:
    return sso_profile

  cas_login_url = get_login_url(SERVICE_URL)
  return redirect(cas_login_url)

@app.route('/logout')
def logout():
    cas_logout_url = get_logout_url(SERVICE_URL)
    return redirect(cas_logout_url)

@app.route('/')
def root():
  return render_template('login.html')




