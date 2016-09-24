from .requester import Requester
from lib.models.collection import Collection
from lib.models.widget import Widget
from .collectionService import CollectionService
from .widgetService import WidgetService

class App(object):

    def __init__(self, email, password, organizationId):
        self.requester = Requester(email, password, organizationId)
        self.widgetService = WidgetService(self.requester)
        self.collectionService = CollectionService(self.requester, self.widgetService)

    def createWeeklyBoard(self, collection_name):
        collectionId = self.collectionService.getCollectionIdFromName(collection_name)
        collection = self.collectionService.getCollection(collectionId)
        nextBoardName = collection.getNextDailyGoalsName()
        self.widgetService.addWeeklyBoard(collection, nextBoardName)
