from flask import Flask, render_template, request, redirect, session
from kiteconnect import KiteConnect

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Secret key for session management

# Zerodha API credentials
api_key = ''
api_secret = ''
redirect_url = 'http://localhost:5000/callback'  # Redirect URL after authentication

# Initialize Kite Connect client
kite = KiteConnect(api_key=api_key)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    # Redirect the user to Zerodha's login page for authentication
    return redirect(kite.login_url())

@app.route('/callback')
def callback():
    # Callback URL after successful authentication
    request_token = request.args.get('request_token')
    data = kite.generate_session(request_token, api_secret=api_secret)
    kite.set_access_token(data['access_token'])

    # Store the access token in the session
    session['access_token'] = data['access_token']

    return redirect('/')

@app.route('/search', methods=['POST'])
def search_instruments():
    query = request.form['search_query']
    
    # Retrieve the access token from the session
    access_token = session.get('access_token')

    if access_token:
        kite.set_access_token(access_token)
        instruments = kite.search_instruments(query)
        return render_template('search_results.html', instruments=instruments)
    else:
        return "Access token not found. Please authenticate first."

if __name__ == '__main__':
    app.run(debug=True)
