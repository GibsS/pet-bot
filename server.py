from flask import Flask

import translate

sess, model, inVocab, outVocab = translate.setup()

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/test")
def hello_world():
    res = translate.respondTo(sess, model, inVocab, outVocab, "hello")
    print(res)
    return 

if __name__ == "__main__":
    app.run()