from mongoengine import Document, StringField, IntField
class Traffic(Document):
    time = StringField()
    carsAmount = IntField()
    motorcyclesAmount = IntField()
    busesAmount = IntField()
    trucksAmount = IntField()