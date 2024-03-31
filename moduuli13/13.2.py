from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='flight_game',
    user='root',
    password='5alattu',
    autocommit=True
)

@app.route('/kenttä/<icao_code>')
def get_airport(icao_code):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT icao, name, municipality FROM airports WHERE icao = %s", (icao_code,))
    airport = cursor.fetchone()
    if airport is None:
        return jsonify({"error": "No airport found with the given ICAO code"}), 404
    return jsonify({"ICAO": airport['icao'], "Name": airport['name'], "Municipality": airport['municipality']})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
