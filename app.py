from flask import Flask

app = Flask(__name__)

@app.route('/') # This defines the route for the root URL
def home_page():
    return "Hello Gopi"

@app.route('/Jagan') # This defines the route for the root URL
def home_page():
    return "Hello Jagan"

# ... other routes you might have ...
