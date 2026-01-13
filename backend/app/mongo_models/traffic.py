from mongoengine import Document, StringField, IntField
class TrafficWithTimeStamp(Document):
    time = StringField(required=True)
    carsAmount = IntField(required=True)
    motorcyclesAmount = IntField(required=True)
    busesAmount = IntField(required=True)
    trucksAmount = IntField(required=True)