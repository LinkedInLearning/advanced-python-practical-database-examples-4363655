from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:password@localhost/project_tracker"
app.config["SECRET_KEY"] = b'\xa6\xcbo-Z\xf6\xeb\xce\xb0\xbc\xf9"\xba\xad\xed\xe2\xa4L\x14\x1a\xde\x8eg@'
db = SQLAlchemy(app)

class Project(db.Model):
	__tablename__ = 'projects'
	project_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(length=50))



#Define a route
@app.route("/")
def show_projects():
	return render_template("index.html", projects=Project.query.all())

@app.route("/project/<project_id>")
def show_tasks(project_id):
	return render_template("project-tasks.html", project_id=project_id)

@app.route("/add/project", methods=['POST'])
def add_project():
	# TODO: Add project
	return "Project added successfully"

@app.route("/add/task/<project_id>", methods=['POST'])
def add_task(project_id):
	# TODO: Add task
	return "Task added successfully"


app.run(debug=True, host="127.0.0.1", port=3000)