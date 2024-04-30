from flask import Flask

app = Flask(__name__)


@app.route("/summa/<int:num1>/<int:num2>/<int:num3>/")
def min_avg_max(num1, num2, num3):
    arr = [num1, num2, num3]
    return {
        'min': min(arr),
        'avg': sum(arr) / len(arr),
        'max': max(arr)
    }


if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=3000)
