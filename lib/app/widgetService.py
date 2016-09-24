from lib.models.widget import Widget

class WidgetService(object):
    def __init__(self, requester):
        self.requester = requester 
        self.defaultColumnNames = ['Doing', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']


    def getWidgets(self, collectionId):
        widgetsJson = self.requester.getWidgets(collectionId)
        widgets = []
        for widgetJson in widgetsJson['entities']:
            widgets.append(Widget(widgetJson))
        return widgets

    def addWeeklyBoard(self, collection, boardName):
        newBoard = Widget(self.requester.createBoard(boardName, collection.collectionId))
        for columnName in self.defaultColumnNames:
            self.requester.addColumnToBoard(columnName, newBoard.widgetId)
        return True