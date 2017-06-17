from flask import Flask, request

import translate

sess, model, inVocab, outVocab = translate.setup()

app = Flask(__name__)

app.debug = False
app.testing = False

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/test")
def hello_world():
	res = translate.respondTo(sess, model, inVocab, outVocab, "hello")
	print(res)
	return res 

@app.route("/ask", methods=['POST'])
def ask():
	res = translate.respondTo(sess, model, inVocab, outVocab, request.get_json()["message"])
	print(res)
	return res

if __name__ == "__main__":
    app.run("0.0.0.0")
