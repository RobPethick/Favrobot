from .requester import Requester
from models.collection import Collection
from models.widget import Widget

class App(object):

    def __init__(self, email, password, organizationId):
        self.requester = Requester(email, password, organizationId)
        self.success = False
        self.defaultColumnNames = ['Doing', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    def run(self, collection_name):
        collectionId = self.getCollectionIdFromName(collection_name)
        collection = self.getCollection(collectionId)
        nextBoardName = collection.getNextDailyGoalsName()
        self.success = self.addWeeklyBoard(collection, nextBoardName)

    def getCollectionIdFromName(self, collection_name):
        collectionsJson = self.requester.getCollections()
        for collectionJson in collectionsJson['entities']:
            collection = Collection(collectionJson)
            if collection_name in collection.name:
                print(collection.name + ": collection found")
                return collection.collectionId

    def getCollection(self, collectionId):
        collectionJson = self.requester.getCollection(collectionId)
        collection = Collection(collectionJson)
        collection.addWidgets(self.getWidgets(collection.collectionId))
        return collection

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
