cart = []
class Cliente:
    count = 0
    def __init__(self, name, surname, email, age):
        self.name = name
        self.surname = surname
        self.email = email
        self.age = age
        Cliente.count += 1
    def welcome(self):
        return f'Bienvenido {self.name} a "Tu mundo digital"'
    def buy(self, product, quantity):
        cart.append(product)
        return f'El cliente {self.name} ha elejido {quantity} unidad/es del producto {product}\nSe le ha mandado su factura a su mail {self.email}'
    def age_control(self):
        if(self.age < 18):
            return 'Eres menor de edad, debes venir con tus padres o traer una autorización de ellos para poder hacer una compra.'
        return f'Usted puede comprar'
    def __str__(self):
        return f'El usuario {self.email} ha sido registrado'
    
    

class User(Cliente):
    def __init__(self, name, surname, email, age, password):
        super().__init__(name, surname, email, age)
        self.password = password    
    def __str__(self):
        return f'El usuario {self.name} esta conectado'   
        