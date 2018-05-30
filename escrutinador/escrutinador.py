#!/usr/bin/env python3

import json
import http.client
import urllib.request

def jsonMessages():

    machine = 'http://httpbin.org/post'
    secretKey = {"con1":40, "con2":20}                                                                             # Create keys in json format
    params = json.dumps(secretKey).encode('ISO-8859-1')                                                            # Encode and send json key
    req = urllib.request.Request(machine, data=params, headers={'content-type': 'application/json'})               
    response = urllib.request.urlopen(req)                                                                         # Get response 
    print(response.read().decode('ISO-8859-1'))                                                                    # Read response

def getRequest():
    connection = http.client.HTTPSConnection('http://httpbin.org/post')                                            # Machine to connect to (IP or URL)
    connection.request("GET", "/")
    answer1 = connection.getresponse()

def postRequest():
    pass
    
def publicDecipher():
    pass

def nonce():
    pass

def calcXor():
    pass

def privateDecipher():
    pass

def voteCount():
    pass

def main():
    jsonMessages()
    publicDecipher()
    nonce()
    calcXor()
    privateDecipher()
    voteCount()

if __name__ == "__main__":
    main()




# USAR ISO-8859-1 PARA LOS JSON
