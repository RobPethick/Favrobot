
class MockWidget(object):
    def __init__(self, isDailyGoals, date):
        self.isDailyGoals = isDailyGoals
        self.date = date
        self.hasDateBeenQueried = False
    
    def getDate(self):
        self.hasDateBeenQueried = True
        return self.date

    def isDailyBoard(self):
        return self.isDailyGoals