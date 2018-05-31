import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization


endpoint_identificador = 'http://algo.com/endpoint'

@app.route('/escrutinador', 'POST')
def recibir():
    id_encriptado = request.form['id']
    voto_encriptado = request.form['voto']
    voto = desencriptar(voto_encriptado)
    id = desencriptar(id_encriptado)
    response = requests.post(endpoint_identificador, data={'id': 12524})
    nonce_encriptado = response.form['nonce']
    nonce = desencriptar(nonce_encriptado)
    voto = voto ^ nonce
    guardar_voto(voto)

def desencriptar(cifrado):
    clave = cargar_clave()
    mensaje = clave.decrypt(cifrado, 
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    ))
    return mensaje

def cargar_clave():
    with open(archivo_clave_privada, "rb") as key_file:
        key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
        return key