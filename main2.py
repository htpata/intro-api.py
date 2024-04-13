from flask import Flask, request
import json
app = Flask(__name__)

HTTP_RETURN_CODE_OK = 200
HTTP_RETURN_CODE_NOT_FOUND = 404

datos = [
    {"id":9,"nombre":"teclado","precio":80},
    {"id":5,"nombre":"monitor","precio":90}
]

@app.route('/')
def root():
    response_data = {"message":"all is good in the server side"}
    return response_data, HTTP_RETURN_CODE_OK

@app.route('/productos')
def productos():
    return datos, HTTP_RETURN_CODE_OK

@app.route('/productos/<int:id>')
def un_producto(id: int):
    for dato in datos:
        if json.loads(json.dumps(dato))["id"] == id:
            return dato, HTTP_RETURN_CODE_OK
    return {}, HTTP_RETURN_CODE_NOT_FOUND


@app.route('/productos',methods=['POST'])
def grabar_producto():
    datos.append(request.get_json())
    return {}, HTTP_RETURN_CODE_OK

@app.route('/productos/<int:id>',methods=['DELETE'])
def borrar_producto(id: int):
    array_index = 0
    for dato in datos:
        if json.loads(json.dumps(dato))["id"] == id:
            datos.pop(array_index)
            return {}, HTTP_RETURN_CODE_OK
        else:
            array_index = array_index + 1
    return {}, HTTP_RETURN_CODE_NOT_FOUND

@app.route('/productos/<int:id>',methods=['PUT'])
def actualizar_producto(id: int):
    array_index = 0
    for dato in datos:
        if json.loads(json.dumps(dato))["id"] == id:
            datos.pop(array_index)
            datos.append(request.get_json())
            return {}, HTTP_RETURN_CODE_OK
        else:
            array_index = array_index + 1
    return {}, HTTP_RETURN_CODE_NOT_FOUND

if __name__ == '__main__':
    app.run(debug=True, # muestra mas detalle en mensajes de error
            host="0.0.0.0", # abre la comunicación con cualquier IP origen
            port="8888" # puerto para escuchar peticiones http
            )