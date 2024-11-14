from flask import Flask, request, jsonify

app = Flask(__name__)

# get请求：http://127.0.0.1:5000/index?age=19&pwd=123
# post请求：http://127.0.0.1:5000/index
@app.route('/', methods=["POST", "GET"])
def index():
    age =request.args.get('age')
    pwd = request.args.get('pwd')
    # print(age, pwd)
    xx = request.form.get("p_age")
    yy = request.form.get("p_pwd")
    age = request.form.get("p_age")
    pwd = request.form.get("p_pwd")
    # str_json = request.json
    print(xx, yy)
    print(age, pwd)
    # print(str_json)
    return jsonify({"status": True, "Des": "Your are successful!"})

@app.route('/xx')
def xx():
    return('成功!')

@app.route('/yy')
def yy():
    return('失败')

if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)