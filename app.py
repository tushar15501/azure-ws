from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Linux, World !! <b> Hello !! </b>  <img src = 'https://myimagestorage123.blob.core.windows.net/myconttest/1614679561595.jfif'>"
