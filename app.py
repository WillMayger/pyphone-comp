from flask import Flask, request, make_response
app = Flask(__name__)

@app.route("/")
def send():
    password = request.args['pass']
    use = request.args['app']
    if password == "password":

        db = open('db.txt', 'w')
        db.writelines(use)
        db.close()

        return "200"
    else:
        return "500"

@app.route("/check/")
def check():
    if request.args['pass'] == "password":
        db = open('db.txt', 'r')
        user_request = db.readline()
        db.close()

        db = open('db.txt', 'w')
        db.writelines("")
        return user_request
    else:
        "500"


if __name__ == "__main__":
    app.run()