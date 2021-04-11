from flask import Flask, request
from flask_restful import Resource, Api
import psycopg2

app = Flask(__name__)
api = Api(app)

# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}

class Movie(Resource):
    def get(self, year,streamPlat):
        conn = psycopg2.connect(
            database="movies_streaming_plataform", user='postgres', password='root', host='34.89.4.184', port= '5432'	
        )
        conn.autocommit = True
        cursor = conn.cursor()
        aux=""
        print("TESTE: "+streamPlat)
        if streamPlat == "netflix":
            aux+=" and netflix=1"
        if streamPlat == "hulu":
            aux+=" and hulu=1"
        if streamPlat == "prime_video":
            aux+=" and prime_video=1"
        if streamPlat == "disneyplus":
            aux+=" and disneyplus=1"
        cursor.execute("""SELECT title from streaming_plataform where year="""+year+aux)
        resposta = cursor.fetchall()
        print("Querie correu bem")
        conn.close()
        return resposta

# api.add_resource(HelloWorld, '/')
api.add_resource(Movie,'/api/movie/<string:year>/<string:streamPlat>/')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
