# OnLineVoting


Proyecto de votación en linea para la materia de Proyecto Especial de 3 Créditos.


# Identificador

Recibe un Nonce y crea un objeto en la base de datos con un ID único.

## Endpoints

### generateId

POST {context}/generateId

Recibe un Nonce y devuelve su respectivo ID



```HEADERS: Content-Type = application/json
BODY : {
“nonce”:"asasd324" 
}
RESPONSE : Bad_request 400 Unauthorized 401 Ok 200
RESPONSE_BODY : {
“id”:123,
"nonce":"asasd324" 
}

```


### getNonce

POST {context}/getNonce

Recibe un ID y devuelve su respectivo Nonce



```HEADERS: Content-Type = application/json
BODY : {
"id":123
}
RESPONSE : Bad_request 400 Unauthorized 401 Ok 200
RESPONSE_BODY : {
"id":123,
"nonce":"asasd324" 
}

```


## Para tener en cuenta

- En /Identifier/src/main/resources/application.properties cambiar las propiedades de Postgress por las de la base de datos (URL, user, password, etc)

- Tambien se debe comentar en /Identifier/pom.xml el XML que contiene el artefacto H2 y descomentar el XML que contiene el artefacto Postgress

### Run

Para correr el aplicativo es necesario tener instalado java 1.8 o superior. 
Tambien es necesario tener Apache Maven instalado en el equipo y para correr el aplicativo se debe correr el siguiente comando

``` #mvn spring-boot:run ```