from pymongo import MongoClient
from flask import Response
import json
import numpy as np


mongoURL = "mongodb://localhost:27017"
client = MongoClient(mongoURL)
db = client.piosoft

class JSONResponse(Response):
    def __init__(self, response = None, status = None, headers = None, mimetype = None, content_type = "application/json", direct_passthrough= False):
        super().__init__(response,status,headers,mimetype,content_type, direct_passthrough)

def obj_to_json(ob, dumps= True):
    if ob and "_id" in ob:
        ob["_id"] = str(ob["_id"])
    return json.dumps(ob) if dumps else ob

#append meter a lista

def list_to_json(lista):
    respuesta = []
    for l in lista:
        respuesta.append(obj_to_json(l,False))
    return json.dumps(respuesta)

def check_id(i):
    #hexadesimal
    if len(i) ==24:
        try:
            int(i,16)
            return True
        except ValueError:
            return False
    return False


def check_tipo(tipo):
    if tipo in ['Carro', 'Moto', 'Bicicleta', 'carro', 'moto', 'bicicleta' , 'bici']:
            return True
    return False

def check_tipo_reserva(tipoOferta,tipo):
    if tipoOferta==tipo:
        return True

def check_object(model, obj):
    if len(set(model).difference(set(obj.keys())))==0:
        return False
    return True


def check_disponibilidad(cal_ofertante, cal_demantante=None):
    a = np.matrix(cal_ofertante)
    if cal_demantante:
        b = np.matrix(cal_demantante)
        c = a & b
        return c.any()
    else:
        return a.any()

def check_disponibilidad_reserva(cal_ofertante, cal_demantante):
    a = np.matrix(cal_ofertante)
    if cal_demantante:
        b = np.matrix(cal_demantante)
        c = a & b
        return c.any()
    else:
        return a.any()
def do_error(error,status):
    return JSONResponse(json.dumps({"error":error}), status =status)


def check_telefone(telefono):
    numero = str(telefono)
    if not len(numero) == 10:
        return False
    else:
        return True

def check_email(email):
    if "@" in email:
        return True
    else:
        return False

def check_existe_user(idUser):
    if db.users.find_one({"_id": idUser}) is None:
        return False
    else:
        return True

def check_conductor(conductor):
    return  check_email(conductor[0])


