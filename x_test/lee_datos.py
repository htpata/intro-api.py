import json

datos = [
    {"id":9,"nombre":"teclado","precio":80},
    {"id":5,"nombre":"monitor","precio":90}
]

for dato in datos:
    #print(dato)
    #print(json.load(dato))
    print(json.loads(json.dumps(dato))["id"])