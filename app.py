from flask import Flask
from github import ContentFile
from github import Github
import json
import sys

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello from Dockerized Flask App!!"

# @app.route('/v1/<name>')
# def getYaml(name):
#     r = requests.get("https://github.com/HenryWan16/cmpe273-assignment1/blob/master/" + name)
#     if (r.ok):
#         print r.content
#         repoItem = json.loads(r.content)
#         return "welcome_message: " + repoItem['welcome_message']

@app.route('/v1/<name>')
def getContent(name):
    g = Github("HenryWan16@gmail.com", "Wh19881004")
    # path = "https://github.com/HenryWan16/cmpe273-assignment1"
    path = sys.argv[1]
    args = path.split("/")
    n = len(args)
    repo = g.get_user().get_repo(args[n - 1])
    contents = repo.get_contents("" + name)
    str = contents.decoded_content
    element = str.split("\n")
    # return the first line.
    return element[0]

    # return json
    # strJson =
    # i = 0
    # for i in range(0, len(element)):
    #     if (i)

    # return all the text;
    # str = ""
    # for e in element:
    #     str = str + e + "\n"
    # print str
    # return str

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
