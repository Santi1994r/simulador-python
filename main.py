import json


def register():
    name = input("Ingrese su nombre").lower()
    password = input("Ingrese su password. Minimo 8 caracteres y maximo 15.").lower()

    while (not name or name.isdigit() or len(name) < 3 or len(name) > 12 or not password or len(password) < 8 or len(password) > 15):
        name = input("Ingrese su nombre").lower()
        password = input(
            "Ingrese su password. Minimo 8 caracteres y maximo 15.").lower()

    register_format = {
        "nombre": name,
        "contrasenia": password
    }

    user_json = json.dumps(register_format, indent= 2)
    return user_json


def upload_to_DB(dic):
    with open("DB.txt", "a") as file:
        file.write(dic + "," + "\n")


def show_DB():
    with open("DB.txt", "r") as file:
        contenido = file.read()
        return contenido
    
def exist_user():
    data_users = json.loads(show_DB()) 
    return data_users    

#   Esto me marco el tutor corrertor que tengo que agregar
# En cuanto a tu codigo, esta bien pero aun le falta algo importante: en el logeo. se debe validar que el usuario y clave ingresado este dentro de nuestra base de datos. 
# Por ultimo ojo con los. "breaks" ya que te rompen el loop y la idea es que salga solo con la opcion de "salir", no?
# Para mi el trabajo esta correcto pero si poder agregar la validacion la subimos a optimo.



# Quiero que con esta funcion hacer la validacion de si existe el usuario. Quiero pasar lo que tengo en el txt a formato dict pero tengo ese error.
# def login():
#     with open("DB.txt", "r") as file:
#         content = file.read()
#         convert = json.loads(content) # Tengo un error con el loads y nose como resolverlo
#     print(convert)

 

validate = True

while validate:
    option_main = input("Bienvenido al curso de coder de python \n¿Que desea hacer?:\n (1)Registrarme\n (2)Ver usuarios\n (3)Salir").lower()
    
    if (option_main == "1"):
        upload_to_DB(register())
        break
    elif (option_main == "2"):
        print("Los usuarios ingresados son: " + show_DB())
        break
    elif (option_main == "3"):
        print("Adios")
        break
    else:
        print("Opción incorrecta")
        validate = True
        
   
