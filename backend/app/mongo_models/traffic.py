from mongoengine import (
    Document, EmbeddedDocument, DateTimeField, IntField, EmbeddedDocumentField
)

class TrafficData(EmbeddedDocument):
    carsIn = IntField(required=True)
    carsOut = IntField(required=True)
    motorcyclesIn = IntField(required=True)
    motorcyclesOut = IntField(required=True)
    busesIn = IntField(required=True)
    busesOut = IntField(required=True)
    trucksIn = IntField(required=True)
    trucksOut = IntField(required=True)

class Traffic(Document):
    time = DateTimeField(required=True)
    carsIn = IntField(required=True)
    carsOut = IntField(required=True)
    motorcyclesIn = IntField(required=True)
    motorcyclesOut = IntField(required=True)
    busesIn = IntField(required=True)
    busesOut = IntField(required=True)
    trucksIn = IntField(required=True)
    trucksOut = IntField(required=True)

class DailyTraffic(Document):
    day = DateTimeField(required=True)
    traffic = EmbeddedDocumentField(TrafficData, required=True)
