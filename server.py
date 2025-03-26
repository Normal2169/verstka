from flask import Flask, Response, jsonify
from flask_cors import CORS
from sqlalchemy import create_engine, text
connection_string = "mysql+pymysql://admin:123@192.168.50.114:3306/Local"
engine = create_engine(connection_string, echo=True)
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})
@app.route("/")
def index():
    return "Hello world"
@app.route("/api/Local/all")
def get_Local():
    with engine.connect() as connection:
        raw_Local = connection.execute(text("SELECT * FROM Local"))
        Local = []
        for i in raw_Local.all():
            Local.append(i._asdict())
        return jsonify(Local)
    return Response(jsonify({"status": "500", "message": "Database is down!"}), status=500)


def main():
    app.run("0.0.0.0", 8000, True)
if __name__ == "__main__":
    main()

