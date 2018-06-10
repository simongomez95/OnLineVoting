import flask
import Crypto
import requests
from Crypto.PublicKey import RSA
from Crypto import Random

endpoint_identificador = 'http://algo.com/endpoint'
endpoint_jurado = 'http://algo.com/endpoint'
votos = []
def cargar_clave(keyfile):
    fd = open(keyfile, "rb")
    key = fd.read()
    fd.close()
    return RSA.importKey(key)

def decypher(cypher, key):
    message = key.decrypt(cypher)
    return message

def verify(msg, pubkey, signature): 
    return pubkey.verify(msg, signature)


def guardar_voto(voto_caso):
    base = pow(2,32)
    porcion = int(base/6)
    if 0 <= voto_caso <= porcion-1:
        voto[0]+= 1
    elif porcion<= voto_caso <= (porcion*2)-1 :
        voto[1] += 1
    elif (porcion*2) <= voto_caso <= (porcion*3)-1 :
        voto[2]+=1
    elif porcion*3 <= voto_caso <= porcion*4-1 :
        voto[3]+=1
    elif porcion*4 <= voto_caso <= porcion*5-1 :
        voto[4]+=1
    elif porcion*5 <= voto_caso <= porcion*6-1:
        voto[5]+=1
    elif porcion*6 <= voto_caso <= ((porcion * 6) + (base%6)):
        voto[6]+=1



@app.route('/escrutinador', methods=['POST'])
def recibir():
    priv_key= cargar_clave(priv_key_file)
    jury_pub = cargar_clave(jury_key_file)

    json_recibido = request.get_json(force=True)
    id_cifrado = json_recibido.get('id')
    voto_cifrado = json_recibido.get('voto')
    signature = json_recibido.get('firma')
    if(not verify(voto_cifrado, jury_pub, signature)):
        print("Firma invalida")

    vote = decypher(voto_cifrado, priv_key)

    identificador = decypher(id_cifrado, priv_key)

    response = requests.post(endpoint_identificador, data={'id': identificador}, headers={'content-type': 'application/json'})
    nonce_cifrado = json_recibido.get('nonce')
    nonce = decypher(nonce_cifrado, priv_key)
    voto = voto ^ nonce #xor
    guardar_voto(vote)
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
