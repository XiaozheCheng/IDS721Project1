from flask import Flask
from flask import jsonify
app = Flask(__name__)

def calculator(x, y):
    m = max(x, y)
    n = min(x, y)
    while m%n:
        m, n = n, m%n
    gcd = n
    lcm = (x*y//n)}
    
    return [{'gcd':gcd}, {'lcm':lcm}]





@app.route('/')
def hello():
    print("I am a Greatest Common Divisor & Least Common Multiple")
    return 'Hello Greatest Common Divisor & Least Common Multiple! Please use it to calculate Greatest Common Divisor & Least Common Multiple at route by typing: /gcd-and-lcm/x/y (x and y are the two number you want to calculate)'

@app.route('/gcd-and-lcm/<x>/<y>')
def changeroute(x, y):
    print(f"Solve Greatest Common Divisor & Least Common Multiple for GCD:{x} and LCM:{y}")

    result = calculator(int(x), int(y))
    return jsonify(result)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
