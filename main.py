from customers.auth import Auth

auth = Auth()

print(auth.register("khachhang01", "123456"))
print(auth.login("khachhang01", "123456"))
