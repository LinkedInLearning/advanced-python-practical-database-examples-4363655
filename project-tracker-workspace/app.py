from flask import Flask, render_template

app = Flask(__name__)

#Define a route
@app.route("/")
def show_projects():
	return render_template("index.html")

app.run(debug=True, host="127.0.0.1", port=3000)