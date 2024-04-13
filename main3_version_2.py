from flask import Flask, request
import google.generativeai as genai
from dotenv import load_dotenv
import os
import json
app = Flask(__name__)

load_dotenv()

HTTP_RETURN_CODE_OK = 200
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

# gemini safety config
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_NONE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_NONE"
  },
]

model = genai.GenerativeModel(model_name="gemini-1.0-pro",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

@app.route('/mini-historia',methods=['POST'])
def genera_mini_historia():
    palabra_base = json.loads(json.dumps(request.get_json(), ensure_ascii=False))["palabra_base"]
    
    # pedirle una mini historia a Gemini
    convo = model.start_chat(history=[
    ])
    convo.send_message("dime una historia pequeña de un párrafo que incluya la palabra " + palabra_base)
    mini_historia = convo.last.text

    resultado = {
        "texto" : mini_historia,
    }
    return json.dumps(resultado, ensure_ascii=False), HTTP_RETURN_CODE_OK

if __name__ == '__main__':
    app.run(debug=True, # muestra mas detalle en mensajes de error
            host="0.0.0.0", # abre la comunicación con cualquier IP origen
            port="9999" # puerto para escuchar peticiones http
            )