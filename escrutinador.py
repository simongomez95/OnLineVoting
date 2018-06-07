import requests
import flask
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

endpoint_identificador = 'http://algo.com/endpoint'
endpoint_jurado = 'http://algo.com/endpoint'
priv_key=None

@app.route('/escrutinador', 'POST')
def recibir():
    id_cifrado = request.form['id']
    voto_cifrado = request.form['voto']
    voto = descifrar(voto_cifrado)
    id = descifrar(id_cifrado)
    response = requests.post(endpoint_identificador, data={'id': 12524})
    nonce_cifrado = response.form['nonce']
    nonce = descifrar(nonce_cifrado)
    voto = voto ^ nonce #xor
    guardar_voto(voto) 

def send():                        # NEED HEALING, no sé si es así XD, la ide es enviar la llave publica
    pub_key = create_keys_RSA() 
    requests.post(endpoint_jurado, data={'pub_key': pub_key})

def cargar_clave():
    with open(archivo_clave_privada, "rb") as key_file:
        key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
        return key

######################################## CHARLIE - MANU #####################################

def create_keys_RSA(bits=2048):
    new_key = rsa.generate_private_key(
          public_exponent=65537,
          key_size=bits,
          backend=default_backend()
    )
    private_key = new_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = new_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    
    self.priv_key = private_key
    return public_key

def jury(encrypted_vote):
    scrutator_vote = decypher(encrypted_vote, priv_key) 
    vote = decypher(scrutator_vote, jury_pubkey)

def decypher(cypher, key):
    message = key.decrypt(cypher, 
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    return message
    
if __name__ == "__main__":
    create_keys_RSA()
