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
        
   
