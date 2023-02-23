# import json

# DB = {}

# def register(DB):
#     name = input('Ingrese su nombre').lower()
#     password = input(
#         'Ingrese su password. Minimo 8 caracteres y maximo 15.').lower()

#     while (not name or name.isdigit() or len(name) < 3 or len(name) > 12 or not password or len(password) < 8 or len(password) > 15):
#         name = input('Ingrese su nombre').lower()
#         password = input('Ingrese su password. Minimo 8 caracteres y maximo 15.').lower()

#     DB["name"] = name
#     DB["password"] = password
    
#     return DB

# print(register(DB))