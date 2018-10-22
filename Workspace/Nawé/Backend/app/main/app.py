from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/educacion", methods=["GET"])
def pureba():
    return render_template('prueba.html')

@app.route("/home", methods=["GET"])
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET"])
def login():
    return render_template('index.html')

@app.route("/mapa", methods=["GET"])
def mapa():
    return render_template('mapa.html')
@app.errorhandler(404)
def page_not_found(e):
    return e, 404


@app.errorhandler(500)
def page_server_error(e):
    return e, 500


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9090, debug=False, threaded=True)
