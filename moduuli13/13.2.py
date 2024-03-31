from flask import Flask, Response
import mysql.connector
import json

app = Flask(__name__)

mydb = mysql.connector.connect(
    host='localhost',
    port='3306',
    database='flight_game',
    user='root',
    password='5alattu',
    autocommit=True
)


@app.route('/kentta/<icao_code>')
def get_airport(icao_code):
    cursor = mydb.cursor(dictionary=True)
    cursor.execute("SELECT ident, name, municipality FROM airport WHERE ident = %s", (icao_code,))
    airport = cursor.fetchone()
    if airport is None:
        return Response(json.dumps({"error": "Syöttämälläsi ICAO-koodilla ei löytynyt lentokenttää."}), status=404,
                        mimetype='application/json')
    return Response(
        json.dumps({"ICAO": airport['ident'], "Name": airport['name'], "Municipality": airport['municipality']}),
        status=200, mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True, port=3000)
