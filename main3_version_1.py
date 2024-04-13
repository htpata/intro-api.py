from flask import Flask, request
from dotenv import load_dotenv
import os
import json
app = Flask(__name__)

load_dotenv()

VALOR_ENV_EJEMPLO = os.getenv('VALOR_ENV_EJEMPLO')
HTTP_RETURN_CODE_OK = 200

@app.route('/mini-historia',methods=['POST'])
def genera_mini_historia():
    palabra_base = json.loads(json.dumps(request.get_json(), ensure_ascii=False))["palabra_base"]
    mini_historia = {
        "texto" : "Había una vez una " + palabra_base,
        "valor_env_ejemplo": VALOR_ENV_EJEMPLO
    }
    return json.dumps(mini_historia, ensure_ascii=False), HTTP_RETURN_CODE_OK

if __name__ == '__main__':
    app.run(debug=True, # muestra mas detalle en mensajes de error
            host="0.0.0.0", # abre la comunicación con cualquier IP origen
            port="9999" # puerto para escuchar peticiones http
            )