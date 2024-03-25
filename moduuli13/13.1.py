from flask import Flask, Response
import json

app = Flask(__name__)

def is_prime(n):
    if n <= 1 or (n % 2 == 0 and n > 2): 
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

@app.route('/alkuluku/<int:n>', methods=['GET'])
def check_prime(n):
    result = {
        "Number": n,
        "isPrime": is_prime(n)
    }
    return Response(json.dumps(result), mimetype='application/json')

if __name__ == '__main__':
    app.run(debug=True, port=3000)
