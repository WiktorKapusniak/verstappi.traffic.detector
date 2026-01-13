from datetime import datetime, timezone
from mongo_models import logs
def getTime():
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return time
def saveLog(service,type,message,transactionId):
    log = logs.Logs(service=service,type=type,time=getTime(),message=message,transactionId=transactionId)
    log.save()
    print(f'{service} {type} {message} transactionId: {transactionId} {getTime()}')