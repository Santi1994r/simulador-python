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
    def receipt(self):
        return f'Usted compro '
    def __str__(self):
        return f'El usuario {self.email} ha sido registrado'
    
# print(cliente1)
# print(cliente1.welcome())
# print(cliente1.count)
# print(cliente1.buy('computadora', 3))
# print(cliente1.receipt())
# print(cliente2.buy('mouse', 2))
# print(f'el carrito contiene: {cart}')
