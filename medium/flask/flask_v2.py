from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bili', methods=['GET','POST'])
def bili():
    data = request.get_json()
    print(data)
    return jsonify({"message": "Data received", "data": data})

if __name__ == '__main__':
    app.run(debug=True)