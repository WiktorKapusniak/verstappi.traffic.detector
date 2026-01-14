from mongoengine import Document, StringField, DateTimeField
class Logs(Document):
    service = StringField(required=True)
    type = StringField(
        required = True,
        choices = ("INFO","WARNING","ERROR","CRITICAL")
    )
    time = DateTimeField(required=True)
    message = StringField(required=True)
    transactionId = StringField(required=True)