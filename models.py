from peewee import SqliteDatabase,Model,CharField,IntegerField

db = SqliteDatabase('mysql.db')
db.connect()

class User(Model):
    name = CharField(max_length=50)
    age = IntegerField()
    email = CharField(max_length=50)

    class Meta:
        database = db
        db_table = 'users'

User.create_table()