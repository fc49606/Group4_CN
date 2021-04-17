from flask import Flask, request, jsonify
from flask_restful import Resource, Api
import os
import sqlalchemy
import psycopg2

app = Flask(__name__)
api = Api(app)

db = None

def tcp_connection_engine():
    db_user = os.environ["DB_USER"]
    db_pass = os.environ["DB_PASS"]
    db_name = os.environ["DB_NAME"]
    db_socket_dir = os.environ.get("DB_SOCKET_DIR", "/cloudsql")
    cloud_sql_connection_name = os.environ["CLOUD_SQL_CONNECTION_NAME"]

    pool = sqlalchemy.create_engine(
        # Equivalent URL:
        # postgres+pg8000://<db_user>:<db_pass>@<db_host>:<db_port>/<db_name>
        sqlalchemy.engine.url.URL(
            drivername="postgresql+pg8000",
            username=db_user,  # e.g. "my-database-user"
            password=db_pass,  # e.g. "my-database-password"
            database=db_name,  # e.g. "my-database-name"
            query={
                "unix_sock": "{}/{}/.s.PGSQL.5432".format(
                    db_socket_dir,  # e.g. "/cloudsql"
                    cloud_sql_connection_name)  # i.e "<PROJECT-NAME>:<INSTANCE-REGION>:<INSTANCE-NAME>"
            }
        )
    )
    return pool

def read(year,streamPlat):
    print("TESTE: ")
    db = tcp_connection_engine()
    with db.connect() as conn:
        aux = ""
        print("TESTE: "+streamPlat)
        if streamPlat == "netflix":	
            aux +=" and netflix=1"
        if streamPlat == "hulu":
            aux+=" and hulu=1"
        if streamPlat == "prime_video":
            aux+=" and prime_video=1"
        if streamPlat == "disneyplus":
            aux+=" and disneyplus=1"
        teste = conn.execute("""SELECT title from streaming_plataform where year="""+year+aux)
        #resposta = cursor.fetchall()
        print("Querie correu bem")
        conn.close()
        return jsonify({'result': [dict(row) for row in teste]})

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world Movies'}
		
class Movie(Resource):
    def get(self,year,streamPlat):
        return read(year,streamPlat)		

api.add_resource(HelloWorld, '/')
api.add_resource(Movie,'/api/movie/<string:year>/<string:streamPlat>/')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
	#app.run(host='127.0.0.1', port=8080, debug=True)
