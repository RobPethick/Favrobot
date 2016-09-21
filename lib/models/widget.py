from .user import User
from datetime import datetime

class Widget(object):
    def __init__(self, json):
        self.type = json['type']
        self.name = json['name']
        self.color = json['color']
        self.publicSharing = json['publicSharing']
        self.widgetId = json['widgetCommonId']
        self.users = []
        for jsonUser in json['sharedToUsers']:
            self.users.append(User(jsonUser))

    def isDailyBoard(self):
        return self.type =='board' and 'Daily Goals' in self.name

    def getDate(self):
        if(self.isDailyBoard()):
            return datetime.strptime(self.name[-10:], '%d-%m-%Y')
