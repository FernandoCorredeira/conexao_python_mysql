
import mysql.connector
from flask import Flask, make_response, jsonify




mydb = mysql.connector.connect(
    host= 'localhost',
    user= 'root',
    password= 'root',
    database= 'lojinha'
)


#app = Flask(__name__)


def get_carros():
    cursor = mydb.cursor()
    cursor.execute('SELECT * FROM produtos')
    result = cursor.fetchall()
    #carros = list()
    #for carro in result:
     #   carros.append({
     #       'id': carro[0],
     #       'marca': carro[1],
     #       'modelo': carro[2],
     #       'ano': carro[3]
      #  })
    return result
#make_response(jsonify(cars)) #Caso não retornar a req


#Insert no banco

def create_cars(data_mark_car, data_model_car, data_year_car):
    cursor = mydb.cursor()
    sql= f"INSERT INTO produtos(marca,modelo,ano) VALUES ('{data_mark_car}','{data_model_car}','{data_year_car}')"
    cursor.execute(sql)
    mydb.commit()
    mydb.close()
    


def delete_cars(id):
    cursor = mydb.cursor()
    sql= f"DELETE FROM produtos WHERE id = {id}"
    cursor.execute(sql)
    mydb.commit()

    
