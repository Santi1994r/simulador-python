from paquete.modulo1 import Cliente, User

cliente1 = Cliente('santiago', 'ruiz', 'santiagoruiz9416@gmail.com', 28)
cliente2 = Cliente('maria', 'perez', 'maria@gmail.com', 30)
cliente3 = Cliente('manuel', 'befart', 'manu@gmail.com', 15)
user1 = User('martin', 'nazseski', 'martin@gmail.com', 22, 123456)


print(cliente1)
print(cliente1.welcome())
print(cliente1.buy('notebook', 2))
print(cliente3.age_control())
print(user1)
