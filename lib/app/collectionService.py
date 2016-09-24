from lib.models.collection import Collection

class CollectionService(object):
    def __init__(self, requester, widgetService):
        self.requester = requester 
        self.widgetService = widgetService

    def getCollectionIdFromName(self, collection_name):
        collectionsJson = self.requester.getCollections()
        for collectionJson in collectionsJson['entities']:
            collection = Collection(collectionJson)
            if collection_name in collection.name:
                return collection.collectionId

    def getCollection(self, collectionId):
        collectionJson = self.requester.getCollection(collectionId)
        collection = Collection(collectionJson)
        collection.addWidgets(self.widgetService.getWidgets(collection.collectionId))
        return collection
