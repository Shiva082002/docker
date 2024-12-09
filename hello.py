from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "hello world"

@app.route("/sum")
def Smaths():
    a = 10
    b = 20
    return str(a+b)

@app.route("/multiply")
def Mmaths():
    a = 10
    b = 20
    return str(a*b)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
