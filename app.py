from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return """
    <html>
    <head>
    <title>Login</title>
    </head>
    <body>

    <h1>Login</h1>

    <form>
    <label for="fname">First name:</label><br>
    <input type="text" id="fname"><br>
    <label for="lname">Last name:</label><br>
    <input type="text" id="lname">
    </form>

    </body>
    </html>
"""

@app.route('/users',methods=["POST","GET"])
def users():
   if request.method == 'POST':
       print(request.json)
       return "OK (POST)"
   else:
       return "OK (GET)"

