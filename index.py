from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
	return render_template("form.html")

@app.route("/submit", methods=["POST"])
def form_submit():
	return request.form.get("todo")

app.run()