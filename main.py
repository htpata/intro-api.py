from flask import Flask
app = Flask(__name__)

HTTP_RETURN_CODE_OK = 200

@app.route('/')
def root():
    response_data = {"message":"all is good in the server side"}
    return response_data, HTTP_RETURN_CODE_OK

if __name__ == '__main__':
    app.run(debug=True, # muestra mas detalle en mensajes de error
            host="0.0.0.0", # abre la comunicación con cualquier IP origen
            port="8888" # puerto para escuchar peticiones http
            )