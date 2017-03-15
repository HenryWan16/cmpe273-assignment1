from flask import Flask
import requests
import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

@app.route('/v1/<name>')
def getYaml(name):
    r = requests.get("https://github.com/sithu/assignment1-config-example/blob/master/" + name)
    if (r.ok):
        repoItem = json.loads(r.text)
        return "welcome_message: " + repoItem['welcome_message']

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')