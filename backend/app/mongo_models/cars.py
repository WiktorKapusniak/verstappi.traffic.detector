from mongoengine import Document, StringField, IntField
class TenMinuteStamp(Document):
    time = StringField()
    amount = IntField()
class HourStamp(Document):
    time = StringField()
    amount = IntField()
