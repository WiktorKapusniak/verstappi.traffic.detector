from mongoengine import connect
from mongo_models import cars

connect(
    db="mydb",
    host="mongodb://localhost:27017/mydb"
)


def saveToDataBase(choice): # choice 1 - wybór zapisu dziesięciominutowego, choice 2 - wybór zapisu godzinnego
    if choice == 1:
        


# # zapis
# traffic = cars.Traffic(time="12.09.00", amount=12)
# traffic.save()

# # odczyt
# traffic = cars.Traffic.objects(time="12.09.00").first()
# print(traffic.amount)