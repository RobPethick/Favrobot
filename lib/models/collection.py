from .user import User
import datetime
class Collection(object):
    def __init__(self, json):
        self.name = json['name']
        self.shareWidgetsByDefault = json['shareWidgetsByDefault']
        self.collectionId = json['collectionId']
        self.publicSharing = json['publicSharing']
        self.archived = json['archived']
        self.users = []
        for jsonUser in json['sharedToUsers']:
            self.users.append(User(jsonUser))
        self.widgets = []

    def addWidgets(self, widgets):
        for widget in widgets:
            self.widgets.append(widget)

    def getNextDailyGoalsName(self):
        boardDates = [x.getDate() for x in self.widgets if x.isDailyBoard()]
        latestDate = max(boardDates)
        oneWeek = datetime.timedelta(weeks= 1)
        nextBoardDate = latestDate + oneWeek
        return "Daily Goals " + nextBoardDate.strftime("%d-%m-%Y")
