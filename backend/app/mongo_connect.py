from mongoengine import connect
from mongo_models import traffic
from datetime import datetime, timezone
from ownLogger import saveLog
connect(
    db="mydb",
    host="mongodb://localhost:27017/mydb"
)

service = {
    'name': "MONGO",
    'info': "INFO",
    'error' : "ERROR",
    'warning': "WARNING"
}

def getTime():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time

def saveToDataBase(amount,transId):
    try:
        data = traffic.TrafficWithTimeStamp(time=getTime(),amount=amount)
        data.save()
        saveLog(service['name'],service['info'],"saved data to database",transId)
    except Exception as e:
        saveLog(service['name'],service['error'],str(e),transId)
        
def readFromDataBase(transId):
    try:
        data = traffic.TrafficWithTimeStamp.objects()
        saveLog(service['name'],service['info'],"granting database data",transId)
        return data
    except Exception as e:
        saveLog(service['name'],service['error'],str(e),transId)