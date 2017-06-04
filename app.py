from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABSE_URI'] = "sqlite:///database.db"

# Configuration variabale depends on your database:
# postgresql+psycopg2://uname:passwd@host/dbname

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
