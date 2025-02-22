from flask import Flask  # 'Flask' debe ir en mayúscula

app = Flask(__name__)  # 'Flask' en mayúscula

@app.route("/")
def index():
    return "Hola mundo"

if __name__ == "__main__":
    app.run()
