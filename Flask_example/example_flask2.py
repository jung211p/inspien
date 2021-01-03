from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def first():
	return "first"

@app.route('/flask')
def flask():
	return "flask"

@app.route("/profile/<username>")
def get_profile(username):
	return "profile: " + username

@app.route("/first/<username>")
def get_first(username):
	return "hello " + username

@app.route("/hello/")
def hello():
	return "hello"

if __name__ == "__main__":
	"""
	with app.test_request_context():
		print(url_for('hello'))
		print(url_for('get_profile', username = "jh"))
"""
	app.run(host="0.0.0.0", port = "1234")
