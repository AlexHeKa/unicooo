from peewee import *

db = MySQLDatabase('hey',user='root',password='123456')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.

class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database


db.connect()

Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
