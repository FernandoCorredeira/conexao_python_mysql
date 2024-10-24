
import mysql.connector
from flask import Flask, make_response, jsonify, request



mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'root',
    database= 'lojinha'
)


app = Flask(__name__)


@app.route('/cars', methods=['GET'])

def get_carros():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM produtos')
    result = cursor.fetchall()
    carros = list()
    for carro in result:
        carros.append({
            'id': carro[0],
            'marca': carro[1],
            'modelo': carro[2],
            'ano': carro[3]
        })
    return carros
#make_response(jsonify(cars)) #Caso não retornar a req


#Insert no banco
@app.route('/cars', methods=['POST'])
def create_cars():
    car = request.json
    cursor = mydb.cursor()
    sql= f"INSERT INTO produtos(marca,modelo,ano) VALUES ('{car['marca']}','{car['modelo']}','{car['ano']}')"
    cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
        mensagem= 'Carro cadastrado',
        car = car
    ))

@app.route('/cars/delete/<id>', methods=['DELETE'])
def delete_cars(id):
    cursor = mydb.cursor()
    sql= f"DELETE FROM produtos WHERE id = {id}"
    cursor.execute(sql)
    mydb.commit()

    return make_response(
        jsonify(
        mensagem= 'Carro deletado',
        
    ))
    


app.run()