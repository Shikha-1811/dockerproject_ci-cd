from flask import Flask

app = Flask(_name_)

@app.route("info")
def lwinfo():
    return "i m LW from India"

@app.route("/phone")
def lwphone():
    return "987654321"

app.run(host="0.0.0.0")
