from flask import Flask, Response, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, text, bindparam, INTEGER
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

@app.route("/api/Local/<id>/upvote", methods=["PUT"])
def upvote(id: int):
    if request.method == "PUT":
        with engine.connect() as connection:
            raw_Local = connection.execute(text("SELECT * FROM Local"))
            Local = []
            for i in raw_Local.all():
                Local.append(i._asdict())
            return jsonify(Local)
        return Response(jsonify({"status": "500", "message": "Database is down!"}), status=500)
@app.route("/api/Local/<id>/downvote", methods=["PUT"])
def downvote(id: int):
    if request.method == "PUT":
        with engine.connect() as connection:
            raw_local = connection.execute(text(f"SELECT * FROM Local WHERE id = {id}"))
            score1 = []
            for i in raw_local.all():
                i.append(score1.asdict())
            return 


            score1 = int(score)-1
            query = text(f"UPDATE article SET score =  WHERE id = {id}")
            
            query = query.bindparams(bindparam("score", score1))
            connection.commit()
        return jsonify({"status": "500", "message": "Database is down!"})
def main():
    app.run("localhost", 8000, True)
if __name__ == "__main__":
    main()

