from models import User

# u1 = User(name = 'Victor',age = 45,email = 'alien1982@hotmail.fr')
# u2 = User(name = 'Maxim',age = 40,email = 'maxfactor@hotmail.com')
# u1.save()


u = User.get(User.name == 'Victor')
print(u)
print(u.age)
print(u.email)
u.delete_instance()
